

username = input('Username:')
password = input('Password:')


if username == 'Roza' and password == 'password':
    print('\nWelcome to the web site!')
    age = int(input('How old are you?'))
    if age < 18:
        print('\nYou can not enter this page')
    else:
        print('\nCongratulations!')
else:
    print('\nThere is no such user')