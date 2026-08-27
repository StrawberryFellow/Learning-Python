creditnum= '2332-4567-4321-3214'

##reverses the order
creditnum1 = creditnum[::-1]
print(f'Reversed order is: {creditnum1}')

##indexes last four digits
creditnum2 = creditnum [-4:]
print (f'Last four digits is {creditnum2}')

##gets first four digits
creditnum3 = creditnum[0:4]
print(f'First four digits is {creditnum3}')


##Testing splicing by seperating domain and email
email = input('Enter your email: ')


## Uses the index point to check everything in the string before, and after
username = email[:email.index('@')]
domain = email[email.index('@') + 1:]

print(f'Your username is: {username} and your domain is {domain}')