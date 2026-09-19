# Company Maker

#A basic tool to form a company with however many employees you wish.
# A simple excersise I made to help me understand OOP, inheritance, and __init__ better.


# Defines the company class:
class company:
    def __init__(self, name):
        self.name = name
        self.employees = []
        
    # Defines func to add employees
    def add_employee(self, employee):
        self.employees.append(employee)
        
    #defines list of employees
    def list_employees(self):
        return [f'Name = {employee.staff_name}, Position = {employee.position}' for employee in self.employees]
    

# Defines the employee class:
class employee:
    def __init__(self, staff_name, position):
        self.staff_name = staff_name
        self.position = position
        
        

#Asks user for input and then saves it as current company name
company_name = input('What is the name of your company?: ')
my_company = company(company_name)

# Asks how many staff
employee_count = int(input('How many employees?: '))


# Bassed on above user input the for loop will iterate as many times as their is staff
for i in range (employee_count):
    staff_name = input('What is the staff members name?: ')
    position = input('What is their position?: ')
    new_employee = employee(staff_name, position)
    my_company.add_employee(new_employee)
    


#Prints chosen name of company
print (my_company.name)

#Iterates through staff list and prints name along with position
for employee in my_company.list_employees():
    print (employee)
    
    



        
        
        