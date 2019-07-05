def sqrt(x):
    '''
    (number) -> number

    Return square root of number by Newton's Method
    guess = 1.0
    new_guess = 1/2(guess + x/guess)

    >>> sqrt(0.023)
    0.15165750888103102

    >>> sqrt(72)
    8.485281374239733
    '''

    def sqrt_iter():
        guess = 1.0
        while not good_enough(guess):
            guess = improve(guess)
        return guess

    def improve(guess):
        return average(guess, x/guess)

    def average(x, y):
        return (x + y)/2

    def good_enough(guess):
        if round(guess ** 2, 10) == x:
            return 1
        else:
            return 0

    return print("square root of " + str(x) + " =", sqrt_iter())
if __name__ == '__main__':
    import doctest
    doctest.testmod
