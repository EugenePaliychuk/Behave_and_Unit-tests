def fibonacci(number):
    if number == 1 or number == 2:
        return 1
    elif number < 0:
        raise ValueError("The input value is incorrect: {}".format(number))
    elif number == 0:
        return 0
    else:
        return fibonacci(number-1) + fibonacci(number-2)