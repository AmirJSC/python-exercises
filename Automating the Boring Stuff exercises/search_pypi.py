#! python3
#  searchpypi.py - Opens several search results links

import requests, sys, bs4, webbrowser
#First you have to know the format of the URL
print('Searching...')
res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

#Turn it into a bs4 object
soupObject = bs4.BeautifulSoup(res.text,'html.parser')
linkElems = soup.select('.package-snippet')#returns a list
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    #get- will get the attribute's value, ang value ni href kay link
    urltoOpen = 'https://pypi.org'+ linkElems[i].get('href')
    print('Opening',urltoOpen)
    webbrowser.open(urltoOpen)
