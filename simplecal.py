## Defines the calculator function
def calculator():
    while True:
    
        ## Begins a loop to error check user to ensure a correct name is used
        while True:
            name = input('Please enter your name: ')
            
            if name.isdigit():
                print('Please enter a valid name...')
            else:
                break
        
        print(f'Hello {name}! Welcome to my calculator!')
        
        ##Another loop begins to error check user so the correct number is entered
        while True:
            try:
                userSelect = int(input('Please enter a number. 1 = Addition, 2 = Subtraction, 3 = Multiplication, 4 = Division: '))
            
                if userSelect not in (1,2,3,4):
                    print (f'{name} The number you entered must be one of the four options, please try again!!')
                    continue
                
                break
            
            except ValueError:
                print(f'{name}, that is not a number.... Try again!')
            
        ##Gets the value for the first number in the sum
        while True:
            try:           
                num1=float(input('Please enter your first number: '))
                break
            except ValueError:
                print(f'{name}, that is not a number.... Try again!')
                
        ##Gets the value for the second number in the sum
        while True:
            try:           
                num2=float(input('Please enter your second number: '))
                break
            except ValueError:
                print(f'{name}, that is not a number.... Try again!')
                
        ##Sees what the user entered and calculates a value based on it
        if userSelect == 1:
            sum1=num1+num2
            print(f'{name}, {num1} + {num2} = {sum1}')
            
        elif userSelect == 2:
            sum1=num1-num2
            print(f'{name}, {num1} - {num2} = {sum1}')
            
        elif userSelect == 3:
            sum1= num1*num2
            print(f'{name}, {num1} x {num2} = {sum1}')
            
        elif userSelect == 4:
            sum1 = num1/num2
            print(f'{name}, {num1} / {num2} = {sum1}')
        
        ##allows user to restart, if not breaks the loop and ends the program
        while True:
            restart =input(f'{name}, would you like to perform another calculation? (y/n): ')
            if restart.lower() not in ('y', 'n'):
                print(f'{name}, please enter a valid input of y or n!!')
            else:   
                break
        if restart.lower() != 'y':
            break
calculator()
print('Bye Bye!')
