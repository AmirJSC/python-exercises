#! python3
#Reads a text file
#Replaces the word ADJECTIVE, NOUN, ADVERB, or VERB
#whenever it appears in the text with whatever word they want
import re

dict_word = {'ADJECTIVE':'','NOUN':'','ADVERB':'','VERB':''}

sampletext = open('C:\\Pythoncode\\testing.txt')
sampleread = sampletext.read()
sampletext.close()
samplefile = open('samplefile.txt','w')

regex1 = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
rlist = regex1.findall(sampleread)
wlist = []
z = 0
for i in rlist:
    print('What is the ' +i+ '?')
    wlist.append(input())
    regex2 = re.compile(i)
    #The 1 means that it is nongreedy sub.
    sampleread = regex2.sub(wlist[z],sampleread,1) 
    z = z + 1
    print(sampleread)

print(sampleread)
samplefile.write(sampleread)
samplefile.close()

    
    
    




    
    

