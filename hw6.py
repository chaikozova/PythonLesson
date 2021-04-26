
dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
new_dict ={}

for key, value in dict.items():
    print(key, ' - ', value)
    new_dict.setdefault(value, key)

print(new_dict)