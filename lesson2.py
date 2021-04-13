# x = 15
# y = 13
#
# sum = x + y
# print('Result of sum: '+str(sum))
#
# a = int(input('Tape fisrt number: '))
# b = int(input('Tape second number: '))
# sum = a + b
# print('Result = '+str(sum))


list = ['Dima', 'Vanya']
list.append('Next data')
list.append(123)
list.append(False)
list.append(False)
list.remove(123)
for data in list[2:5]:
    print(data)

#print('List:', list)

tuple1 = (123, 'first data', 'second data', 'any data', 123, True)
print('Tuple:')
for i in tuple1:
    print(i)
#print('Tuple:', tuple1)

set_list = {'apple', 'banana', 'bread', 'sugar', 'bread'}
print('Set List:', set_list)

dictionary = {'word': 'слово', 'dictionary': 'словарь'}
print(dictionary)