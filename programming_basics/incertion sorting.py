def insertion_sort(lst):
    for i in range(1, len(lst)):
        tmp = lst[i]
        j = i - 1
        while tmp < lst[j] and j > -1:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = tmp
    return lst
    
import random
import math
print(100000*100000)
print(int(100000*math.log(100000)))
numbers = []
for i in range(100000):
    numbers.append(random.randint(1,1000))