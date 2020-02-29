import bs4 as bs
import urllib.request
source = urllib.request.urlopen('https://www.w3schools.com').read()
soup = bs.BeautifulSoup(source,'lxml')
for link in soup.find_all('a', href=True):
		if('.asp' in link['href']):
			source_next = urllib.request.urlopen('https://www.w3schools.com' + link['href']).read()
			soup_next = bs.BeautifulSoup(source_next,'lxml')
			for paragraph in soup.find_all('p'):
				print(str(paragraph.text))