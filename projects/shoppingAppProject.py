#Simple Cart and Total Project



##Defines cart and total variables
cart = []
total = 0

# Defines the various menus

cleaning_menu = {'Brush': 5.00,
                'Mop': 6.00,
                'Bucket': 3.00,
                'Soap': 2.00}


techno_menu = {'Computer': 115.00,
                'CPU': 16.00,
                'Fan': 3.00,
                'Mouse': 32.00}

furniture_menu = {'Sofa': 135.00,
                'Chair': 46.00,
                'Desk': 33.00,
                'Table': 42.00}

groceries_menu = {'Chicken': 5.00,
                'Carrot': 2.00,
                'Potato': 3.00,
                'Soup': 4.00}

# A list containing all menus that allows searching
all_menus = [cleaning_menu, techno_menu, furniture_menu, groceries_menu]



#Function to remove items from the cart
def remove_items():
    while True:
        global total
        print(f'Cart: {cart}')
        print(f'Total: £{total:.2f}')
        rem_choice = input('Which item do you want to remove? (q to return to menu) : ')
        if rem_choice == 'q':
            return
        found = False
        for menu in all_menus:
            if menu.get(rem_choice) is not None:
                total = total - menu[rem_choice]
                cart.remove(rem_choice)
                found = True
                break
        if found == False:
            print('NOT VALID ITEM...')
                
                


#function to print whatever menu is chosen
def print_menu(menu):
    for key, value in menu.items():
        print(f'{key:10}: £{value:.2f}')


#function for the sub menu system
def menu_choice(menu, choice_name):
    global total
    while True:
        print('------------------------------')
        print(f'Welcome to the {choice_name} menu.')
        print('----------------------------------')
        print_menu(menu)
        choice = input('Select an item (q to quit): ')
        if choice == 'q':
            return
        elif menu.get(choice) is not None:
            cart.append(choice)
            total = total + menu[choice]
        elif menu.get(choice) is None:
            print('NOT VALID ITEM...')

#function for the intial main menu and displays options
def main_menu():
    while True:
        print('---------MENU----------')
        print('1. Groceries')
        print('2. Furniture')
        print('3. Technology')
        print('4. Cleaning')
        print('--------------------------')
        print(f'Your cart: {cart}')
        print(f'Total is: £{total:.2f}')
        print('To remove an item: f')
        print(f'To checkout and exit: q')
        
        ##Input so user can choose which menu to view
        choice = input('Please say the name or number of which department you would like to visit: ')
        match choice:
            case 'Groceries'| '1':
                menu_choice(groceries_menu, 'Groceries')
            
            case 'Furniture' | '2':
                menu_choice(furniture_menu, 'Furniture')
            
            case 'Technology' | '3':
                menu_choice(techno_menu, 'Technology')
            
            case 'Cleaning' | '4':
                menu_choice(cleaning_menu, 'Cleaning')
            
            case 'q':
                print(f'Cart: {cart}, Total: £{total:.2f}. Thank you for shopping, bye!')
                break
            
            case 'f':
                remove_items()
                
                    


#Starts the progam by calling the main menu
main_menu()