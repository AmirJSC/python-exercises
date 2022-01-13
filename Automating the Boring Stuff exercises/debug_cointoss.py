# python3
import random, logging

logging.basicConfig(level=logging.DEBUG, format=''' %(asctime)s - %(levelname)s
- %(message)s''')

guess = ' '
logging.debug('The value of guess is ' +guess)
while guess not in ('heads','tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    
def tossf():
    toss = random.randint(0,1) # 0 is tails, 1 is heads
    if toss == 0:
        toss = 'heads'
    else:
        toss = 'tails'
    return toss

value =  tossf()
logging.debug('Value is: ' +str(value))


for i in range(1):
    if value == guess:
        print('You got it!')
        break
    else:
        print('Nope Guess again!')
        value = tossf()
        logging.debug('Value is: ' +str(value))
        guess = input()
        if value == guess:
            print('You got it!')
        else:
            print('Nope. You are really bad at this game.')
            
