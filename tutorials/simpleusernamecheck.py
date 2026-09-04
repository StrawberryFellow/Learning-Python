while True:
    
    username = input('Type your username: ')
    if len(username) > 12:
        print('Your username cannot have more than 12 characters!. Try again!')
        continue
    elif not username.isalpha():
        print('Usernames cannot have spaces or digits. Please try again')
        continue
    else:
        break
        
print(f'Your username is: {username}, thank you!')
    