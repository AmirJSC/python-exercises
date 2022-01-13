#! python3
#  xkcd.py - downloads xkcd comic images

import os, bs4, requests

os.chdir('C:\\Pythoncode')
#If XKCD already exists, it won't make an exception because of exist_ok=True 
os.makedirs('XKCD',exist_ok=True) 

url = 'https://xkcd.com'
#Url of the first comic has # at the end.
while not url.endswith('#'):
    #Downloads the page
    print('Downloading page %s...' %url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    comicElem = soup.select('#comic img')

    if comicElem == []:
        print('Could not find the image.')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
        res = requests.get(comicUrl)
        res.raise_for_status()

        imageFile = open(os.path.join('XKCD',os.path.basename(comicUrl)),'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

        prevLink = soup.select('a[rel="prev"]')[0]
        url = 'https://xkcd.com' + prevLink.get('href')
    
