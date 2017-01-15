#importing modules
import time
import sys
import re
import os
from sets import Set

# check your OS for cross-platform functionality
platform = sys.platform

# make an array to add wordlist items to
wordlist = []

if 'linux' in platform:
	files = [f for f in os.listdir('.') if os.path.isfile(f)]
	for f in files:
		if f != 'translate_curdir.py':
			if f != 'translate_curdir_new.py':
				# open input file to read and work with	
				file = open(f, 'r')

				# .lower() returns a version with all upper case characters replaced with lower case characters.
				text = file.read().lower()
				file.close()

				# replaces anything that is not a lowercase letter, a space, or an apostrophe with a space:
				text = re.sub('[^a-z\ \']+', " ", text)
				text = re.sub('\ ', '\n', text)
				text = re.sub('\"', '\'', text)
				words = list(text.split())
				for w in words:
					w = w.lstrip('\'')
					w = w.rstrip(',')
					w = w.rstrip('\'')

				for word in words:
					wordlist.append(word)

else:
	print "this OS is Windows..."

# dedupe the wordlist
dedupedlist = sorted(set(wordlist))

# create file and set stdout to point at it
file = open('wordlist.txt', "w") 
sys.stdout = file

for text in dedupedlist:
	print text
