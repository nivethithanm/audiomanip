### Segment Audio

import subprocess
import os

files = os.listdir('./')

i = 0
for file in files:
	if ('.py' not in file and '.mp3' in file):
		print("Converting " + str(i) + " out of " + str(len(files)))
		i += 1
		name = file.split('.')[0]
		try:
			subprocess.call('ffmpeg -i ' + str(file) + ' -f segment -segment_time 10 ' + str(name) + '%03d.mp3', shell=True)
		except:
			print("An exception occured")
		
print("Conversion Complete")



