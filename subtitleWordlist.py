#v0.1 subtitleWordlist.py
#To Do:
#1. Automate process of downloading subtitles from Youtube
#---maybe just have uesr input URL to video, and this will download subs and translate them into a wordlist
#2. Have a combination function for multiple wordlists

#importing modules
import time
import sys
import re
import os

#set the current working directory variable
curdir = os.getcwd()
print curdir

#request a filename to use
transfile = raw_input('Enter the path to your file to translate, or press ENTER to translate files in the RawSubs folder: ')
if transfile == '':
	transfolder = curdir + '\RawSubs'
	for file1 in os.listdir(transfolder):
		file = open(transfolder + '\\' + file1, 'r')

		#TESTING - above runs with print just fine, printing 1.txt, 2.txt, and 3.txt for file1 variable
		#  this should indicate that the issue is in the code below

		# .lower() returns a version with all upper case characters replaced with lower case characters.
		text = file.read().lower()
		file.close()

		#create file and set stdout to point at it
		f = open('TransSubs\subout_' + file1 + '' +time.strftime("%x").replace('/', '.')+'_' +time.strftime("%X").replace(':', '.')+'.txt', "w") 
		sys.stdout = f

		# replaces anything that is not a lowercase letter, a space, or an apostrophe with a space:
		text = re.sub('[^a-z\ \']+', " ", text)
		text = re.sub('\ ', '\n', text)
		text = re.sub('\"', '\'', text)
		words = list(text.split())
		for w in words:
			w = w.lstrip('\'')
			w = w.rstrip(',')
			w = w.rstrip('\'')
			print w

else:
	file = open(transfile, 'r')
	# .lower() returns a version with all upper case characters replaced with lower case characters.
	text = file.read().lower()
	file.close()

	#create file and set stdout to point at it
	f = open('TransSubs\subout' +time.strftime("%x").replace('/', '.')+'_' +time.strftime("%X").replace(':', '.')+'.txt', "w") 
	sys.stdout = f

	# replaces anything that is not a lowercase letter, a space, or an apostrophe with a space:
	text = re.sub('[^a-z\ \']+', " ", text)
	text = re.sub('\ ', '\n', text)
	text = re.sub('\"', '\'', text)
	words = list(text.split())
	for w in words:
		w = w.lstrip('\'')
		w = w.rstrip(',')
		w = w.rstrip('\'')
		print w
