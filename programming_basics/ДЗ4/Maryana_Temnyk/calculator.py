def calculator():
    '''
    Return a result of addition, multiplication or a sum of squares
    of two entered numbers.
    >>> calculator()
    enter a number: 3
    enter a number: 4
    choose a, m, or s: a
    7
    '''
    num1 = eval(input("enter a number: "))
    num2 = eval(input("enter a number: "))
    operation = input("choose a, m, or s: ")
    if operation != 'a' and operation != 'm' and operation != 's':
        raise ValueError('enter a, m, or s')
    
    def addition(num1, num2):
        return num1 + num2
    def multiplication(num1, num2):
        return num1 * num2
    def sum_of_squares(num1, num2):
        return num1**2 + num2**2

    if operation == 'a':
        print(addition(num1, num2))
    if operation == 'm':
        print(multiplication(num1, num2))
    if operation == 's':
        print(sum_of_squares(num1, num2))
    
calculator()