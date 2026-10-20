<div align="center">

# ATM10-Wahha

**Модовая сборка на основе All the Mods 10: 386 модов, свой оверлей и свои моды. Раздаётся через WLauncher.**

![Minecraft](https://img.shields.io/badge/Minecraft-1.21.1-62B47A)
![NeoForge](https://img.shields.io/badge/NeoForge-21.1.255-E68C2D)
![Release](https://img.shields.io/github/v/release/WahhaWood/wahha-pack)

</div>

Репозиторий — не сам набор модов, а его раздача: манифест, скрипты сборки и удалённый
конфиг лаунчера. Архивы с модами лежат в [Releases](https://github.com/WahhaWood/wahha-pack/releases),
а [WLauncher](https://github.com/WahhaWood/WLauncher) по манифесту скачивает и обновляет игру.

## Из чего состоит сборка

- **Основа.** Профиль All the Mods 10 (ATM10), Minecraft 1.21.1, NeoForge 21.1.255.
- **Оверлей.** Наши конфиги, скрипты KubeJS, ассеты и шейдерпаки поверх основы.
- **Свои моды.** Собираются из исходников и попадают в сборку как локальные jar:
  [Botania Reforged](https://github.com/WahhaWood/botaniareforged),
  [IndustrialReforged](https://github.com/WahhaWood/industrialreforged),
  [Thaumic Reforged](https://github.com/WahhaWood/thaumicreforged) и несколько небольших утилит.

Текущая версия указана в `manifest.json` (поле `packVersion`).

## Что где лежит

| Файл | Назначение |
| --- | --- |
| `manifest.json` | индекс клиентской сборки с SHA-256 каждого архива. **Главный файл**, его читает WLauncher |
| `launcher.json` | удалённый конфиг лаунчера: адрес сервера, ник по умолчанию, объём памяти |
| `build-pack.py` | собирает клиентскую раздачу из профиля Modrinth |
| `build-server.py` | собирает серверный архив из того же профиля |
| `NEXT.md` | журнал последних выпусков и то, что осталось сделать |

## Как это работает

```
профиль Modrinth ──► build-pack.py ──► mods-*.zip, overlay-config.zip, kubejs-*.zip, shaderpacks.zip
                                   └─► manifest.json ──► GitHub Pages ──► WLauncher
                                       zip-архивы     ──► GitHub Releases ──┘
```

Манифест раздаётся с GitHub Pages, архивы — из Releases (в git лимит файла 100 МБ, в Releases 2 ГБ).
В `manifest.json` записаны адрес архивов (`baseUrl`), версии Minecraft и NeoForge и хеши, по которым
лаунчер понимает, что нужно докачать.

## Выпуск новой версии

1. Поставьте или обновите мод в профиле Modrinth.
2. Соберите раздачу:
   ```bash
   python3 build-pack.py --tag v8.2-wahha.56 --out out56
   ```
   По умолчанию берётся профиль `~/.local/share/ModrinthApp/profiles/All the Mods 10 - ATM10`.
   Флаги `--profile`, `--out`, `--minecraft`, `--neoforge` переопределяют значения.
3. Проверьте `manifest.json` и состав архивов: скрипт печатает, что пропущено.
4. Запушьте манифест и загрузите архивы в релиз с тем же тегом:
   ```bash
   git add manifest.json && git commit -m "v8.2-wahha.56" && git push
   gh release create v8.2-wahha.56 --title v8.2-wahha.56 --notes "" out56/*.zip
   ```
5. Сервер: `python3 build-server.py --tag v8.2-wahha.56-srv --serverfiles <папка с файлами сервера>`.
   Архив `ATM10-Wahha-server-<tag>.zip` создаётся в `--out`.

В раздачу **не** попадают: сохранения, бэкапы, логи, краш-репорты, `options.txt`, `usercache.json`,
пользовательские шейдеры и служебные файлы модов, которые держат блокировку. Полный список — в
докстринге `build-pack.py`.

## Совместимость

Манифест читает WLauncher версии 1.0.4 и новее. Более старые версии лаунчера использовали
формат packwiz, который больше не поддерживается: их нужно обновить.

## Лицензии

Скрипты и манифест этого репозитория — авторские. Моды сборки принадлежат их авторам и
распространяются на условиях своих лицензий.
