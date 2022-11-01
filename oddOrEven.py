def checker(num):
    if num % 2 == 0:
        return 'Your number is even!'
    else:
        return 'Your number is odd!'

while True:
    a = input('Please input an integer! ')
    try:
        a = int(a)
        if isinstance(a, int):
            break
    except ValueError:
        print('Not an integer! Try again!')


print(checker(a))


