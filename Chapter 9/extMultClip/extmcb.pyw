#! python3
# extmcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe extmcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe extmcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe extmcb.pyw list - Loads all keywords to clipboard.
#        py.exe extmcb.pyw delete <keyword> - Deletes keyword from the shelf.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3:
	# Save clipboard content.
	if sys.argv[1].lower() == 'save':
		mcbShelf[sys.argv[2]] = pyperclip.paste()
	# Delete clipboard content.
	elif sys.argv[1].lower() == 'delete':
		del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
	# List keywords and load content.
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbShelf.keys())))
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])
	elif sys.argv[1].lower() == 'delete': # Delete all keywords
		for k in mcbShelf.keys():
			del mcbShelf[k]

mcbShelf.close()