dog = {}
dog = {'name':'fluff', 'color':'black', 'breed':'rottweiler'}

student = {
    'first_name':'Chris',
    'last_name':'Lu',
    'gender':"F",
    'skills': ['python', 'C', 'C++']
}

print(len(student))
print(type(student['skills']))
student['skills'].append('SML')
print(student.keys())
print(student.values())
print(student.items())

del student['first_name']
del dog

print(student)
