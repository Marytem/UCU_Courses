def equal_parts(numbers):
    numbers1 = []
    numbers2 = []
    numbers.sort(reverse = True)
    for i in numbers:
        if sum(numbers1) < sum(numbers2):
            numbers1.append(i)
        else:
            numbers2.append(i)
    if sum(numbers1) == sum(numbers2):
        return(numbers1, numbers2)
    else:
        return([],[])
print(equal_parts([2, 2, 3, 4, 5]))