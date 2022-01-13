def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        #The string inside the Exception is the Exception statement
        #The Exception will return an Exception object
        raise Exception('Symbol must be a one character string.')
    if width <= 2:
        raise Exception('Widht must be greater than 2')
    if height <=2:
        raise Exception('Height must be greater than 2')
    print(symbol*width)
    for i in range(height-2):
        print(symbol + (' ' *(width-2)+symbol))
    print(symbol*width)
    


for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
              try: #Let us execute the function
                  boxPrint(sym, w, h)
                  #However, if there is an exception, this code below will
                  #execute
                  #The Exception object will be stored in err
                  #Then it will be changed to a string
              except Exception as err:
                  print('An exception happened: ' + str(err))
                

                  
