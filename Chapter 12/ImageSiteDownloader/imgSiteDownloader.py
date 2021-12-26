#! python3
# imgSiteDownloader.py - Downloads every photo from flickr given a search query

import requests, bs4, time, os
from selenium import webdriver

def downloadPhotos(searchText, n):
	os.makedirs('images', exist_ok=True) # Store images in ./images
	print('Searching for {} images of {}...\n'.format(n, searchText))
	browser = webdriver.Firefox() # Open Firefox browser
	browser.get('https://www.flickr.com/search/?text=' + searchText)
	time.sleep(5) # Wait some time for the page to load all images
	html = browser.page_source
	soup = bs4.BeautifulSoup(html, 'lxml')

	print('Opening ' + 'https://www.flickr.com/search/?text=' + searchText)

	linkElems = soup.select('.overlay')

	for i in range(min(len(linkElems), n)):
		urlToOpen = 'https://www.flickr.com' + linkElems[i].get('href')
		print('\nOpening ' + urlToOpen)

		res = requests.get(urlToOpen)
		res.raise_for_status()
		soup = bs4.BeautifulSoup(res.text, 'lxml')
		elem = soup.select('.main-photo')

		imgSrc = 'https:'+elem[0].get('src')

		print('Downloading ' + imgSrc)

		res = requests.get(imgSrc)
		res.raise_for_status()

		# Save image
		imageFile = open(os.path.join('images', os.path.basename(imgSrc)), 'wb')
		for chunk in res.iter_content(100000):
			imageFile.write(chunk)
		imageFile.close()

downloadPhotos('gatos', 3)
