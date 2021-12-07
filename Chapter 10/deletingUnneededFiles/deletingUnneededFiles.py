#! python3
# selectiveCopy.py - walks through a folder and copies 
# pdf or jpg files to a new folder.

import shutil, os
from pathlib import Path

cwd = Path.cwd()
folder = cwd / 'folderTreeTest' # Make folder absolute

for foldername, subfolders, filenames in os.walk(folder):
	for filename in filenames:
		if os.path.getsize(Path(foldername) / filename) > 20*1024: # 20 KB = 20*1024 B 
			print()
			print(Path(foldername) / filename)
