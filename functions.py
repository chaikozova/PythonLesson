def func(x):
    y = x * 2
    return y


print(func(5))
print(func(2))
print(func(3))


def hello(name):
    # print('Hello, '+name)
    return 'Hello, ' + str(name)


print(hello('Jama'))
print(hello('Harry'))
print(hello('123'))


def sum_of_number(x1, x2, x3=7):
    return x1 + x2 + x3


sum = sum_of_number(1, 2, 3)
print('Sum of three numbers = ' + str(sum))


def sum(*args):
    result = 0

    for i in args:
        result += i
    return result


print(sum(1, 2, 3))
print(sum(1, 2, 3, 4, 5, 6))
print(sum(1, 2, 3, 4, 5, 6, 7, 8))
print(sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
