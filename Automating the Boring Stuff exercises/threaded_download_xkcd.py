#! python3
#  threadedDownloadXkcd.py - Adds a threading

import os, requests, bs4, threading
os.chdir('C:\\Pythoncode')
os.makedirs('xkcd', exist_ok=True) #Will not  raise an exception if xkdc already exists


def downloadXkcd(startComic, endComic):
    for urlNum in range(startComic, endComic):
        print('Downloading https://xkcd.com/%s' %(urlNum))
        res = requests.get('https://xkcd.com/%s' %(urlNum))
        

        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('No comic is found.')
        else:
            comicUrl = 'https:'+comicElem[0].get('src')
            res = requests.get(comicUrl)
            

            imageFile = open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')

            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

#Add the threading
downloadedThreads = [] #Will keep track of the threads
for i in range(0,140,10):
    start = i
    end = i + 9
    if start == 0:
        start = 1
    downloadThreads = threading.Thread(target=downloadXkcd,args=(start, end))
    downloadedThreads.append(downloadThreads)
    downloadThreads.start()

for downloadThreads in downloadedThreads:
    downloadThreads.join()
print('Done.')
