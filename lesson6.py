number_list = [4, 7, 2, 34, 56]
print('lenght = ',len(number_list))

# for i in range(len(number_list)):
#     print(i, '-', number_list[i])

for i in enumerate(number_list):
    print(i)

dict = {'21.04.2021': 1, '20.04.2021': 2, '19.04.2021': 'three'}
dict.setdefault('18.04.2021', 4)
dict.update({'21.04.2021': 6, '20.04.2021': 7, 'two' : 22})
dict.pop('21.04.2021')
dict.popitem()      # удаляет полсденее значение в словаре
print(dict.get('18.04.2021'))


for key, value in dict.items():
    print(key, '-', value)