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


def sorting(numbers):
    for i in range(len(numbers) - 1, 0, -1):
        for j in range(i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return(numbers)
numbers = sorting(numbers)

if int(len(numbers)/2) == float(len(numbers)/2):
    print('median = ', (numbers[int(len(numbers)/2)] + numbers[int(len(numbers)/2) + 1])/2)
else:
    print ('median = ', numbers[int(len(numbers)/2)])

    