#Python password Checker
#Simple program to check if user inputted string confines with set requirements






#Defines the function that checks the user inputted password
def passwordChecker(password):
    #Checks length
    if len(password) < 8:
         passlength = False
    else:
        passlength = True
        
    print(f'Length of password is at least 8 characters?: {passlength}')
        
    #Checks for any numbers
    passnum = any(char.isdigit() for char in password)
        
        
    print(f'Does password contain any digits?: {passnum}')
    
    #Checks for uppercase characters    
    has_uppercase = any(char.isupper() for char in password)
    print(f'Uppercase Chars?: {has_uppercase}')
    
    #Checks all three values and returns a final value to see if password passed checks
    if passlength and passnum and has_uppercase:
        return True
    else:
        return False

#Defines function that accepts input and prints final password result
def passwordInput():
    passcheck = False
    while passcheck == False:
        password = input('Please enter the password: ')
        passcheck = passwordChecker(password)
        if passcheck:
            print('Password Accepted!')
        else:
            print('Password Denied!')
  


#Calls the function that begins the program
passwordInput()
    
        
    
        