import json
import re

f = open('./data/obama_speech.txt')
txt = f.readlines()
print(len(txt))
words = 0
for line in txt:
    words = words + len(line.split())
print(words)
f.close()

def most_spoken_languages(file):
    f = open(file)
    info = f.read()
    data = json.loads(info)
    population_name = []
    for country in data:
        population_name.append((country["population"], country["name"]))
    population_name.sort(reverse=True)
    top_ten = []
    for i in range(10):
        top_ten.append(population_name[i][1])

    f.close()
    return top_ten


print(most_spoken_languages('./data/countries_data.json'))


f = open('./data/email_exchanges_big.txt')
emails = f.readlines()
list_of_emails = []
for line in emails:
    for word in line.split():
        if '@' in word:
            list_of_emails.append(word)

def find_most_common_words(param, count):
    if '.txt' in param:
        f = open(param)
        txt = f.read()
    else:
        txt = param
    txt = re.sub(r'[^\w\s]', '', txt)
    counts = {}
    for word in txt.split():
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    answer = []
    for key, value in counts.items():
        answer.append((value, key))
    answer.sort(reverse='True')
    return answer[:10]

print(find_most_common_words('./data/obama_speech.txt', 10))
print(find_most_common_words('./data/romeo_and_juliet.txt', 10))