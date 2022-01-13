#! python3
# randomquizgenerator.py - creates quizzes with questions
#and answes in random order, along with the answer key
import random
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quiznum in range(35):
    #make the quiz files and answer keys
    quizfile = open('capitalsquiz%s.txt' %(quiznum + 1),'w')
    answerkey = open('answerkey%s.txt' %(quiznum + 1),'w')

    quizfile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizfile.write((' ' * 20)+ 'State Capital Quiz (Form %s)' %(quiznum + 1))
    quizfile.write('\n\n')

    states = list(capitals.keys())
    random.shuffle(states)
    for questionNum in range(50):
        correctAnswer = capitals[states[questionNum]]
        wrongAnswer = list(capitals.values())
        del wrongAnswer[wrongAnswer.index(correctAnswer)]
        wrongAnswer = random.sample(wrongAnswer,3)
        answeroptions = wrongAnswer + [correctAnswer] #remember, they are a list
        random.shuffle(answeroptions)

        quizfile.write('%s. What is the capital of %s?\n' %(questionNum+1, states[questionNum]))
        for i in range(4):
            quizfile.write('   %s. %s' %('ABCD'[i],answeroptions[i]))
            quizfile.write('\n')
        answerkey.write('%s. %s\n' %(questionNum+1,'ABCD'[answeroptions.index(correctAnswer)]))

quizfile.close()
answerkey.close()
