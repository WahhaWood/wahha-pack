#!/usr/bin/env python3
"""Сборка клиентской раздачи ATM10 для WLauncher.

Берёт эталонный профиль (по умолчанию твой Modrinth-профиль) и пакует
только обязательные папки в несколько архивов:

  mods-0.zip … mods-f.zip — mods/*.jar, разложенные по 16 корзинам по
                             md5(имени). Привязка стабильна: добавление или
                             обновление пары модов меняет 1–2 архива (~70М),
                             а не всю сборку.
  overlay-config.zip       — config/ + defaultconfigs/
  kubejs-assets.zip        — kubejs/assets/ (тяжёлое, меняется редко)
  kubejs-code.zip          — остальной kubejs (скрипты, data, config)
  shaderpacks.zip          — shaderpacks/*.zip (шейдеры требует EuphoriaPatcher;
                             без них висит красная ошибка SHADER NOT FOUND)

Плюс manifest.json с SHA-256 каждого архива, списком модов (чистка
устаревших jar) и списком файлов оверлея (чистка удалённых конфигов —
движок удаляет только то, что сам когда-то распаковал).

Что НЕ пакуется (локальное/генерируемое): saves, backups, journeymap,
local, logs, crash-reports, dynamic-*-cache, .cache, .mixin.out, .sable,
libraries-integratedscripting, shaderpacks/resourcepacks пользователя,
options.txt, usercache.json, servers.dat/hotbar.nbt (симлинки), ESM,
blueprints, screenshots, downloads, mods/.index, mods/_disabled_orphans.

Использование:
  python3 build-pack.py --tag v8.2-wahha.1
  python3 build-pack.py --tag v8.2-wahha.1 --profile /путь/к/профилю --out /tmp/pack-out

Дальше:
  1. Проверь manifest.json и состав архивов.
  2. git add manifest.json && git commit && git push
  3. Залей zip в GitHub Releases с тем же тегом:
       gh release create <tag> --title <tag> --notes "" out/*.zip
     (manifest.json раздаётся с GitHub Pages, zip — из Releases: лимит
     файла в git 100М, в Releases — 2Г.)
"""

import argparse
import hashlib
import json
import os
import sys
import zipfile

DEFAULT_PROFILE = os.path.expanduser(
    "~/.local/share/ModrinthApp/profiles/All the Mods 10 - ATM10"
)

# Корзин для шардирования mods/. Стабильная привязка по md5(имени файла):
# обновление пары модов затрагивает 1–2 корзины вместо всей сборки.
MODS_SHARDS = 16

# Служебный мусор лаунчеров внутри mods/ — никогда не часть сборки.
MODS_EXCLUDE_DIRS = {".index", "_disabled_orphans"}

# Игровой мусор внутри config/kubejs — генерируется при игре, личный или
# пересоздаётся сам (поисковые индексы, бекапы, JEI-закладки, XRay-стор).
OVERLAY_EXCLUDE_SUFFIXES = (".bak", ".backup", "_backup1", "_backup2", ".etag")
OVERLAY_EXCLUDE_PARTS = ("/search_index/", "jei/world/", "/xray/")


def is_overlay_junk(rel):
    low = rel.replace(os.sep, "/").lower()
    if low.endswith(OVERLAY_EXCLUDE_SUFFIXES):
        return True
    return any(p in low for p in OVERLAY_EXCLUDE_PARTS)


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def shard_of(name):
    return int(hashlib.md5(name.encode("utf-8")).hexdigest()[0], 16) % MODS_SHARDS


def collect_mods(profile):
    """Только jar из корня mods/. Возвращает [(имя, полный путь)]."""
    mods_dir = os.path.join(profile, "mods")
    if not os.path.isdir(mods_dir):
        sys.exit(f"Нет папки mods в профиле: {profile}")
    result = []
    for name in sorted(os.listdir(mods_dir)):
        full = os.path.join(mods_dir, name)
        if os.path.isfile(full) and name.endswith(".jar"):
            result.append((name, full))
    if not result:
        sys.exit("В mods/ не найдено ни одного jar — проверь профиль.")
    return result


def collect_overlay(profile):
    """Все файлы из config/, defaultconfigs/, kubejs/.

    Возвращает [(путь_в_архиве, полный путь, имя_архива)] — оверлей разбит
    по частоте изменений, чтобы правка скрипта не тянула 180М ассетов.
    """
    groups = {
        "overlay-config.zip": ("config", "defaultconfigs"),
        "kubejs-assets.zip": (os.path.join("kubejs", "assets"),),
        "kubejs-code.zip": None,  # остальной kubejs, собирается ниже
    }
    result = []
    for archive, dirnames in groups.items():
        if dirnames is None:
            continue
        for dirname in dirnames:
            root = os.path.join(profile, dirname)
            if not os.path.isdir(root):
                sys.exit(f"Нет обязательной папки {dirname} в профиле: {profile}")
            result.extend((archive, rel, full)
                          for rel, full in walk_files(profile, root))
    # kubejs целиком минус assets
    kubejs_root = os.path.join(profile, "kubejs")
    if not os.path.isdir(kubejs_root):
        sys.exit(f"Нет обязательной папки kubejs в профиле: {profile}")
    assets_root = os.path.join(kubejs_root, "assets") + os.sep
    # kubejs целиком минус assets
    kubejs_root = os.path.join(profile, "kubejs")
    if not os.path.isdir(kubejs_root):
        sys.exit(f"Нет обязательной папки kubejs в профиле: {profile}")
    assets_root = os.path.join(kubejs_root, "assets") + os.sep
    for rel, full in walk_files(profile, kubejs_root):
        if full.startswith(assets_root):
            continue
        result.append(("kubejs-code.zip", rel, full))
    # Шейдеры: только zip из корня (распакованные папки и чужое не тащим).
    # EuphoriaPatcher требует Complementary в папке, иначе красная ошибка.
    shaders_root = os.path.join(profile, "shaderpacks")
    if os.path.isdir(shaders_root):
        for fn in sorted(os.listdir(shaders_root)):
            full = os.path.join(shaders_root, fn)
            if os.path.isfile(full) and fn.endswith(".zip"):
                result.append(("shaderpacks.zip",
                               os.path.join("shaderpacks", fn), full))
    return result


