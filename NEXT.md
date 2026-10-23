# NEXT — v8.2-wahha.61: IR 1.1.9.3-beta

- [x] IR 1.1.9.2-beta → 1.1.9.3-beta: иридиевая руда в сканере 6000 UU (молекулярка 320M без изменений)
- [x] `build-pack.py --tag v8.2-wahha.61 --out out61`, GitHub Release v8.2-wahha.61
- [ ] Сервер: заменить `industrialreforged-*.jar` на `1.1.9.3-beta`
- [ ] Игру в профиле перезапустить; откат — zip из `out60`

# Прошлый релиз: v8.2-wahha.60: IR 1.1.9.2-beta

- [x] IR 1.1.9.1-beta → 1.1.9.2-beta: иридиевая руда дешевле на треть (сканер 9999 → 6666 UU, молекулярка 480M → 320M)
- [x] `build-pack.py --tag v8.2-wahha.60 --out out60`, GitHub Release v8.2-wahha.60
- [ ] Сервер: заменить `industrialreforged-1.1.9-beta.jar` (или 1.1.9.1) на `1.1.9.2-beta`
- [ ] Игру в профиле перезапустить; откат — zip из `out59`

# Прошлый релиз: v8.2-wahha.59: IR 1.1.9.1-beta

- [x] IR 1.1.9-beta → 1.1.9.1-beta: ME-репликатор и ME-генератор материи без лимита за тик, остальные ME-машины ×4 крафтов (1024 → 4096), ME-утилизатор ×4
- [x] `build-pack.py --tag v8.2-wahha.59 --out out59`, GitHub Release v8.2-wahha.59
- [ ] Сервер: заменить `industrialreforged-1.1.9-beta.jar` на `1.1.9.1-beta`
- [ ] Игру в профиле перезапустить; откат — zip из `out58`

# Прошлый релиз: v8.2-wahha.58: IR 1.1.9-beta

- [x] IR 1.1.8-beta → 1.1.9-beta: шерсть (16 цветов, 62 UU ≈ 2,5M FE) в репликаторе, ME-репликатор, рудокрушитель вдвое быстрее
- [x] `build-pack.py --tag v8.2-wahha.58 --out out58`, GitHub Release v8.2-wahha.58
- [ ] Сервер: заменить `industrialreforged-1.1.8-beta.jar` на `1.1.9-beta`
- [ ] Игру в профиле перезапустить; откат — zip из `out57`

# Прошлый релиз: # NEXT.md — v8.2-wahha.57: IR 1.1.8-beta, Botania 1.2.0, Thaumcraft 1.0.8.0

- [x] IR 1.1.7.3-beta → 1.1.8-beta (`e8d24637…`): ME-машины для рецептов Botania (инфузер маны, аптекарь, рунический алтарь, агломерационная фабрика, рынок Альфхейма), один CPU-миксин на оба семейства машин
- [x] Botania 1.1.5 → 1.2.0 (`8a2f9393…`): AE2 необязателен, ME-машины рецептов переехали в IR (нужны оба мода вместе)
- [x] Thaumcraft 1.0.7.0 → 1.0.8.0 (`1eddbadc…`): аспекты для предметов IR, Botania, AE2 и металлов по общим тегам
- [x] `build-pack.py --tag v8.2-wahha.57 --out out57`, GitHub Release v8.2-wahha.57 (20/20)
- [x] GitHub Pages: проверено — отдаёт v8.2-wahha.57
- [ ] Сервер: заменить `botania-neoforge-1.21.1-1.1.5.jar` на `1.2.0`, `industrialreforged-1.1.7.3-beta.jar` на `1.1.8-beta`, `thaumcraft-1.0.7.0.jar` на `1.0.8.0`
- [ ] Игру в профиле перезапустить; откат — zip из `out56`

# Прошлый релиз: v8.2-wahha.55: Botania 1.1.5

