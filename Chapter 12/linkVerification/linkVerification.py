#! python3
# linkVerification.py - Downloads every linked page on the page.

import requests, bs4

page = input('Enter the website: ')
res = requests.get(page)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

links = soup.select('a')

for link in links:
	try:
		if link.get('href')[0] == '/':
			linkh = page + link.get('href')
		else:
			linkh = link.get('href')
		print('Checking {}'.format(linkh))
		res = requests.get(linkh)

		if res.status_code == 404:
			print('Status 404 for {}'.format(linkh))

	except:
		pass