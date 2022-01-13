#! python3
#  renamingfiles.py - renames all the files in a folder and give them a suffix.
#  Then, the files will be copied to a new folder

import os, shutil, re
os.chdir('C:\\Pythoncode\\saaample')
def givenfolder(oldfolder, newfolder):
    number = 1
    regex = re.compile(r"""(.*?)     #text  that comes before the suffix
                           (.pdf)    #the extension
                       """, re.VERBOSE)
    for foldername, subfoldername, filenames in os.walk(oldfolder):
        for files in filenames:
            #The regular expression
            mo = regex.search(files)
            #The parts of the initial filename
            beforepart = mo.group(1)
            extension = mo.group(2)
            #New filename
            newfilename = mo.group(1) + str(number) + mo.group(2)
            number = number + 1
            oldpath = os.path.abspath(oldfolder)
            newpath = os.path.abspath(newfolder)
            shutil.copy(os.path.join(oldpath,files),os.path.join(newfolder,newfilename))

givenfolder('Proof of other insurance','lol')
            


