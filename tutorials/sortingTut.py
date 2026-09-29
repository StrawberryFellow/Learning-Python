#SORTING IN PYTHON .sort() or sorted()
#Lists[], Tuples(), Dictionaries { '':''}, Objects



# -------------LISTS------------------------

#fruits = [3,1,5,2,7,4]

#fruits.sort(reverse = True)

#print(fruits)


#------TUPLES-----------------

#fruits = ('banana', 'orange', 'apple', 'coconut')


#fruits = tuple(sorted(fruits))
#fruits = tuple(sorted(fruits, reverse = True))


#print(fruits)

#--------Dictionaries-------------

#fruits = {'banana' : 105,
# 		'orange' : 73,
#                    'apple': 72,
#                    'coconut': 354}


#fruits = dict(sorted(fruits.items()))
#fruits = dict(sorted(fruits.items(), key=lambda item: item[0], reverse = True))
#fruits = dict(sorted(fruits.items(), key=lambda item: item[1]))
#fruits = dict(sorted(fruits.items(), key=lambda item: item[1], reverse = True))


#print(fruits)



#--------------OBJECTS---------------

class Fruit:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories
        
    def __repr__(self):
        return f'{self.name}: {self.calories}'
    
fruits = [Fruit('banana', 105),
                Fruit('apple', 72),
                Fruit('orange', 73),
                Fruit('coconut', 354)]


fruits = sorted(fruits, key=lambda fruit: fruit.calories)

print (fruits)
