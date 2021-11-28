#! python3

from pathlib import Path

txtFile = input('Enter the name of the txt file to read: ')

inputFile = open(Path(txtFile))

inputContents = inputFile.read()
inputFile.close()

adjective = input('\nEnter an adjective:\n')
noun = input('Enter a noun:\n')
adverb = input('Enter a adverb:\n')
verb = input('Enter a verb:\n')

outContents = inputContents.replace('ADJECTIVE', adjective)
outContents = outContents.replace('NOUN', noun)
outContents = outContents.replace('ADVERB', adverb)
outContents = outContents.replace('VERB', verb)

outputTxt = input('Enter the name of the output txt file: ')

outFile = open(outputTxt, 'w')
outFile.write(outContents)
outFile.close()