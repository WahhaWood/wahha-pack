#!/usr/bin/env python3
"""
Добавляет или обновляет мод из Modrinth в сборку.

Использование:
  python3 add-mod.py sodium
  python3 add-mod.py sodium "sodium-neoforge-0.9.2+mc26.1.2.jar"   # точный файл

После запуска:
  git add -A && git commit -m "Добавлен мод X" && git push
"""
import hashlib
import json
import os
import sys
import urllib.parse
import urllib.request

GAME_VERSION = "26.1.2"
LOADER = "neoforge"

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "wahha-pack/1.0"})
    return json.load(urllib.request.urlopen(req))

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    slug = sys.argv[1]
    want_file = sys.argv[2] if len(sys.argv) > 2 else None

    gv = urllib.parse.quote(json.dumps([GAME_VERSION]))
    ld = urllib.parse.quote(json.dumps([LOADER]))
    versions = get(f"https://api.modrinth.com/v2/project/{slug}/version?game_versions={gv}&loaders={ld}")
    if not versions:
        print(f"!! У проекта {slug} нет версий для {GAME_VERSION}/{LOADER}")
        sys.exit(1)

    chosen = None
    chosen_file = None
    for v in versions:
        for f in v["files"]:
            if want_file is None or f["filename"] == want_file:
                chosen, chosen_file = v, f
                break
        if chosen:
            break
    if not chosen:
        chosen = versions[0]
        chosen_file = chosen["files"][0]

    filename = chosen_file["filename"]
    toml = f'''name = "{chosen['name'].replace('"', '')}"
filename = "{filename}"
side = "client"

[download]
hash-format = "sha1"
hash = "{chosen_file['hashes']['sha1']}"
url = "{chosen_file['url']}"

[update.modrinth]
mod-id = "{chosen['project_id']}"
version = "{chosen['id']}"
'''
    mod_path = f"mods/{slug}.pw.toml"
    with open(mod_path, "w") as fh:
        fh.write(toml)
    print(f"OK  {slug}: {filename}")

    # пересобрать index.toml
    lines = ['hash-format = "sha256"\n']
    for name in sorted(os.listdir("mods")):
        p = f"mods/{name}"
        h = hashlib.sha256(open(p, "rb").read()).hexdigest()
        lines.append(f'[[files]]\nfile = "{p}"\nhash = "{h}"\nmetafile = true\n')
    with open("index.toml", "w") as fh:
        fh.write("\n".join(lines))

    ih = hashlib.sha256(open("index.toml", "rb").read()).hexdigest()
    pack = f'''name = "Wahha Test Pack"
author = "Wahha"
version = "1.0.0"
pack-format = "packwiz:1.1.0"

[index]
file = "index.toml"
hash-format = "sha256"
hash = "{ih}"

[versions]
minecraft = "{GAME_VERSION}"
neoforge = "26.1.2.114"
'''
    with open("pack.toml", "w") as fh:
        fh.write(pack)
    print("index.toml и pack.toml пересобраны. Не забудь git commit && git push.")

if __name__ == "__main__":
    main()
