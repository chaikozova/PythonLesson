
def sum_of_numbers(*args, **kwargs):
    result = 0
    operator = kwargs.get('operator')
    if operator == '+':
        for num in args:
            result += num
    elif operator == '*':
        result = 1
        for num in args:
            result = result * num
    print(result)
    return result


sum_of_numbers(2, 4, 5, 6, 3, operator='+')
sum_of_numbers(2, 4, 5, 6, 3, operator='*')

