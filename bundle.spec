# -*- mode: python -*-

block_cipher = None


a = Analysis(['bundle.py'],
             pathex=['D:\\bundle-path'],
             binaries=[],
             datas=[("bundle-category", "bundle-category")],
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
          name='Bundle',
          debug=False,
          strip=False,
          upx=True,
          console=False )
