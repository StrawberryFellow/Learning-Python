# Python credit card validator program

#1. Remove any '-' or ' '
#2. Add all digits in the odd places from right to left
#3. Double ever second digit from right ot left.
#			(If result is a two-digit number,
#                            add the two digit-number together to get a single digit.)
#4. Sum the total of steps 2 & 3
#5. If sum is divisible by 10, credit card is valid



sum_odd_digits = 0
sum_even_digits = 0
total = 0

credit_num=input('Please enter your credit card number: ')
credit_num = credit_num.replace('-', '')
credit_num = credit_num.replace(' ', '')
credit_num = credit_num[: : -1]
for x in credit_num[::2]:
    sum_odd_digits += int(x)

for x in credit_num[1::2]:
    x = int(x) * 2
    if x >= 10:
        sum_even_digits += ( 1 +(x % 10))
    else:
        sum_even_digits += x
        
        

total = sum_odd_digits + sum_even_digits

if total % 10 == 0:
    print('VALID')
else:
    print('INVALID')
print(credit_num)
