#! python3
# 2048.py - Plays the game 2048

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

b = webdriver.Firefox() # Open Firefox browser
b.get('https://gabrielecirulli.github.io/2048/') # Navigate to the website of 2048

htmlElem = b.find_element_by_tag_name('html') # The general web page enclosed by <html> </html>

while True:
	try:
		go = b.find_element_by_class_name('game-over')
		break
	except:
		htmlElem.send_keys(Keys.UP)
		htmlElem.send_keys(Keys.RIGHT)
		htmlElem.send_keys(Keys.DOWN)
		htmlElem.send_keys(Keys.LEFT)

print('Game Over !')

# To get the 'text' of a 'FirefoxWebElement' object use .text method:
score = b.find_element_by_class_name('score-container').text

# Use split by line breaks because sometimes there is
# another number (+4), apparently when you pass 2048 points
score = score.split('\n')[0] 

print('Your score is {}'.format(score))

if int(score) >= 2048:
	print('You got to 2048 or more. Congratulations!')
else:
	print("You didn't get 2048. Try again!")