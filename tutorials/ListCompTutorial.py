#List comprehension = A concise way to create lists in Python
#                     Compact and easier to read than normal loops
#                     [expression for value in iterable if condition]



#doubles = [x*2 for x in range(1, 11)]
#triples = [y*3 for y in range(1, 11)]
#squares = [z * z for z in range(1,11)]

#print(squares)

#numbers = [1, -2, 3, -4, 5, -6, 8, -7]
#positive_nums = [num for num in numbers if num >= 0]
#negative_nums = [num for num in numbers if num <0]
#odd_nums = [num for num in numbers if num % 2 == 1]
#print(odd_nums)

grades = [85, 80, 34, 56, 62, 30]
abovesixty = [grade for grade in grades if grade >=60]
lessthansixty = [grade for grade in grades if grade <60]

print(f'People who passed: {abovesixty}')
print(f'People who failed: {lessthansixty}')