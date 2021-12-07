#! python3
# fillingGaps.py - finds gaps in file names 
# and renames them to fill the gaps

import shutil, os, re

# Set the prefix of the files
prefixPattern = re.compile(r"""^(spam00) # starts with the string 'spam00'
	(.*?)                              # followed by anything
	(.txt)$                            # ends with .txt extension
	""", re.VERBOSE)

firstFile = False

for spamFilename in os.listdir('.'):
	mo = prefixPattern.search(spamFilename)

	if mo == None:
		continue

	firstPart = mo.group(1)
	secondPart = mo.group(2)
	thirdPart = mo.group(3)

	if firstFile:
		number += 1
		if secondPart != str(number):
			newName = firstPart + str(number) + thirdPart

			absWorkingDir = os.path.abspath('.')
			prevName = os.path.join(absWorkingDir, spamFilename)
			newName = os.path.join(absWorkingDir, newName)

			print(f'Renaming "{prevName}" to \n"{newName}"\n\n')
			shutil.move(prevName, newName)
	else:
		firstFile = True
		number = int(secondPart)
