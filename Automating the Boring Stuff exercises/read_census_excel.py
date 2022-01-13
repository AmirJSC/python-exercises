#! python3
#  readCensusExcel.py - tabulates the population and number of county tracts pery county

import openpyxl, os, pprint
os.chdir('C:\\Pythoncode')

print('Opening Workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.active
countyData = {}

#Sample Data Structure
#{CA: {San Francisco:{pop:'0', tract:'0'}, Denver: {pop:'0', tract:'0'}},
#FL: {Pinellas County: {pop:'0', tract:'0'}, Wayne:{pop:'0', tract:'0'}},
#and so on and so forth

for i in range(2, sheet.max_row+1):
    state = sheet['B'+str(i)].value
    county = sheet['C'+str(i)].value
    pop = sheet['D'+str(i)].value

    countyData.setdefault(state, {})
    countyData[state].setdefault(county,{'pop': 0, 'track':0})
    #Count  the number of pop and track
    countyData[state][county]['track'] += 1
    countyData[state][county]['pop'] += int(pop)

    #We will write the date into a pythonscipt so we can just import it

print('Printing results...')
newfile = open('censurdata.py','w')
newfile.write('countyData = ' +pprint.pformat(countyData))
newfile.close()
print('Done')


    
    
                                
 
