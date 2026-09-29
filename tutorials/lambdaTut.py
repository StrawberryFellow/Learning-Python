#Lambda function = A small anonymous function for a one time use
#They take any num of arguments, but have only 1 expression
#Helps keep the namespace clean and is useful with higher order functions
#		'sort()', 'map()', 'filter()', 'reduce()'
# 		Lambda parameters: expression


double = lambda x: x * 2
add = lambda x, y: x + y

max_value = lambda x, y: x if x > y else y
min_value = lambda x, y: x if x < y else y

full_name = lambda first, last: first + ' ' + last

is_even = lambda x: x % 2  == 0


print(full_name('Joseph', 'Joestar'))
print(is_even(5))
age_check = lambda age: True if age >= 18 else False


print(age_check(12))