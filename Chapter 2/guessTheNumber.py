import random

print('I am thinking of a number between 1 and 20.')
num = random.randint(1, 20)
guess = -1
tries = 6
for i in range(tries):
	print('Take a guess.', tries - i, 'attempts left.')
	guess = int(input())
	if guess == num:
		break
	elif guess < num:
		print('Your guess is too low.')
	else:
		print('Your guess is too hight.')

if guess == num:
	print('Good job! You guessed the number in', i+1, 'guesses!')
else:
	print('Nice try. The number is', num)