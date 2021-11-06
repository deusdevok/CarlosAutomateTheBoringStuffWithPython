import re

def regexStrip(text, chars=' '):
	#subRegex = re.compile(r'^{}+|{}+$'.format(chars, chars))
	text = subRegex.sub(r'^chars|chars$', '', text)0
	return text

texts = [
	'    holas   ',
	'   chau   ',
	'---dklasdasd-----',
	'www.example.com'
]

for text in texts:
	chars = ' -cmowz.'
	if text.strip(chars) != regexStrip(text, chars):
		print('Test failed.')
		print('Original string: ', text)
		print('Using strip method: ', text.strip(chars))
		print('Using regex strip: ', regexStrip(text, chars))
		print()

print('All done!')