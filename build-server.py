#!/usr/bin/env python3
"""Сборка цельного серверного zip для хостинга.

Состав:
  база   — ServerFiles-8.2: startserver.sh/.bat, neoforge-installer,
           user_jvm_args.txt, server-icon.png, datapacks/, defaultconfigs/,
           local/kubejs/dev.json
  моды   — из твоего профиля МИНУС клиентские (рендер/звук/UI/шейдеры —
           на выделенном сервере они не нужны, а часть вообще крашит его)
  config — целиком из профиля (под вырезанный набор + добавленные моды)
  kubejs — из профиля БЕЗ assets/ и client_scripts/ (как в сервер-паке)

Использование:
  unzip -q ~/Загрузки/ServerFiles-8.2.zip -d /tmp/sf
  python3 build-server.py --serverfiles /tmp/sf --tag v8.2-wahha.1-srv --out /tmp
"""

import argparse
import os
import shutil
import sys
import zipfile

DEFAULT_PROFILE = os.path.expanduser(
    "~/.local/share/ModrinthApp/profiles/All the Mods 10 - ATM10"
)

# Рантайм сервер-пака — едет как есть.
SERVERFILES_KEEP = (
    "startserver.sh",
    "startserver.bat",
    "user_jvm_args.txt",
    "server-icon.png",
    "neoforge-21.1.251-installer.jar",
    "datapacks",
    "local",
)

# Клиентские моды из профиля — на сервер НЕ едут.
CLIENT_ONLY_MODS = {
    "AsyncParticles-21.1.4.5+1.21.1.jar",
    "BadOptimizations-2.4.1-1.21.1.jar",
    "BetterAdvancements-NeoForge-1.21.1-0.4.3.21.jar",
    "chloride-NEOFORGE-mc1.21.1-v1.8.1.jar",
    "colorfulhearts-neoforge-1.21.1-10.5.9.jar",
    "colorwheel-neoforge-1.3.0-beta3+mc1.21.1.jar",
    "colorwheel_patcher-neoforge-1.0.5+mc1.21.1.jar",
    "darkmodeeverywhere-neoforge-1.21.1-1.4.0.jar",
    "dynamic-fps-3.11.4+minecraft-1.21.0-neoforge.jar",
    "entityculling-neoforge-1.11.2-mc1.21.1.jar",
    "EuphoriaPatcher-1.10.5-r5.9.3-neoforge.jar",
    "ExtremeSoundMuffler-3.56_NeoForge-1.21.jar",
    "iris-neoforge-1.8.14-beta.1+mc1.21.1.jar",
    "justzoom_neoforge_2.1.0_MC_1.21.1.jar",
    "keybindbundles-1.4.0.jar",
    "konkrete_neoforge_1.9.9_MC_1.21.jar",
    "modelfix-1.21-1.10.jar",
    "moreculling-neoforge-1.21.1-1.0.10.jar",
    "moreoverlays-1.24.2-mc1.21.1-neoforge.jar",
    "NeoAuth-1.21.1-1.0.1.jar",
    "notenoughanimations-neoforge-1.12.6-mc1.21.1.jar",
    "dynamiclights-1.21.1.2NF.jar",
    "smithingtemplateviewer-1.0.4.jar",
    "sodium-extra-neoforge-0.9.4+mc1.21.1.jar",
    "sodium-neoforge-0.8.13+mc1.21.1.jar",
}


def copy_tree(src, dst):
    shutil.copytree(src, dst, symlinks=False, ignore_dangling_symlinks=True)


def main():
    ap = argparse.ArgumentParser(description="Сборка серверного zip")
    ap.add_argument("--profile", default=DEFAULT_PROFILE)
    ap.add_argument("--serverfiles", required=True,
                    help="Распакованный ServerFiles-8.2.zip")
    ap.add_argument("--tag", required=True, help="Напр. v8.2-wahha.1-srv")
    ap.add_argument("--out", default=".")
    args = ap.parse_args()

    profile = os.path.abspath(os.path.expanduser(args.profile))
    sf = os.path.abspath(os.path.expanduser(args.serverfiles))
    out = os.path.abspath(os.path.expanduser(args.out))
    stage = os.path.join(out, f"stage-{args.tag}")
    shutil.rmtree(stage, ignore_errors=True)
    os.makedirs(stage)

    # 1. Рантайм из сервер-пака.
    for name in SERVERFILES_KEEP:
        src = os.path.join(sf, name)
        if not os.path.exists(src):
            print(f"  нет в сервер-паке (пропуск): {name}")
            continue
        dst = os.path.join(stage, name)
        if os.path.isdir(src):
            copy_tree(src, dst)
        else:
            shutil.copy2(src, dst)

    # 2. defaultconfigs: профиль + недостающее из сервер-пака.
    copy_tree(os.path.join(profile, "defaultconfigs"),
              os.path.join(stage, "defaultconfigs"))
    for dirpath, _d, fns in os.walk(os.path.join(sf, "defaultconfigs")):
        for fn in fns:
            full = os.path.join(dirpath, fn)
            rel = os.path.relpath(full, sf)
            dst = os.path.join(stage, rel)
            if not os.path.exists(dst):
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.copy2(full, dst)
                print(f"  defaultconfigs из сервер-пака: {rel}")

    # 3. config целиком из профиля.
    copy_tree(os.path.join(profile, "config"), os.path.join(stage, "config"))

    # 4. kubejs из профиля без assets/ и client_scripts/.
    for dirpath, _d, fns in os.walk(os.path.join(profile, "kubejs")):
        rel_dir = os.path.relpath(dirpath, profile)
        parts = rel_dir.split(os.sep)
        if len(parts) > 1 and parts[1] in ("assets", "client_scripts"):
            continue
        for fn in fns:
            full = os.path.join(dirpath, fn)
            if os.path.islink(full):
                continue
            rel = os.path.relpath(full, profile)
            dst = os.path.join(stage, rel)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(full, dst)

    # 5. Моды из профиля минус клиентские.
    mods_src = os.path.join(profile, "mods")
    mods_dst = os.path.join(stage, "mods")
    os.makedirs(mods_dst)
    kept, dropped = 0, []
    for name in sorted(os.listdir(mods_src)):
        full = os.path.join(mods_src, name)
        if not (os.path.isfile(full) and name.endswith(".jar")):
            continue
        if name in CLIENT_ONLY_MODS:
            dropped.append(name)
            continue
        shutil.copy2(full, os.path.join(mods_dst, name))
        kept += 1
    print(f"Модов на сервер: {kept}, выкинуто клиентских: {len(dropped)}")

    # Контроль: фикс звезды обязан быть внутри.
    star_fix = os.path.join(
        stage, "kubejs", "server_scripts", "modpack", "atm_star_assembly.js")
    if not os.path.isfile(star_fix):
        sys.exit("ВНИМАНИЕ: в сборке нет atm_star_assembly.js!")

    # 6. Упаковка.
    zip_path = os.path.join(out, f"ATM10-Wahha-server-{args.tag}.zip")
    if os.path.exists(zip_path):
        os.remove(zip_path)
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED,
                         compresslevel=6) as zf:
        for dirpath, _d, fns in os.walk(stage):
            for fn in fns:
                full = os.path.join(dirpath, fn)
                zf.write(full, os.path.relpath(full, stage))
    shutil.rmtree(stage, ignore_errors=True)
    size_mb = os.path.getsize(zip_path) / 1024 / 1024
    print(f"Готово: {zip_path} ({size_mb:.0f} МБ)")
    print("На хостинге: распаковать, принять EULA, запустить startserver.sh.")


if __name__ == "__main__":
    main()
