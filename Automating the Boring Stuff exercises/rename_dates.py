#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format to
#European DD-MM-YYYY

import shutil,os,re
#create a regex that matches files with the American date format

datePattern = re.compile(r"""^(.*?)   #all text before date, ? means nongreedy
                        ((0|1)?\d)-   #one or two digits of the month
                        ((0|1|2|3)?\d)- #the day
                        ((19|20)\d\d) #the year
                        (.*?)$
                        """,re.VERBOSE)

#Look over the files in the working directory that  matches the regex
for amerFilename in os.listdir('.'):
    mo = datePatter.search(amerFilename)
    if mo == None:
        continue #if walay match na pattern sa current file, go to the next file

    beforepart = mo.group(1)
    monthpart = mo.group(2)
    daypart = mo.group(4)
    yearpart = mo.group(6)
    afterpart = mo.group(8)

    #Form the Europena-style format
    euroFilename = beforepart + daypart + '-' +monthpart+ '-'+yearpart+afterpart

    absdir = os.path.abspath('.')
    amerFilename = os.path.join(absdir,amerFilename)
    euroFilename = os.path.join(absdir,euroFilename)
    print('Renaming "%s" to "%s"...' %(amerFilename,euroFilename))
    #shutil.move(amerFilename,euroFilename) #i move niya ang file with a new
    #name
    
