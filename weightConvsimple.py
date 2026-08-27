#Python Weight converter

while True:
    weight = float(input('Enter your weight: '))
    
    ##Checks for weight selection and error checks user
    while True:
        unit = input('Kilograms or Pounds? (K or L): ')
        if unit.lower() == 'k':
            weight = weight  *  2.205
            print (f'The converted weight is : {weight} Pounds')
            break
        elif unit.lower() == 'l':
            weight = weight / 2.205
            print (f'The converted weight is : {weight} KG')
            break
        else: unit.lower() not in ('l', 'k')
        print ('That is not a valid Selection, try again!')
    
    ##Asks user to repeat, if not exits the program
    repeat = int(input('Would you like to go again? (1 to repeat, 2 to exit): '))
    if repeat == 1:
        continue
    else:
        break