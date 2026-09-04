#args = allows you to pass multiple non-key arguements
#kwargs = allows you to pass multiple keyword-arguements

#def display_name(*args):
    #for arg in args:
       # print(arg, end = ' ')
        

#display_name('Joe', 'Mower')
       
       


#def print_address(**kwargs):
    #for key, value in kwargs.items():
        #print(f'{key}: {value}')

#print_address(street = '123 major street', city = 'Dublin', eircode = 'd08ype9')
        


def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end = ' ')
    print()
    
    if 'apt' in kwargs :
        print(f'{kwargs.get("street")} {kwargs.get('apt')}')
    
    elif 'pobox' in kwargs:
        print(f'{kwargs.get('pobox')}')
        print(f'{kwargs.get("street")}')

    
    else:
        print(f'{kwargs.get("street")}')
    print(f'{kwargs.get('city')} {kwargs.get('country')}, {kwargs.get('eircode')}')
shipping_label('Dr', 'Joe', 'Mower', 'II',
               street = '124 real st.',
               city = 'dublin',
               pobox = '233',
               country = 'ireland',
               eircode = 'd08ti99')