- [x] Botania 1.1.4 → 1.1.5 (`f5660235…`) из `../MODS`: запись «Симулятор Гайи» в Лексике (Alfhomancy, с визуализацией мультиблока); структура симулятора дороже: плита 3×3 элементиевых блоков, малахитовые блоки по сторонам основания (вместо элементиевых). Старые симуляторы после обновления «разваливаются», пока структуру не достроят
- [x] `build-pack.py --tag v8.2-wahha.55 --out out55`: изменились mods-3, mods-a, overlay-config, kubejs-code; GitHub Release v8.2-wahha.55 (20/20)
- [ ] GitHub Pages: проверить, что `wahhawood.github.io/wahha-pack/manifest.json` отдаёт `v8.2-wahha.55`
- [ ] Сервер: заменить `mods/botania-neoforge-1.21.1-1.1.4.jar` на `1.1.5`
- [ ] Игру в профиле перезапустить; откат — zip из `out54`

# Прошлый релиз: v8.2-wahha.54: Botania 1.1.4, IR 1.1.7.2-beta

- [x] Botania 1.1.2 → 1.1.4 (`378a69a4…`) из `../MODS`: симулятор Гайи (мультиблок 3×3, 1M маны + 10 000 FE/т на 5 минут, лут сложного режима), MEGA-ячейки маны 1M–256M (рецепты при MEGA Cells), 1000 маны на байт — ёмкость mana-ячеек ×2
- [x] IR 1.1.7-beta → 1.1.7.2-beta (`e771505a…`): лежал в профиле и `../MODS` до деплоя (двойная отдача соединителя солнечных панелей). Остальные наши моды совпали с профилем
- [x] `build-pack.py --tag v8.2-wahha.54 --out out54`: изменились mods-3, -4, -6, -8, overlay-config, kubejs-code; состав оверлея тот же
- [ ] GitHub Pages: проверить, что `wahhawood.github.io/wahha-pack/manifest.json` отдаёт `v8.2-wahha.54`
- [ ] Сервер: заменить `mods/botania-neoforge-1.21.1-1.1.2.jar` на `1.1.4`, `industrialreforged-1.1.7-beta.jar` на `1.1.7.2-beta`
- [ ] В базе игроков: mana-ячейки стали вдвое ёмче, накопленная мана сохранилась

# Прошлый релиз: v8.2-wahha.53 — IR 1.1.7-beta

- [x] IR 1.1.7-beta (`2e8f7cfc…`) из `../MODS`: ME-генератор материи, FE-кабели к ME-узлам (2 FE = 1 AE), буфер ME-узлов закрыт для сети (сети нужен свой источник питания), модули и линзы в соединителе панелей (дождь соединителя теперь 40%, как у панели), пакетный расчёт автокрафта ME-машин, возврат входов при отмене. Остальные наши моды совпали с профилем
- [x] Профиль Modrinth: 1.1.4-beta убран в scratchpad сессии (откат — zip из `out52`), 1.1.7-beta в `mods/`
- [x] `build-pack.py --tag v8.2-wahha.53 --out out53`, манифест запушен, GitHub Release v8.2-wahha.53 (20/20)
- [ ] GitHub Pages: сразу после деплоя отдавал `.52` — проверить `wahhawood.github.io/wahha-pack/manifest.json`
- [ ] Сервер: заменить `mods/industrialreforged-1.1.3-beta.jar` на `1.1.7-beta`, `thaumcraft-1.0.6.9.jar` на `1.0.7.0`, `thaumicenergistics-1.0.5.1.jar` на `1.0.5.2` (если .52 ещё не ставился)
- [ ] В базе игроков: ME-сети с ME-машинами должны иметь источник питания; старый заряд буфера машин остаётся при них
- [ ] Игру в профиле перезапустить

# Прошлый релиз: v8.2-wahha.52

