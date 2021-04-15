def function(num):
    # num = int(input('Type a number\n'))
    print(num)
    if num > 0:
        print('the number is greater than 0')
    elif num < 0:
        print('The number is less than 0')
    else:
        print('The number is equal to 0')


for i in range(6):
    function(i)

i = 1
while i <= 3:
    print(i)
    i += 1

for i in range(3):
    print(i)
