# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(it_companies))
it_companies.add('Twitter')
it_companies.update(['Salesforce', "Mongo"])
it_companies.pop()
print(it_companies)


print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(B.union(A))
print(A.symmetric_difference(B))
del A
del B

print(len(age), len(set(age)))
statement = " am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence?"
print(len(set(statement.split(' '))))




