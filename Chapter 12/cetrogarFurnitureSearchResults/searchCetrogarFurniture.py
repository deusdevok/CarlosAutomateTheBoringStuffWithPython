import requests, sys, bs4, webbrowser

print('Searching on Cetrogar...')

res = requests.get('https://www.cetrogar.com.ar/catalogsearch/result/?q=' + '+'.join(sys.argv[1:]))
res.raise_for_status() # Check if the search worked

soup = bs4.BeautifulSoup(res.text, 'html.parser')

linkElems = soup.select('.product-item-photo')

numOpen = min(4, len(linkElems))

for i in range(numOpen):
	urlToOpen = linkElems[i].get('href')
	print('Opening ' + urlToOpen)
	webbrowser.open(urlToOpen)