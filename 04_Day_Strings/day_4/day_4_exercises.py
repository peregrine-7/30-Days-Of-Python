temp1 = 'Thirty ' + 'Days ' + 'of ' + 'Python'
print(temp1)
print(len(temp1))
print(temp1.upper())
print(temp1.lower())
print(temp1.swapcase())

test2 = 'hi'
print(test2.capitalize())
test3 = 'hIdfjIuehfSDFKjhII823795'
print(test3.title())

print(temp1[:6])
print('Coding' in 'Coding for All')

string = 'Python for Everyone'
print(string.replace('Everyone', 'All'))

string = 'Coding for All'
s1, s2, s3 = string.split(' ')
print(s1 + ' lol ' + s2 + ' lol ' + s3)

string = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(string.split(','))

string1 = 'Python for Everyone'
string2 = 'Coding For All'
print(string2.find('C'))
print(string2.find('F'))
print(string2.rfind('l'))
print(len(string2) - 1)
string3 = 'You cannot end a sentence with because because because is a conjunction'
print(string3.index('because'))
print(string3.rindex('because'))
print(string3[0:31] + string3[54:])

print(string2.startswith('Coding'))
print(string2.startswith('coding'))

string = '   Coding For All      ' 
print(string.strip())
print(string1.isidentifier())
print('3'.isidentifier())
libs = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('!'.join(libs))

sentences = '''I am enjoying this challenge.
I just wonder what is next.'''
print(sentences.splitlines())

print('Name\t\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')

r = 10
print(f'radius = {r}\narea = 3.14 * radius ** 2\nThe area of a circle with radius {r} is {int(r**2*3.14)} meters square')