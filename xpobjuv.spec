# -*- mode: python -*-

block_cipher = None


a = Analysis(['ff777wingflex.py'],
             pathex=['/Users/apple/code/xpobjuv'],
             binaries=[],
             datas=[('main.ui','.'),
             ('xpobjuv.cfg','.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='xpobjuv',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='777.ico')
app = BUNDLE(exe,
             a.datas, 
             name='xpobjuv.app',
             icon='777.icns')
