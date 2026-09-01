#Project Number Guesser

##imports the py random module
import random

#defines the variables used
low = 1
high = 50
guesses = 1

##Outer loop controls the restart, inner controls the game itself
while True:
    number = random.randint(low, high)
    while True:
        if guesses > 7:
            print (f'Game over, you ran out of guesses! the number was {number}!!')
            break
        
        print(f'This is guess number: {guesses}')
        guess=int(input(f'Guess a number between: {low} and {high} : '))
        if guess < number:
            print('Too low!')
        
        elif guess > number:
            print('Too high!')  
        
        else:
            print('Well done you win!')
            break
        
        ##iterates the guesses each round to ensure user only gets 7 guesses
        guesses += 1
    
    ##continues the loop and resets counter if user wishes to continue, else breaks the loop
    retry = input('Would you like to play again? (y/n)').lower()
    if retry == 'y':
        guesses = 1
    else:
        break