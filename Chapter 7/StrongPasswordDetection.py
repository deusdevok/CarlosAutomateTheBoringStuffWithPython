import re

moreThanEight = re.compile(r'[\w]{8,}')
lower = re.compile(r'[a-z]')
upper = re.compile(r'[A-Z]')
oneDigit = re.compile(r'[\d]')

def isStrongPass(password):
	mo1 = moreThanEight.search(password)
	mo2 = lower.search(password)
	mo3 = upper.search(password)
	mo4 = oneDigit.search(password)

	return not any(elem is None for elem in [mo1, mo2, mo3, mo4])

passwords = [
	'hola',
	'abCde2afKs',
	'bfoabofibaofb',
	'asdj832rfouasdf',
	'419641934',
	'FNAONFOAFFADFS']

for password in passwords:
	print(isStrongPass(password))