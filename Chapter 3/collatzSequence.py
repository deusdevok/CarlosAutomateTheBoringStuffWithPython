def collatz(number):	
	number = int(number)
	if number % 2 == 0: # Even
		print(number // 2)
		return number // 2
	else:               # Odd
		print(3 * number + 1)
		return 3 * number + 1

print('Enter an integer number:')
n = input()
while True:
	try:
		n = collatz(n)
		if n == 1:
			print('See you next time!')
			break
	except:
		print('Your input number is not an integer. Try again.')
		break
