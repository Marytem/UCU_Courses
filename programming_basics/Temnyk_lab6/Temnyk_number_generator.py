number = str(input('Enter any integer: '))
digit = str(input('Enter an integer between 0 and 9: '))
position = int(input('Enter any positive integer: '))


def  number_generator(number, digit, position):
    if int(digit) > 9 or int(digit) < 0 or position < 0:
        raise ValueError ('ValueError')
    elif position > len(number):
        number = digit + (position - len(number))*'0' + number
    else:
        number = number.replace((number)[-position -1], digit)
    print(number)


number_generator(number, digit, position)