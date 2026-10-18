# NEXT.md — v8.2-wahha.51: Botania 1.1.2 и IR 1.1.3-beta из MODS

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
- [x] Пересборка из исходников: IR `1.1.2-beta` (`627228ec…`, пакет `ic3` → `tech`, классы в ic3 не нужны ни конфигам, ни kubejs), Botania `1.1.1` (UP-TO-DATE, `853b8a59…`), TC `1.0.6.9` (`0a385c51…`, без shim `team.luxinfine`/`legacy.gamerforea`), ThaumicEnergistics `1.0.5.1` (`23baa67d…`), degrinder/eawireless/ejecttweak без изменений
- [x] MODS и профиль Modrinth обновлены теми же jar
- [x] `build-pack.py --tag v8.2-wahha.50 --out out50`: изменились mods-0, -2, -3, -5, -9, -a, -d, overlay-config (правки профиля с 17 окт: ftbchunks, biomeswevegone, iris/asyncparticles timestamps), kubejs-code без изменений
- [ ] Сервер: заменить `mods/industrialreforged-1.1.1-beta.jar` на `791e7687…`, удалить `mods/accelplus-1.0.0.jar` и `config/accelplus-common.toml`; xray там не нужен (клиентский мод), удалить, если лежит
