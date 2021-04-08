### MP3 TO WAV MONO

import subprocess
import os

files = os.listdir('./')

i = 0
for file in files:
	if ('.mp3' in file):
		print("Converting " + str(i) + " out of " + str(len(files)))
		i += 1
		name = file.split('.')[0]
		try:
			subprocess.call('ffmpeg -i ' + str(file) + ' -acodec pcm_s16le -ac 1 -ar 44100 ' + str(name) + '.wav', shell=True)
		except:
			print("An exception occured")
		
print("Conversion Complete")

