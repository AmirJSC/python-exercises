#! python3
#  backupToZip.py - Copies an entire folder and its contents into
#  a ZIP file whose filename increments

import zipfile, os

def backupToZip(folder):
    #Backup the entire contents of a folder into a zip file

    folder = os.path.abspath(folder)

    #Figure out the filename this code should use based on
    #what files already exist
    number = 1
    while True:
        zipFilename = os.path.basename(folder)+'_'+str(number)+'.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1
    #CREATING THE ZIP file
        print('Creating %s...' %(zipFilename))
        backupZip = zipfile.ZipFile(zipFilename,'w')  #creating a zip

    #Walk the entire folder tree
        for foldername, subfolders, filenames in os.walk(folder):
            print('Adding files in %s...'%(foldername))
            #Add the current folder to ZIP file
            backupZip.write(foldername)
            #Add all files in this folder to the ZIP file
            for filename in filenames:
                if filename.endswith('.zip'):
                    continue
                backupZip.write(os.path.join(foldername, filename))
        backupZip.close()
        print('Done')
