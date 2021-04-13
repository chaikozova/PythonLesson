import random

number = random.randint(0, 10)
num = input('Type number from 0 to 10\n')

if number == num:
    print('Congratulations!')
    print(num, number)
else:
    print('Try again!')
    print(num, number)