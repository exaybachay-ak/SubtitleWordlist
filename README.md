# SubtitleWordlist
Does what it says.. feed a subtitle file downloaded from Youtube and this will output a wordlist that does not contain duplicate words, and is arranged to be used with Hashcat or other similar utilities.

USAGE:
Place this python script (curdirWordlists.py) into a directory that contains all subtitle files you would like to translate into wordlists.  Run curdirWordlists.py.  This currently only works for Linux.

Functionality to be added:

1. Add a function to concatenate and deduplicate all wordlists into a singular wordlist output file

2. Implement cross-platform function for Windows users

3. Create function that will download the subtitle from Youtube for you, so you don't have to feed files to the script
  --have user input URL for video they want translated into wordlist
