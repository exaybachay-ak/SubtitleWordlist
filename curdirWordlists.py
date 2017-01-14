#v0.2 curdirWordlists.py
#To Do:
#1. Automate process of downloading subtitles from Youtube
#---maybe just have uesr input URL to video, and this will download subs and translate them into a wordlist
#2. Have a combination function for multiple wordlists
#3. Complete cross-platform functionality for Windows. Currently only functions properly in Linux

#importing modules
import time
import sys
import re
import os
from sets import Set

#check your OS for cross-platform functionality
platform = sys.platform

if 'linux' in platform:
	files = [f for f in os.listdir('.') if os.path.isfile(f)]
	for f in files:
		if f != 'curdirWordlists.py':
			print f
			# open file for reading words
			file = open(f, 'r')

			# .lower() returns a version with all upper case characters replaced with lower case characters.
			text = file.read().lower()
			file.close()

			#create file and set stdout to point at it
			file = open('Translated_' + f + '' +time.strftime("%x").replace('/', '.')+'_' +time.strftime("%X").replace(':', '.')+'.txt', "w") 
			sys.stdout = file

			# replaces anything that is not a lowercase letter, a space, or an apostrophe with a space:
			text = re.sub('[^a-z\ \']+', " ", text)
			text = re.sub('\ ', '\n', text)
			text = re.sub('\"', '\'', text)
			words = list(text.split())
			for w in words:
				w = w.lstrip('\'')
				w = w.rstrip(',')
				w = w.rstrip('\'')

else:
	print "this OS is Windows..."

cleanlist = Set(words)
for i in cleanlist:
	print i
