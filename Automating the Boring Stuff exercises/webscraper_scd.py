#! python3
#  ScheduledComicDownloader.py (SCD.py) - checks every day to see if there is a new comic
#  uploaded in the website

import os, bs4, requests
os.chdir('C:\\Pythoncode')
os.makedirs('ComicFolder', exist_ok=True)

#Checks whether a new comic is available. If it is available, it will download it.
def ComicCheck(url):
    #This is the name of the imagefile in the directory
    path = os.path.basename(url)

    if path in os.listdir('./ComicFolder'):
        print('There are no new comics available at this time.')
    else:
        res = requests.get(url)
        res.raise_for_status()
        imageFile = open(os.path.join('ComicFolder', path),'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()


def xkcd():
    site = 'https://xkcd.com'
    res = requests.get(site) 
    res.raise_for_status()
    comic = bs4.BeautifulSoup(res.text, 'html.parser')
    comicElem = comic.select('#comic img')

    if comicElem == []:
        print('Could not find comic element at %s.' %(site))
    else:
        url = 'https:' + comicElem[0].get('src')
        ComicCheck(url)


def qwantz():
    site = 'https://qwantz.com/'
    res = requests.get(site)
    res.raise_for_status()
    comic = bs4.BeautifulSoup(res.text, 'html.parser')
    comicElem = comic.select('.comic')

    if comicElem == []:
        print('Could not find comic element at %s.' %(site))
    else:
        url = site + '/'+ comicElem[0].get('src')
        ComicCheck(url)

xkcd()
qwantz()
    

    

