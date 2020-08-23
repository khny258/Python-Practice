def is_even():
    x = input('Enter a number: ')

    is_even = int(x) % 2 == 0

    if is_even:
        print('Even')
    else:
        print('Odd')

is_even()