#! python3
import logging


#logging.disable(logging.DEBUG)
#It is better to use logging than print
#It prevents from accidentally removing print functions
#that are supposed to be there. 
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
logging.debug('start of the program')

def factorial(n):
    logging.debug('Start of factorial(%s)' %(n))
    total = 1
    for i in range(n):
        total = total * (i+1)
        logging.debug('i is ' +str(i) +', total is ' + str(total))
    logging.debug('End of factorial(%s)' % (n))
    return total

print(factorial(5))
logging.debug('End of the entire program')

