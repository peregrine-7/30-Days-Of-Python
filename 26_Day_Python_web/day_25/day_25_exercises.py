import pandas as pd
import numpy as np

nums = [1,2,3,4,5]
s = pd.Series(nums, index = [1,2,3,4,5])
print(s)

dct = {'name':'Asabeneh','country':'Finland','city':'Helsinki'}

s = pd.Series(dct)
print(s)

s = pd.Series(np.linspace(5,20,10))
print(s)

data = [
    ['Asabeneh', 'Finland', 'Helsink'],
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]
df = pd.DataFrame(data, columns = ['Names', 'Country', 'City'])
print(df)

df = pd.read_csv('./data/weight-height.csv')
print(df)
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
heights = df['Height']
print(heights)
weights = df['Weight']
print(len(heights) == len(weights))

print(heights.describe())

print(df.describe())

data = [
    {"Name": "Asabeneh", "Country":"Finland","City":"Helsinki"},
    {"Name": "David", "Country":"UK","City":"London"},
    {"Name": "John", "Country":"Sweden","City":"Stockholm"}]

df = pd.DataFrame(data)

weights = [74, 78, 69]

df['Weight'] = weights
print(df)

heights = [173, 175, 169]
df['Height'] = heights
print(df)
df['Heights'] = df['Height'] * 0.01
print(df)
