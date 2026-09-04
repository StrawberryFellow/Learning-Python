#Membership operators = used to test wheter a value or variable is found
# in a sequence

#   (string, list, tubple, set, or dictionary)

#           1.in
#           2. not in



#grades = {'Sandy': 'A', 'Squidward': 'B', 'Spongebob': 'C', 'Patrick': 'D'}

#student = input('Enter name of student: ')

#if student in grades:
   # print(f'{student}.s grade is {grades[student]}')
#else:
    #print(f'{student} was not found')
   
   
   

email = 'markdoran2011@gmail.com'

if '@' in email and '.' in email:
    print(f'{email} is a valid email!')
else:
    print('Invalid email..')