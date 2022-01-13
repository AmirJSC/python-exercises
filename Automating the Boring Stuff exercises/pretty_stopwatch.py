#! python3
#  Prettystopwatch.py - A prettified stopwatch

import time, os
os.chdir('C:\\Pythoncode')


input()
startTime = time.time()
lastTime = startTime
lapNum = 1

try:
    while True:
        input()
        totalTime = round(time.time() - startTime, 2)
        lapTime = round(time.time() - lastTime, 2)
        print('Lap #' +(str(lapNum)+':').ljust(3,' ')+ str(totalTime).rjust(6, ' ') + str(lapTime).rjust(6, ' '), end='')
        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:
    print('\nDone')
