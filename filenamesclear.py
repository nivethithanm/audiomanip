### CLEAN FILE NAMES IN A DIRECTORY

import os
import pathlib

path = pathlib.Path.cwd()

files = os.listdir('./')

for index, file in enumerate(files):
	ext = file.split('.')[-1]
	filename = file.strip().replace(' ', '').replace('.','').replace('\'','').replace('-','').replace('(','').replace(')','').replace('{','').replace('}','').replace('[','').replace(']','')
	os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(filename), str('.'+ str(ext))])))
