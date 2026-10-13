# ATM10-Wahha: сборка для игроков и сервера

Раздача модовой сборки **ATM10-Wahha** для WLauncher и для сервера. Основа — профиль All the Mods 10 (ATM10) в Modrinth, поверх него наш оверлей (конфиги, kubejs, свои моды).

Текущая версия: `v8.2-wahha.37` (см. `manifest.json`). Minecraft 1.21.1, NeoForge 21.1.255.

## Что где лежит

| Файл | Назначение |
|---|---|
| `build-pack.py` | собирает клиентскую раздачу: `mods-0…f.zip`, `overlay-config.zip`, `kubejs-assets.zip`, `kubejs-code.zip`, `shaderpacks.zip` и `manifest.json` с SHA-256 |
| `build-server.py` | собирает серверный архив `ATM10-Wahha-server-<tag>.zip` из того же профиля |
| `manifest.json` | индекс текущей клиентской сборки. **Главный файл**, его читает WLauncher |
| `launcher.json` | удалённый конфиг лаунчера: адрес сервера, ник, RAM |
| `NEXT.md` | статус последнего деплоя |

## Выпуск новой версии

1. Поставь новый мод в профиль Modrinth (или обнови jar в `mods/` профиля).
2. Собери клиентскую раздачу:
   ```bash
   python3 build-pack.py --tag v8.2-wahha.38
   # по умолчанию профиль: ~/.local/share/ModrinthApp/profiles/All the Mods 10 - ATM10
   # --profile <путь>, --out <папка>, --minecraft, --neoforge переопределяют значения по умолчанию
   ```
3. Проверь `manifest.json` и состав архивов в папке `--out` (по умолчанию текущая). Скрипт печатает, что пропущено (симлинки, мусор).
4. Закоммить и запуши манифест, затем залей zip в GitHub Release с тем же тегом:
   ```bash
   git add manifest.json && git commit -m "v8.2-wahha.38" && git push
   gh release create v8.2-wahha.38 --title v8.2-wahha.38 --notes "" out/*.zip
   ```
   Манифест раздаётся с GitHub Pages, zip-архивы — из Releases (лимит файла в git 100 МБ, в Releases 2 ГБ).
5. Сервер: `python3 build-server.py --tag v8.2-wahha.38-srv --serverfiles <папка с файлами сервера>`. Архив `ATM10-Wahha-server-<tag>.zip` создаётся в `--out`.

Что `build-pack.py` **не** пакует: сохранения, бэкапы, логи, краш-репорты, `options.txt`, `usercache.json`, шейдеры пользователя и служебные данные модов, которые держат лок (`config/euphoria_patcher/.data.json`). Полный список в docstring скрипта.

## Как WLauncher читает сборку

`manifestUrl` в `config.json` лаунчера (и в `launcher.json` этого репозитория) — единственный источник сборки. Запасного пути (packwiz) больше нет: старые файлы `pack.toml`, `index.toml`, `mods/*.pw.toml`, `add-mod.py`, `add-jar.py` удалены. Лаунчер 1.0.4 и новее берёт `manifest.json`. Более старые версии лаунчера могли читать packwiz, их нужно обновить (старые установщики удалены из `WLauncher/dist`).

## Связи

- Наши моды из `../MODS` попадают в сборку как локальные jar: `botania` (`../botaniareforged-core`), `industrialreforged`, `thaumcraft`, `degrinderturbo`, `eawireless`, `ejecttweak`.
- `ae2channels-1.1.4.jar` в сборке — **донорская** версия. Наш форк `1.1.4-nw1` ещё не выпущен в пак (см. `../ae2channels/NEXT.md`).
- Сборка нужна лаунчеру: [`../WLauncher`](../WLauncher/README.md).
