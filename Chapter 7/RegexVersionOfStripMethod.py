import re

def regexStrip(text, chars='\s'):
	stripLeft = re.compile(r'^['+re.escape(chars)+r']+')
	stripRight = re.compile(r'['+re.escape(chars)+r']+$')

	t = re.sub(stripLeft, '', text)
	tFinal = re.sub(stripRight, '', t)

	return tFinal

texts = [
	'    holas   ',
	'   chau   ',
	'---dklasdasd-----',
	'www.example.com'
]

for text in texts:
	chars = ' -cmowz.'

	print('Original string: ', text)
	print('Using strip method: ', text.strip(chars))
	print('Using regex strip: ', regexStrip(text, chars))
	print()

print('All done!')