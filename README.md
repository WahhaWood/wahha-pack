# Wahha Pack

Модовая сборка для сервера (Minecraft 26.1.2 + NeoForge 26.1.2.114).
Раздаётся через packwiz.

## Как это работает

- `pack.toml` — манифест сборки
- `index.toml` — список файлов с хешами
- `mods/*.pw.toml` — метаданные модов (сами jar не хранятся, качаются с Modrinth)

## Публикация на GitHub Pages (5 минут)

1. Создай репозиторий `wahha-pack` на github.com (public).
2. В папке с этим файлом выполни:
   ```
   git init
   git add -A
   git commit -m "Начальная сборка"
   git branch -M main
   git remote add origin https://github.com/ТВОЙ_НИК/wahha-pack.git
   git push -u origin main
   ```
3. На GitHub: Settings -> Pages -> Source: `Deploy from a branch`,
   Branch: `main`, папка `/ (root)` -> Save.
4. Через минуту сборка будет доступна по адресу:
   ```
   https://ТВОЙ_НИК.github.io/wahha-pack/pack.toml
   ```
5. Этот адрес впиши в `config.json` лаунчера (`packUrl`).

## Обновление сборки

При добавлении модов обновляй `index.toml` (скриптом, которым собиралась
папка) и коммить изменения. packwiz-installer у игроков сам подтянет дельту.
