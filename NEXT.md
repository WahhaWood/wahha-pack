# NEXT.md — v8.2-wahha.49: откат ME-машин, accelplus убран

- [x] industrialreforged `791e7687…`: ME-машины откатаны к .45 (1024 оп/т, буфер 100M AE, без Applied Flux, без пакетной передачи), пожиратель 4096/т
- [x] accelplus: jar и `config/accelplus-common.toml` перенесены в `removed-from-pack/` профиля Modrinth (вернуть — переложить обратно)
- [x] `build-pack.py --tag v8.2-wahha.49 --out out49`: accelplus нет ни в модах, ни в оверлее; изменились mods-2, mods-d, overlay-config (kubejs-code — только mtime)
- [x] GitHub Release v8.2-wahha.49 (20/20), manifest.json запушен
- [ ] Сервер: заменить `mods/industrialreforged-1.1.1-beta.jar` на `791e7687…`, удалить `mods/accelplus-1.0.0.jar` и `config/accelplus-common.toml`; xray там не нужен (клиентский мод), удалить, если лежит
