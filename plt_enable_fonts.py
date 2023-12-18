import matplotlib
import matplotlib.font_manager as fm

"""
fonts = [f.name for f in fm.fontManager.ttflist]
for font in fonts:
	print(font)
"""
# 設定ファイルの場所
print(matplotlib.matplotlib_fname())

# キャッシュ削除
fm._rebuild()

