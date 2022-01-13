#! python3
# Import modules and write comments to describe this program
#Go through every folder in the hard drive and finds these photo folders
#Photo folders -more than half are png or jpg, Photos' width and height should be greater than 500

import os
from PIL import Image
for foldername, subfolders, filenames in os.walk('C:\\'):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        if not (filename.endswith('.jpg') or filename.endswith('.png')):
            numNonPhotoFiles += 1
            continue
        else:
            #Erros will arise where it says File not found so do Try and Except
            try:
                Im = Image.open(os.path.join(foldername, filename))
                width, height = Im.size
                if width and height > 500:
                    numPhotoFiles += 1
                else:
                    numNonPhotoFiles += 1
            except OSError: #for Files not found
                numNonPhotoFiles += 1
            except ValueError:
                numNonPhotoFiles += 1
                
                

    if numPhotoFiles > numNonPhotoFiles:
        print(foldername)
        

        
        
    
