##Compound interest Calculator


##Defines the variables
principle = 0
rate = 0
time = 0

##Uses a while loop to for error correction and value errors
while True:
    try:
        principle = float(input('Enter the principle amount: '))
        if principle  <= 0:
            print('Principle cant be less than or equal to 0')
        else:
            break
    except: ValueError
    print('Must be a number!')
    

while True:
    try:
        rate = float(input('Enter the interest rate: '))
        if rate <= 0:
            print('Interest cannot be less than or equal to 0')
        else:
            break
    except: ValueError
    print('Must be a number!')
    

while True:
    try:
        time = int(input('Enter the time in years: '))
        if time <= 0:
            print('Time cannot be less than or equal to zero')
        else:
            break
    except: ValueError
    print('Must be a number!')
    
## Calculates the total   
total = principle * pow((1 + rate / 100), time)

#Prints and displays result to User
print(f'Balance after {time} year/s is equal to: €{total:.2f}')
    