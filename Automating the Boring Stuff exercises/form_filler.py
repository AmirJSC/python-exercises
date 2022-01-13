#! python3
#formFiller.py - Automatically fills in the form

import pyautogui, time

formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand',
 'robocop': 4, 'comments': 'Tell Bob I said hi.'},
 {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4,
 'comments': 'n/a'},
 {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball',
 'robocop': 1, 'comments': 'Please take the puppets out of the break room.'},
 {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money',
 'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'}]

for person in formData: #This is a dictionary inside a list
    time.sleep(5)
    print('Entering the info of %s...' %(person['name']))

    window = pyautogui.getWindowsWithTitle('Generic Form - Google Chrome')
    window[0].activate()

    #Enter the name
    pyautogui.write(['\t', '\t'])
    pyautogui.write(person['name'] +'\t')

    #Enter the Fear(s)
    pyautogui.write(person['fear'] + '\t')

    #Enter the wizard powers
    if person['source'] == 'wand':
        pyautogui.write(['down', 'enter', '\t'], .5)
    elif person['source'] == 'amulet':
        pyautogui.write(['down','down', 'enter', '\t'],.5)
    elif person['source'] == 'crystal ball':
        pyautogui.write(['down','down','down','enter', '\t'],.5)
    elif person['source'] == 'money':
        pyautogui.write(['down','down','down','down','enter', '\t'],.5)

    time.sleep(2)
    #Enter the Rating
    if person['robocop'] == 1:
        pyautogui.write([' ', '\t', '\t'],.5)
    elif person['robocop'] == 2:
        pyautogui.write(['right', '\t', '\t'],.5)
    elif person['robocop'] == 3:
        pyautogui.write(['right','right', '\t', '\t'],.5)
    elif person['robocop'] == 4:
        
        pyautogui.write(['right','right','right', '\t', '\t'],.5)
    elif person['robocop'] == 5:
        pyautogui.write(['right','right','right','right', '\t', '\t'],.5)


    #Enter the comments
    pyautogui.write(person['comments'] + '\t', .1)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.write('\t')
    pyautogui.press('enter')
    
    
    
    

    

    
