#! python3
#  countdown.pyw - A simple countdown script

import time, os, subprocess, sys

os.chdir('C:\\Pythoncode')


timeleft = sys.argv[1]
print(sys.argv[1])
while timeleft > 0:
    print(timeleft, end='')
    time.sleep(1)
    timeleft = timeleft-1

subprocess.Popen(['start','Chainsmoker.mp3'],shell=True)
    

    
 
