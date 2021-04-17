
# def stepen():
#     for a in range(20):
#         print(2**a)
#
#
# stepen()
import random

def randomList(list):
    for i in range(10):
        number = random.randint(0, 1000)
        list.append(number)
    list.sort()
    return list


numbers = []
randomList(numbers)
print(numbers)