#!/usr/bin/env python3
"""
Добавляет локальный .jar в сборку (для модов, которых нет на Modrinth).

Использование:
  python3 add-jar.py /путь/к/Mod-1.2.0.jar                 # имя сохранится
  python3 add-jar.py /путь/к/mod.jar mods/Mod-1.2.0.jar    # своё имя в сборке

Jar копируется в mods/ и индексируется в index.toml со своим sha256.
Игроки скачают его прямо с хостинга сборки (GitHub Pages), packwiz
сверит хеш и положит в mods/.

После запуска:
  git add -A && git commit -m "Добавлен мод X" && git push
"""
import hashlib
import os
import shutil
import sys


def rebuild_index_and_pack():
    lines = ['hash-format = "sha256"\n']
    for name in sorted(os.listdir('mods')):
        path = f'mods/{name}'
        if not os.path.isfile(path):
            continue
        digest = hashlib.sha256(open(path, 'rb').read()).hexdigest()
        if name.endswith('.pw.toml'):
            lines.append(f'[[files]]\nfile = "{path}"\nhash = "{digest}"\nmetafile = true\n')
        else:
            lines.append(f'[[files]]\nfile = "{path}"\nhash = "{digest}"\n')
    with open('index.toml', 'w') as fh:
        fh.write('\n'.join(lines))

    index_hash = hashlib.sha256(open('index.toml', 'rb').read()).hexdigest()
    pack = f'''name = "Wahha Test Pack"
author = "Wahha"
version = "1.0.0"
pack-format = "packwiz:1.1.0"

[index]
file = "index.toml"
hash-format = "sha256"
hash = "{index_hash}"

[versions]
minecraft = "26.1.2"
neoforge = "26.1.2.114"
'''
    with open('pack.toml', 'w') as fh:
        fh.write(pack)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    src = sys.argv[1]
    if not os.path.isfile(src):
        print(f'!! Файл не найден: {src}')
        sys.exit(1)
    if not src.endswith('.jar'):
        print('!! Это не .jar файл')
        sys.exit(1)

    os.makedirs('mods', exist_ok=True)
    dest_name = sys.argv[2] if len(sys.argv) > 2 else os.path.basename(src)
    dest = os.path.join('mods', dest_name)

    if os.path.abspath(src) != os.path.abspath(dest):
        shutil.copy2(src, dest)

    rebuild_index_and_pack()
    size_kb = os.path.getsize(dest) / 1024
    print(f'OK  {dest} ({size_kb:.0f} КБ)')
    print('index.toml и pack.toml пересобраны. Не забудь git commit && git push.')


if __name__ == '__main__':
    main()
