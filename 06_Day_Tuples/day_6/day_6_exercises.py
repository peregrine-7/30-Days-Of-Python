empty = tuple()
siblings = ('Michael', 'imagniary')
brothers = ('Abe', 'Bacon', 'Chuck')
sisters = ('Ava', 'Beck', 'Clara')
siblings = brothers + sisters
print(len(siblings))
family_members = siblings + ('Mom', 'Dad')
print(family_members)

sibligs, *parents= family_members
print(sibligs)
print(parents)

fruits = ('apple', 'pear')
veggies = ('asparagus', 'broccoli')
products = ('food', 'bone')
food_stuff_tp = fruits + veggies + products
food_stuff_lt = list(food_stuff_tp)
del food_stuff_tp
print(food_stuff_lt)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
