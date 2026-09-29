# zip() = Combines multiple iterables (lists, tuples, sets, dict)
#			Into a single iterator.
#			Makes managing multiple indices easier


names = ['Spongebob', 'Patrick', 'Squidward']
ages = [30, 35, 50]
jobs = ['Cook', 'Unemployed', 'Cashier']

data = zip(names, ages, jobs)

for name, age, job in data:
    print(f'{name} is a  {age} year old {job}')