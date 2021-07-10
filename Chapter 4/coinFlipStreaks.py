import random

numberOfStreaks = 0
for experimentNumber in range(10000):
	# Code that creates a list of 100 'heads' or 'tails' values.
	coins = ''
	for _ in range(100):
		coin = random.randint(0, 1) # 50 % change of getting 0 (H) or 1 (T).
		if coin == 0:
			coins += 'H'
		else:
			coins += 'T'

	# Code that checks if there is a streak of 6 heads or tails in a row.
	for i in range(94):
		if coins[i:i+6] == 'HHHHHH' or coins[i:i+6] == 'TTTTTT':
			numberOfStreaks += 1
			break

# Answer should be close to 80.68 %
# https://www.quora.com/What-is-the-probability-in-percent-of-getting-six-heads-in-a-row-or-six-tails-in-a-row-if-you-flip-a-coin-100-times-this-is-not-a-homework-problem
print('Change of streak: %s%%' % (numberOfStreaks / 100))