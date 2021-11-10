#import pyinputplus as pyip
import random, time

numberOfQuestions = 10
correctAnswers = 0
for questionNumber in range(numberOfQuestions):
	# Pick two random numbers:
	num1 = random.randint(0, 9)
	num2 = random.randint(0, 9)

	prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)

	tries = 0
	while tries < 3:
		ans = input(prompt)
		if ans != str(num1*num2):
			print('Incorrect!')
			tries += 1
		else:
			print('Correct!')
			correctAnswers += 1
			break

	if tries == 3:
		print('Out of tries!')
	
	time.sleep(1) # Brief pause to let user see the result.
print('Score: %s / %s' % (correctAnswers, numberOfQuestions))