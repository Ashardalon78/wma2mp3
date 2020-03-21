import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment
from pydub.utils import mediainfo
from os import walk, listdir, rmdir
import os.path as op
from shutil import copytree


class AudioCollection():
	def __init__(self):
		self.read_files()
	
	def ig_f(self,dir, files):
		return [f for f in files if op.isfile(op.join(dir, f))]
	
	def read_files(self):	
		path = filedialog.askdirectory()
		if not path:
			return
		#path = path + "\\"
		outpath = path + "_mp3"			

		try:
			copytree(path, outpath, ignore=self.ig_f)
		except:
			pass
		
		self.wmalist = []
		
		for root, subdirs, files in walk(path):			
			for name in files:
				if name.endswith(".wma"):			
					self.wmalist.append(op.join(root,name))			
								
		for item in self.wmalist:				
			outname = item.lstrip(path)
			outname = outname.strip(outname.split('.')[-1])
			outname = outpath + outname + 'mp3'			
			
			song = AudioSegment.from_file(item)
			tags = mediainfo(item).get('TAG',None)			
			song.export(outname, format='mp3', tags = tags)
			print(outname)
		
		empty = True
		while empty:
			empty = False
			for root, subdirs, files in walk(outpath):
				for folder in subdirs:
					dirpath = op.join(root, folder)				
					if len(listdir(dirpath)) == 0: 
						rmdir(dirpath)
						empty = True		
			
root = tk.Tk()
root.withdraw()
AC = AudioCollection()
#root.mainloop()
