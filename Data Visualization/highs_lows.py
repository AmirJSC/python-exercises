import csv
import os
from matplotlib import pyplot as plt
from datetime import datetime


os.chdir('C:\\Pythoncode')

#Get dates, high, and low temperatures from file. 
sitka_filename = 'sitka_weather_2014.csv'
sitka_OpenFile = open(sitka_filename)
sitka_reader = csv.reader(sitka_OpenFile)

dates, highs, lows = [], [], []
for row in sitka_reader:
    if sitka_reader.line_num == 1:
        continue
    try:
        high = int(row[1])
        current_date = datetime.strptime(str(row[0]), '%Y-%m-%d')
        low = int(row[3])
    except ValueError:
        print(current_date, 'missing data')
    else:
        highs.append(high)
        dates.append(current_date)
        lows.append(low)

dv_filename = 'death_valley_2014.csv'
dv_OpenFile = open(dv_filename)
dv_reader = csv.reader(dv_OpenFile)

dv_dates, dv_highs, dv_lows = [], [], []
for row in dv_reader:
    if dv_reader.line_num == 1:
        continue
    try:
        high = int(row[1])
        current_date = datetime.strptime(str(row[0]), '%Y-%m-%d')
        low = int(row[3])
    except ValueError:
        print(current_date, 'missing data')
    else:
        dv_highs.append(high)
        dv_dates.append(current_date)
        dv_lows.append(low)


#Plot data
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates,highs, c='red', alpha=0.5) #The alpha controls the transparency. alpha = 0 is completelt transparent
plt.plot(dates, lows, c='blue',alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = .1)

plt.plot(dv_dates,dv_highs, c='green', alpha=0.5) #The alpha controls the transparency. alpha = 0 is completelt transparent
plt.plot(dv_dates, dv_lows, c='yellow',alpha=0.5)
plt.fill_between(dv_dates, dv_highs, dv_lows, facecolor = 'yellow', alpha = .1)



#Format plot
plt.title('Daily high and low temperatures comparison', fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
fig.autofmt_xdate()

plt.show()


