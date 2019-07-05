numbers = []
while True:
    try:
        line = input("enter a number or Enter to finish ")
        if line:
            numbers.append(eval(line))
        else:
            break
    except ValueError as err:
        print(err)
        continue
    except EOFError:
        break
print(numbers)
print('count = ', len(numbers))


def suma(numbers):
    thesum = 0
    for i in numbers:
        thesum += float(i)
    return thesum
print('sum = ', suma(numbers))
print('lowest = ', min(numbers))
print('highest = ', max(numbers))
print('mean = ', suma(numbers)/len(numbers))
