# list_num = [2, 7, 34, 9, 43, 16, 23, 23, 21]
#
# for temp in list_num:
#     if 15 < temp < 24:
#         print(temp)
#     else:
#         print('not correct temperature')


is_winter = input('Is it winter now?\n')
visa = input('Do you have visa?\n')
ticket = int(input('How many tickets do you have?\n'))

if is_winter == 'True' and visa == 'yes':
    if ticket > 0:
        print('Have a nice trip')

elif is_winter == 'False' and visa == 'yes':
    if ticket < 1:
        print('Ok, buy ticket you can travel')
else:
    print('You cannot travel')


# if is_winter == 'True':
#     visa = input('Do you have visa?\n')
#     if visa == 'Yes':
#         ticket = int(input('How many tickets do you have?\n'))
#         if ticket > 0:
#             print('You can travel')
#         else:
#             print('You have to buy some tickets')
#     else:
#         print('You have to get one')
# else:
#     print('Then stay home')

