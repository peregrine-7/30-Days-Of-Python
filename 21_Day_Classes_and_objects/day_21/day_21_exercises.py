class Statistics:
    def __init__ (self, ages):
        self.ages = ages

    def count(self):
        return len(self.ages)

    def sum(self):
        return sum(self.ages)
    
    def min(self):
        return min(self.ages)
    
    def max(self):
        return max(self.ages)
    
    def range(self):
        return sorted(self.ages)[-1] - sorted(self.ages)[0]

    def mean(self):
        return sum(self.ages) / len(self.ages)
    
    def median(self):
        if (len(self.ages) % 2 == 1):
            return sorted(self.ages)[len(self.ages) // 2]
    
    def mode(self):
        freq = {}
        for age in ages:
            if age in freq:
                freq[age] += 1
            else:
                freq[age] = 1

        age = -1
        count = -1
        for key, value in freq.items():
            if (value > count):
                count = value
                age = key
        return (age, count)
        # just return the number, not the count

    def describe(self):
        return f"Count: {self.count()}\nSum: {self.count()}"
    

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)

print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}

print(data.describe())

class PersonAccount:
    def __init__(self, firstname, lastname, incomes, expenses):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expenses = expenses