# your_age = int(input('Enter your age: '))
# # if (int(your_age) >= 18):
# #     print("You are old enough to drive")
# # else:
# #     print(f'You need {18 - int(your_age)} more years to learn to drive')

# my_age = 18

# if (your_age == my_age):
#     print("we are the same age")
# elif (your_age == my_age + 1):
#     print("You are 1 year older than me")
# elif (your_age == my_age - 1):
#     print("You are 1 year younger than me")
# elif (your_age > my_age):
#     print(f'You are {your_age - my_age} years older than me')
# else:
#     print(f'You are {my_age - your_age} years younder than me')

# score = int(input("Your score: "))

# if (score >= 90):
#     print("A")
# elif (score >= 80):
#     print("B")
# elif (score >= 70):
#     print("C")
# elif (score >= 60):
#     print("D")
# else:
#     print("F")

# fruits = ['banana', 'orange', 'mango', 'lemon']

# new_fruit = input("Enter a fruit: ")

# if (new_fruit not in fruits):
#     fruits.append(new_fruit)
#     print(fruits)
# else:
#     print('That fruit already exist in the list')

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if ('skills' in person):
    print(person['skills'][len(person['skills']) // 2])

if ('skills' in person and 'Python' in person['skills']):
    print("yeah")
else:
    print('nah')