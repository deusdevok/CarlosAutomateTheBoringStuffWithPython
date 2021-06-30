# Rock, Paper, Scissors Game
import sys, random

print('Welcome to Rock, Paper, Scissors Game!\n')

win = 0
loss = 0
tie = 0

while True:
	print(str(win) + ' Wins, ' + str(loss) + ' Losses, ' + str(tie) + ' Ties')
	print('Enter your move: (r)ock | (p)aper | (s)cissors | (q)uit')
	move = input() # Human's move
	if move not in 'rpsq':
		print('Your input is not valid. Please try again.')
		continue
	if move == 'q':
		print('Thank you for playing!')
		sys.exit()

	move_pc = random.randint(1, 3) # Computer's move
	if move_pc == 1:
		move_pc = 'r'
	elif move_pc == 2:
		move_pc = 'p'
	else:
		move_pc = 's'

	if move == 'r':
		if move_pc == 'r':
			tie += 1
			print('Tied. Computer chose rock.')
		elif move_pc == 'p':
			loss += 1
			print('Lose. Computer chose paper.')
		else:
			win += 1
			print('Win. Computer chose scissors.')

	elif move == 'p':
		if move_pc == 'r':
			win += 1
			print('Win. Computer chose rock.')
		elif move_pc == 'p':
			tie += 1
			print('Tied. Computer chose paper.')
		else:
			loss += 1
			print('Lose. Computer chose scissors.')

	else:
		if move_pc == 'r':
			loss += 1
			print('Lose. Computer chose rock.')
		elif move_pc == 'p':
			win += 1
			print('Win. Computer chose paper.')
		else:
			tie += 1
			print('Tied. Computer chose scissors.')

