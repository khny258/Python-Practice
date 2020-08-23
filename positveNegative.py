def is_even(x):
    if x > 0:
        print('Positive')
    elif x < 0:
        print('Negative')
    else:
        print('Zero')

x = input('Enter a number: ')
x = int(x)
is_even(x)