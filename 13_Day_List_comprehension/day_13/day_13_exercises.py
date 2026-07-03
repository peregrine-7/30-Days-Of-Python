numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

print([i for i in numbers if i <= 0])

print([(i, 1, i, i **2, i **3, i **4, i **5) for i in range(11)])

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
print([[entry[0][0].upper(), entry[0][0][:3].upper(), entry[0][1].upper()] for entry in countries])

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

print([a + ' ' + b for [(a,b)] in names])

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print([list_of_lists[i //3][i % 3] for i in range (9)])