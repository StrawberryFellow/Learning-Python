#Expense Tracker
#Simple Expense Tracker that allows user to track various different expenses and saves them within a JSON File.


import json
#Define different Expense Categories

food_expenses = {}

entertainment_expenses = {}

utility_expenses = {}

housing_expenses = {}

        

#Main Menu Display
def main_menu():
    while True:
        print('---------EXPENSE TRACKER----------')
        print('1. Add Expense')
        print('2. Remove Expense')
        print('3. View Expenses ')
        print('4. Exit')
        
        
        mainmenu_choice = input('Select an option: ')
        match mainmenu_choice:
            case 'Add Expense'| '1':
                add_expense()
            
            case 'Remove Expense'| '2':
                remove_expense()
            
            case 'View Expenses'| '3':
                view_expense()
            
            case 'Exit'| '4':
                break

#All expenses together allowing for searching
all_expenses = {
    "Food": food_expenses,
    "Entertainment": entertainment_expenses,
    "Utilities": utility_expenses,
    "Housing": housing_expenses
}


#Function to save expenses to JSON File
def save_expenses():
    with open('expenses.json', 'w') as file:
        json.dump(all_expenses, file, indent=4)



#Function to load expenses to JSON File
def load_expenses():
    try:
        with open('expenses.json', 'r') as file:
            loaded_data = json.load(file)

            food_expenses.update(loaded_data["Food"])
            entertainment_expenses.update(loaded_data["Entertainment"])
            utility_expenses.update(loaded_data["Utilities"])
            housing_expenses.update(loaded_data["Housing"])

    except FileNotFoundError:
        print('No existing expense file found.')
    

#Defines the function for the view expense menu
#Function displays category, lists items in each category, each categories total's and then also the total over all
def view_expense():
    while True:
        global total
        print('-------EXPENSE BREAKDOWN AND TOTALS-----------')
        print('---------FOOD------')
        for food, price in food_expenses.items():
            print(f'{food}: ${price:.2f}')
        print('----------')
        print(f"Total: ${sum(food_expenses.values())}")
        print('--------ENTERTAINMENT------')
        for entertainment, price in entertainment_expenses.items():
            print(f'{entertainment}: ${price:.2f}')
        print('----------')
        print(f"Total: ${sum(entertainment_expenses.values())}")
        print('---------UTILITIES---------')
        #Loops through the category for each item to get cost
        for utilities, price in utility_expenses.items():
            print(f'{utilities}: ${price:.2f}')
        print('----------')
        print(f"Total: ${sum(utility_expenses.values())}")
        print('-------HOUSING--------')
        for housing, price in housing_expenses.items():
            print(f'{housing}: ${price:.2f}')
        print('----------')   
        print(f"Total: ${sum(housing_expenses.values())}")
        
        
        total = 0
        #gets all dictionaries and loops through them one by one and iterates the total cost each loop
        for expense in all_expenses.values():
            total += sum(expense.values())
        print('')
        print('TOTAL EXPENSES : ')
        print(f'Total: ${total:.2f}')
        quit_choice = input('q to quit menu')
        if quit_choice == 'q':
            return
        

#Defines function to remove an expense
def remove_expense():
    while True:
        global total
        print('----------Remove Expense---------')
        print('Current Expenses:')
        print(f'Food: {food_expenses}')
        print(f'Entertainment: {entertainment_expenses}')
        print(f'Utility: {utility_expenses}')
        print(f'Housing: {housing_expenses}')
        print('q to Quit')
        rem_choice = input('Which item do you want to remove? (q to return to menu) : ')
        if rem_choice == 'q':
            return
        found = False
        for expense in all_expenses.values():
            if rem_choice in expense:
                total = total - expense[rem_choice]
                expense.pop(rem_choice)
                found = True
                save_expenses()
                break
        if found == False:
            print('NOT VALID ITEM...')
        

##Function allows modular and easier way to add an expense
def add_new_expense(category):
    label = input('Enter expense name: ')

    try:
        cost = float(input('Enter expense cost: '))
    except ValueError:
        print('Please enter a valid number.')
        return

    if cost <= 0:
        print('Expense must be greater than zero.')
        return

    category[label] = cost
    save_expenses()

#Defines function to add an expense
def add_expense():
    #Displays menu and uses match case for user selection
    while True:
        print('---------Add Expense----------')
        print('1. Food Expenses')
        print('2. Entertainment Expenses')
        print('3. Utility Expenses')
        print('4. Housing Expenses')
        print('5. Quit')
        addmenu_choice = input('Which Type of Expense would you like to add?: ')
        match addmenu_choice:
           case 'Food Expenses'| '1':                  
               add_new_expense(food_expenses)
            
           case 'Entertainment Expenses'| '2':                  
               add_new_expense(entertainment_expenses)
               
           case 'Utility Expenses'| '3':                  
               add_new_expense(utility_expenses)
               
               
           case 'Housing Expenses'| '4':                  
               add_new_expense(housing_expenses)

            
           case 'q'|'5':
                return
                

load_expenses()
main_menu()
            
        