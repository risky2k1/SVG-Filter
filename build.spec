# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_submodules, collect_data_files

hiddenimports = collect_submodules('PySide6')
datas = collect_data_files('PySide6')

datas += [
    ('assets/icon.png', 'assets'),
    ('assets/preview.svg', 'assets'),
]

a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='SVGFilterStudio',
    windowed=True,
    icon='assets/icon.png',
)
