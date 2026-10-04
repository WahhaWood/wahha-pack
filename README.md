# Wahha Pack

Модовая сборка для сервера (Minecraft 26.1.2 + NeoForge 26.1.2.114).
Раздаётся через packwiz.

## Как это работает

- `pack.toml` — манифест сборки
- `index.toml` — список файлов с хешами
- `mods/*.pw.toml` — метаданные модов с Modrinth (сами jar не хранятся, качаются с CDN)
- `mods/*.jar` — локальные моды (свои или отсутствующие на Modrinth), раздаются прямо с хостинга сборки

## Добавление модов

**Мод есть на Modrinth:**
```
python3 add-mod.py sodium
python3 add-mod.py sodium "sodium-neoforge-0.9.2+mc26.1.2.jar"   # точная версия
```

**Мода нет на Modrinth (свой мод или jar скачан вручную):**
```
python3 add-jar.py /путь/к/MyMod-1.0.0.jar
python3 add-jar.py /путь/к/mod.jar MyMod-1.0.0.jar    # своё имя в сборке
```

После любого из скриптов:
```
git add -A && git commit -m "Добавлен мод X" && git push
```

Примечание: локальные jar-ы без `.pw.toml` устанавливаются всем (и клиенту,
и серверу) — флага стороны у них нет. Если мод строго клиентский и это важно,
проще всего указать `side = "client"` вручную — но для раздачи друзьям это
не критично: лишний мод на сервере просто не загрузится, если он клиентский.

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
