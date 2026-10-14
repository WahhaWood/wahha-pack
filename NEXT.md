# NEXT.md — деплой thaumcraft 1.0.6.7 (v8.2-wahha.42)

- [x] thaumcraft-1.0.6.7.jar в профиль Modrinth `mods/` (копия из `projects/MODS/`), 1.0.6.5 перенесён в scratchpad.
      В репозитории thaumicreforged 1.0.6.6 и 1.0.6.7 пока не закоммичены (см. `git status` там)
- [x] Пак `build-pack.py --tag v8.2-wahha.42`, 20 архивов, `mods-9.zip` содержит thaumcraft-1.0.6.7.jar
- [x] Залить zip в GitHub Release v8.2-wahha.42 (20/20 ассетов, размеры совпадают)
- [x] manifest.json в репо, commit + push (после релиза)
- В архивах overlay-config, kubejs-code и mods-9 изменились файлы профиля, которые игра пересоздала при запуске
  (конфиги, `.snbt`, `.json`, в том числе `kubejs/config/common.json`). Их не трогал, в сборку ушли как есть.
