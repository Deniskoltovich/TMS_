# работа с файлами
'''
f = open('file1.txt', 'w')
f.writelines(['hello\n', 'world\n'])
f.writelines(list(map(lambda x: x + '\n', ['hello', 'world'])))

print('hello', file=f)
f.close()
'''

'''
import json

data = None
with open('data.json', 'r') as f:
    data = json.load(f)
    print(data, type(data))

    data.update({
        'first_name': 'John',
        'last_name': 'Wick',
        'movie': 'The Matrix'
    })



with open('data.json', 'w') as f:
    json.dump(data, f)
'''
############################################

# PANDAS

##################################################
import csv

with open("data.csv", 'r') as f:
    data = csv.reader(f, delimiter=',')
    for item in data:
        print(item)
