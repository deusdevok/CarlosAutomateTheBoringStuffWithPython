#! python3

from pathlib import Path
import re

# Regular expression
# For example:
# Phone number: '(\d\d\d)-(\d\d\d)-(\d\d\d\d)'
# email: '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4})'

userRe = input('Enter your regular expression:\n')
userReComp = re.compile(userRe)

p = Path()
files = list(p.glob('*.txt'))

for file in files:
	myFile = open(file)
	myFileContent = myFile.readlines()
	for line in myFileContent:
		if userReComp.search(line) is not None:
			print(line)