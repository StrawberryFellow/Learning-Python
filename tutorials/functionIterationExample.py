def get_shippingLabel(country, address, name):
    return f'{country} - {address} - {name}'

print('Welcome to the shipping label maker!')

while True:
    country = input('Which country is the package going to?: ')
    address = input ('Please type the address: ')
    name = input('The name of the reciever?: ')

    print(get_shippingLabel(country, address, name))
    
    if not input('Do you need another? (y = yes, n = no) ').lower()=='y':
        break
    

print('Bye bye!')