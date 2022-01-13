#! python3
#  imgurdownloader.py - downloads all the photos in a certain category

import os, sys, bs4, requests, pyperclip

os.chdir('C:\\Pythoncode')
os.makedirs('imgurfolder',exist_ok=True) #If folder already exists, it won't raise an exception

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:]) #Remember, the arguments of sys.argv will be stored in a list
else:
    address = pyperclip.paste()

url = 'https://imgur.com/search?q=' + address
print('Downloading the link...')
res = requests.get(url)
res.raise_for_status()
imgurextract = bs4.BeautifulSoup(res.text,'html.parser') #Make it into a beautiful soup object
imgsearch = imgurextract.select('a img') #Observe the HTML, this is the common denominator between the images
#In each of the element in this list, there is a link, I need to get that link

for i in range(len(imgsearch)):
    link = 'https:' + imgsearch[i].get('src')
    print('Downloading link ' +link)
    imageres = requests.get(link)
    imageres.raise_for_status()
    imagefile = open(os.path.join('imgurfolder',os.path.basename(link)),'wb')
    for chunk in imageres.iter_content(100000):
        imagefile.write(chunk)
    imagefile.close()

print('Done')
