# SubtitleWordlist
Does what it says.. feed a subtitle file downloaded from Youtube and this will output a wordlist that does not contain duplicate words, and is arranged to be used with Hashcat or other similar utilities.

USAGE:

Place this python script (wordlist.py) into a directory that contains all subtitle files you would like to translate into a wordlist.  Run wordlist.py and it will output a file called "wordlist.txt".  This currently only works for Linux.

Functionality to be added:

1. Implement cross-platform function for Windows users

2. Create function that will download the subtitle from Youtube for you, so you don't have to feed files to the script.  Have user input URL for video they want translated into wordlist, instead of having to figure out a way to do it, list using an online utility or Chrome extension.
