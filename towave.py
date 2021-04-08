### Convert to WAV Format

import subprocess
import os

files = os.listdir('./')

i = 0
for file in files:
	if ('.py' not in file):
		print("Converting " + str(i) + " out of " + str(len(files)))
		i += 1
		name = file.split('.')[0]
		try:
			subprocess.call('ffmpeg -i ' + str(file) + ' -f mp3 -af silenceremove=1:0:-50dB ' + str(name) + '.mp3', shell=True)
		except:
			print("An exception occured")
		
print("Conversion Complete")
