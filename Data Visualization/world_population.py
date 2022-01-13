#! python3
#  worldpop.py - gets the country codes and population for the 2010 year

#We are dealing with a JSON file
import json, os
from country_codes1 import get_country_code

os.chdir('C:\\Pythoncode')

filename = 'population_data.json'
openfile = open(filename)
py_data = json.load(openfile)

#py_dict is a list, with each element being a dictionary

for py_dict in py_data:
    if py_dict['Year'] == '2010':
        country_name = py_dict['Country Name']
        population = int(float(py_dict['Value']))
        code = get_country_code(country_name)
        if code:
            print(code + ': ' + country_name + ' ' + str(population))
        else:
            print('ERROR: ' + country_name)
            
