
## Counter for how many times to run the program
counter = int(input("How many boxers do you need to enter?: "))

flyWeight = 0
bantamWeight = 0
featherWeight = 0
lightWeight = 0
welterWeight = 0
middleWeight = 0
lightHeavyweight = 0
heavyWeight = 0
    
while (counter >=1):
    while True:
        name = input("What is the boxer's name?: ")
    
        if name.isdigit():
            print('Please enter a valid name...')
        else:
            break
    
    while True:
        weightType = input("Is the weight in kg or pounds?").lower()
    
        if weightType.isdigit():
            print('Please enter valid weight type..')
        else:
            break
    
    while True:
        try:
            weight1 = int(input("Enter weight of boxer: "))
            break
        except ValueError:
            print('That is not a valid weight, try again..')
            
    if (weightType =="kg"):
        weight1 = weight1  * 2.20462262
            
            ##Finds the weight for Flyweight
    if weight1 <= 112:
        flyWeight += 1
        print(f"Your boxing class is Flyweight. {name} ({weight1:.2f} pounds)")

    elif weight1 <= 118:
        bantamWeight += 1
        print(f"Your boxing class is Bantamweight. {name} ({weight1:.2f} pounds)")

    elif weight1 <= 126:
        featherWeight += 1
        print(f"Your boxing class is Featherweight. {name} ({weight1:.2f} pounds)")

    elif weight1 <= 135:
        lightWeight += 1
        print(f"Your boxing class is Lightweight. {name} ({weight1:.2f} pounds)")

    elif weight1 <= 147:
        welterWeight += 1
        print(f"Your boxing class is Welterweight. {name} ({weight1:.2f} pounds)")

    elif weight1 <= 160:
        middleWeight += 1
        print(f"Your boxing class is Middleweight. {name} ({weight1:.2f} pounds)")

    elif weight1 <= 175:
        lightHeavyweight += 1
        print(f"Your boxing class is Light Heavyweight. {name} ({weight1:.2f} pounds)")

    else:
        heavyWeight += 1
        print(f"Your boxing class is Heavyweight. {name} ({weight1:.2f} pounds)")

    counter -= 1
            
        