def walk_files(profile, root):
    """Все файлы под root. Возвращает [(путь_в_архиве, полный путь)]."""
    out = []
    for dirpath, _dirnames, filenames in os.walk(root):
        for fn in sorted(filenames):
            full = os.path.join(dirpath, fn)
            # Симлинки (servers.dat и т.п.) — не часть сборки.
            if os.path.islink(full):
                print(f"  пропуск симлинка: {os.path.relpath(full, profile)}")
                continue
            rel = os.path.relpath(full, profile)
            if is_overlay_junk(rel):
                print(f"  пропуск мусора: {rel}")
                continue
            out.append((rel, full))
    return out


def write_zip(path, entries):
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
        for arc, full in entries:
            zf.write(full, arc)
    return os.path.getsize(path)


def main():
    ap = argparse.ArgumentParser(description="Сборка раздачи ATM10 для WLauncher")
    ap.add_argument("--profile", default=DEFAULT_PROFILE)
    ap.add_argument("--out", default=".",
                    help="Куда положить архивы и manifest.json")
    ap.add_argument("--tag", required=True,
                    help="Тег GitHub Release, напр. v8.2-wahha.1")
    ap.add_argument("--version", default=None,
                    help="Версия сборки (по умолчанию = tag)")
    ap.add_argument("--repo", default="WahhaWood/wahha-pack")
    ap.add_argument("--minecraft", default="1.21.1")
    ap.add_argument("--neoforge", default="21.1.255")
    args = ap.parse_args()

    profile = os.path.abspath(os.path.expanduser(args.profile))
    out = os.path.abspath(os.path.expanduser(args.out))
    version = args.version or args.tag
    os.makedirs(out, exist_ok=True)

    print(f"Профиль: {profile}")
    mods = collect_mods(profile)
    print(f"Модов: {len(mods)}")
    overlay = collect_overlay(profile)
    print(f"Файлов оверлея (config+defaultconfigs+kubejs): {len(overlay)}")

    # Контроль кастомных правок: фикс звезды должен попасть в архив.
    star_fix = os.path.join("kubejs", "server_scripts", "modpack",
                            "atm_star_assembly.js")
    if not any(a == star_fix for _, a, _ in overlay):
        sys.exit(f"ВНИМАНИЕ: в сборке нет {star_fix} — проверь профиль!")

    archives = []  # (имя архива, [(путь_в_архиве, полный путь)])
    buckets = {}
    for name, full in mods:
        buckets.setdefault(shard_of(name), []).append((f"mods/{name}", full))
    for i in sorted(buckets):
        archives.append((f"mods-{i:x}.zip", buckets[i]))
    overlay_groups = {}
    for archive, arc, full in overlay:
        overlay_groups.setdefault(archive, []).append((arc, full))
    for archive in ("overlay-config.zip", "kubejs-assets.zip", "kubejs-code.zip", "shaderpacks.zip"):
        if overlay_groups.get(archive):
            archives.append((archive, overlay_groups[archive]))

    print("Паковка…")
    for archive, entries in archives:
        write_zip(os.path.join(out, archive), entries)

    base_url = (f"https://github.com/{args.repo}"
                f"/releases/download/{args.tag}/")
    files = []
    for archive, _entries in archives:
        full = os.path.join(out, archive)
        files.append({"name": archive,
                      "sha256": sha256_of(full),
                      "size": os.path.getsize(full)})
    manifest = {
        "pack": "ATM10-Wahha",
        "packVersion": version,
        "minecraft": args.minecraft,
        "neoforge": args.neoforge,
        "baseUrl": base_url,
        "files": files,
        # Точный состав mods/ — движок удалит у игрока jar, которых тут нет.
        "mods": [n for n, _ in mods],
        # Все файлы оверлея — движок удалит ранее установленные, которых
        # тут больше нет (чужое/сгенерированное не трогает).
        "overlay": sorted(arc for _, arc, _ in overlay),
    }
    manifest_path = os.path.join(out, "manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
        f.write("\n")

    total = sum(f["size"] for f in files)
    print(f"Готово: {len(archives)} архивов, всего {total / 1024 / 1024:.0f} МБ")
    for f in files:
        print(f"  {f['name']}: {f['size'] / 1024 / 1024:.0f} МБ")
    print(f"Версия: {version} | NeoForge: {args.neoforge}")
    print("Дальше:")
    print(f"  cp {manifest_path} <корень wahha-pack>/ && git add manifest.json && "
          "git commit -m \"Pack {v}\" && git push".format(v=version))
    print(f"  gh release create {args.tag} --title {args.tag} "
          f"--notes \"\" {out}/*.zip")


if __name__ == "__main__":
    main()
