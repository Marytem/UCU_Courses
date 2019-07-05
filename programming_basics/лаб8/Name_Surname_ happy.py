def happy_number(number):
    if len(str(number)) == 8:
        number = list(str(number))
        for i in range(len(number) + 1):
            number[i] = int(number[i])
    elif len(str(number)) < 8:
        number = list(str(number))
        for i in range(9 - len(str(number))):  
            number.insert(1,'0')
        for i in range(len(number)):
            number[i] = int(number[i])
    else:
        return None
    a = [:len(number)/2]
    y = [len(number)/2:]
    if sum(a) == sum(y):
        return True
    else:
        return False                              
print(happy_number(191234))
def count_happy_numbers(n):
    amount = 0
    for i in range(n+1):
        if happy_number(i):
            amount += 1
    return amount
    

def happy_numbers(m,n):
    tickets = []
    for i in range(m, n+1):
        if happy_number(i):
            tickets.append(i)
    return tickets