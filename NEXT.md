# NEXT.md — деплой thaumcraft 1.0.6.5 (v8.2-wahha.41)

- [x] thaumcraft-1.0.6.5.jar в профиль Modrinth `mods/` (sha256 cbdecb…), 1.0.6.3 удалён. Jar совпадает с `core/build/libs`
- [x] Пак `build-pack.py --tag v8.2-wahha.41`, 20 архивов, jar внутри mods-9.zip сверен по sha256
- [x] Залить zip в GitHub Release v8.2-wahha.41 (20/20 ассетов)
- [x] manifest.json в репо, commit + push; `wahhawood.github.io/wahha-pack/manifest.json` отдаёт v8.2-wahha.41
- В архивах overlay-config и kubejs-code изменились 215 файлов профиля, которые мод пересоздал при запуске игры
  (конфиги, `.snbt`, `.json`). Их не трогал, в сборку ушли как есть.
