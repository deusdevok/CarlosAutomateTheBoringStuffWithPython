import random
import logging

logging.disable(logging.CRITICAL)

logging.basicConfig(level=logging.DEBUG, 
	format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

guess = ''
while guess not in ('heads', 'tails'):
	print('Guess the coin toss! Enter heads or tails:')
	guess = input()

toss = random.randint(0, 1) # 0 is tails, 1 is heads
tossToStr = {0: 'tails', 1: 'heads'}
toss = tossToStr[toss]

logging.debug('Value of variable toss is: %s', toss)
logging.debug('Value of variable guess is: %s', guess)

if toss == guess:
	print('You got it!')
else:
	print('Nope! Guess again!')
	guess = input()
	if toss == guess:
		print('You got it!')
	else:
		print('Nope. You are really bad at this game.')