- [x] IR 1.1.4-beta (`13e5d989…`): ME-машины — расчёт автокрафта по паттернам ME-машин пакетом (0,5 → 0,05 с на 20 000), байты плана в 2–7 раз меньше, при отмене автокрафта входы из очереди машин возвращаются в сеть; очередь 10 240. dev-сервер: tests_me 37/37, tests_me_craft 11/11, bench_me ок
- [x] Thaumcraft 1.0.6.9 → 1.0.7.0 (`4f00729a…`), ThaumicEnergistics 1.0.5.1 → 1.0.5.2 (`cc170396…`) — из `../MODS`; остальные наши моды совпадали с профилем
- [x] Профиль Modrinth: старые jar убраны в scratchpad сессии (не удалены окончательно: откат — zip из `out51`), новые положены в `mods/`
- [x] `build-pack.py --tag v8.2-wahha.52 --out out52`, манифест запушен, GitHub Release v8.2-wahha.52 (20/20)
- [x] GitHub Pages: проверено — отдаёт v8.2-wahha.52; было: проверить, что `wahhawood.github.io/wahha-pack/manifest.json` отдаёт `v8.2-wahha.52`
- [ ] Сервер: заменить `mods/industrialreforged-1.1.3-beta.jar` на `1.1.4-beta`, `thaumcraft-1.0.6.9.jar` на `1.0.7.0`, `thaumicenergistics-1.0.5.1.jar` на `1.0.5.2`; botania 1.1.2 уже в .51
- [ ] Игру в профиле Modrinth перезапустить (во время деплоя она была запущена)

# Прошлый релиз: v8.2-wahha.51

- [x] Из `../MODS` взяты новые jar: `botania-neoforge-1.21.1-1.1.2.jar` (было 1.1.1), `industrialreforged-1.1.3-beta.jar` (было 1.1.2-beta). Остальные (degrinder, eawireless, ejecttweak, thaumcraft, thaumicenergistics) совпадают по SHA-256 с профилем
- [x] Профиль Modrinth: старые jar перенесены в scratchpad (не удалены), новые положены в `mods/`
- [x] `build-pack.py --tag v8.2-wahha.51 --out out51`: изменились mods-2, -4, -5, -a (jar переехали между корзинами по имени), overlay-config (только переписанный модами `ftbchunks-client.snbt` с тем же содержимым в другом порядке и даты в `iris`/`asyncparticles`), kubejs-code без изменений
- [x] Манифест запушен, GitHub Release v8.2-wahha.51 (20/20)
- [ ] GitHub Pages: проверить, что `wahhawood.github.io/wahha-pack/manifest.json` отдаёт `v8.2-wahha.51` (на момент деплоя отдавал `.50`)
- [ ] Сервер: заменить `mods/botania-neoforge-1.21.1-1.1.1.jar` на `botania-neoforge-1.21.1-1.1.2.jar`, `mods/industrialreforged-1.1.2-beta.jar` на `industrialreforged-1.1.3-beta.jar`

# Прошлый релиз: v8.2-wahha.50 — IR 1.1.2-beta и Botania 1.1.1 (пакетная выдача ME-машинам)

- [x] industrialreforged `791e7687…`: ME-машины откатаны к .45 (1024 оп/т, буфер 100M AE, без Applied Flux, без пакетной передачи), пожиратель 4096/т
- [x] accelplus: jar и `config/accelplus-common.toml` перенесены в `removed-from-pack/` профиля Modrinth (вернуть — переложить обратно)
- [x] `build-pack.py --tag v8.2-wahha.49 --out out49`: accelplus нет ни в модах, ни в оверлее; изменились mods-2, mods-d, overlay-config (kubejs-code — только mtime)
- [x] GitHub Release v8.2-wahha.49 (20/20), manifest.json запушен
- [x] Пересборка из исходников: IR `1.1.2-beta` (`627228ec…`, пакет переименован), Botania `1.1.1` (UP-TO-DATE, `853b8a59…`), TC `1.0.6.9` (`0a385c51…`), ThaumicEnergistics `1.0.5.1` (`23baa67d…`), degrinder/eawireless/ejecttweak без изменений
- [x] MODS и профиль Modrinth обновлены теми же jar
- [x] `build-pack.py --tag v8.2-wahha.50 --out out50`: изменились mods-0, -2, -3, -5, -9, -a, -d, overlay-config (правки профиля с 17 окт: ftbchunks, biomeswevegone, iris/asyncparticles timestamps), kubejs-code без изменений
- [ ] Сервер: заменить `mods/industrialreforged-1.1.1-beta.jar` на `791e7687…`, удалить `mods/accelplus-1.0.0.jar` и `config/accelplus-common.toml`; xray там не нужен (клиентский мод), удалить, если лежит
