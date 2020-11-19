import os
import re
import codecs

## フォルダ内にあるテキストファイルの無駄な改行や空白を削除して整えます。

folderPATH ="path/of/folder"

for curDir, dirs, ReadFiles in os.walk(folderPATH):
	for ReadFile in ReadFiles:
		PATH = os.path.join(curDir, ReadFile)
		with codecs.open(PATH, 'r', 'utf-8', 'ignore') as file:
			t = file.read()
		file.close()
		filename = os.path.basename(PATH)
	
		text = "".join([s for s in t.strip().splitlines(True) if s.strip("\r\n").strip()])
			
		with open(PATH , mode='w') as f:
			f.write(text)
		f.close()