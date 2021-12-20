#! python3
# cmdEmail.py - Sends an email to a specific account
# cmdEmail someaccount@gmail.com subject textmsg

import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

if len(sys.argv) > 3:
	# Get email, subject and text from command line.
	email = sys.argv[1]
	subject = sys.argv[2]
	text = sys.argv[3]
	print(email, subject, text)
else:
	print("You haven't provided some info.")
	print("Example usage:")
	print("cmdEmail someaccount@gmail.com subject textmsg")
	sys.exit()

browser = webdriver.Firefox()
browser.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

# Enter email
emailElem = browser.find_element_by_id('identifierId')
emailElem.send_keys('myemail@gmail.com')
emailElem.send_keys(Keys.ENTER)

time.sleep(4)

# Enter password
passElem = browser.find_element_by_name('password')
passElem.send_keys('mypassword')

time.sleep(6)

# Click on "Redactar"
redactarBtn = browser.find_element_by_class_name('z0')
redactarBtn.click()

# Fill recepient email
emailBox = browser.find_element_by_id(':tc')
emailBox.send_keys(email)

# Fill subject
subjectBox = browser.find_element_by_id(':su')
subjectBox.send_keys(subject)

# Fill text body
textBox = browser.find_element_by_id(':u0')
textBox.send_keys(text)

textBox.submit()
