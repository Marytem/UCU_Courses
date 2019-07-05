#hw4.py
import math


def polygon_area(v):
    """
    list(tuple(number)) -> float
    list(list(number)) -> float
    Return an area of a polygon with coordinates
    of its vertexes.
    >>> polygon_area([(4,10), (9,7), (11,2), (2,2)])
    45.5
    >>> polygon_area([(9,7), (11,2), (2,2), (4, 10)])
    45.5
    >>> polygon_area([(0, 0), (0.5,1), (1,0)])
    0.5
    >>> polygon_area([(0, 10), (0.5,11), (1,10)])
    0.5
    >>> polygon_area([(-0.5, 10), (0,-11), (0.5,10)])
    10.5

    """
    v.append(v[0])
    area = 0
    for i in range(len(v) - 1):
        area += 0.5 * (v[i][0] * v[i + 1][1] - v[i + 1][0] * v[i][1])
    return abs(area)


def error(your_area, vertexes):
    '''
    (number, list(tuple(number))) -> bool
    Return True if area, calculated with polygon_area() and
    the other offered area are the same within about 5 decimal digits
    and False otherwise.
    >>> error(0.5, [(0, 0), (0.5,1), (1,0)])
    True
    '''
    area = polygon_area(vertexes)
    return math.isclose(area, your_area, rel_tol = 1e-05)


def polynomial_eval(coefficients, value):
    """
    (list(number), number) -> number
    Return a calculated value of a polynomial, preseted by
    its coefficients and a value of a variable.
    # f(x) = 2x^3 + 3x^2 + 4, f(4) = 180
    >>> polynomial_eval([2,3,0,4], 4)
    180
    >>> polynomial_eval([6], 42)
    6
    >>> polynomial_eval([6,-2,-20], -1)
    -12
    >>> polynomial_eval([6,0,-8,0,-8,0], 2)
    112
    >>> polynomial_eval([6,0,-8,0,-8,0], 1)
    -10
    >>> polynomial_eval([6,0,-8,0,-8,0], 0)
    0
    """
    main_value = 0
    for i in range(len(coefficients)):
        main_value += coefficients[i] * (value ** (len(coefficients) - 1 - i))
    return main_value


def polynomials_multiply(polynom1, polynom2):
    """
    (list(numbers), list(numbers)) -> list(numbers)
    Return the result value of the multiplication of two
    polynomials preseted by their coefficients.
    # (2x)*(3x) == 6
    >>> polynomials_multiply([2], [3])
    [6]
    >>> polynomials_multiply([2,-4],[3,5])
    [6, -2, -20]
    >>> polynomials_multiply([2,0,-4],[3,0,2,0])
    [6, 0, -8, 0, -8, 0]

    """
    multipolynom = []
    for i in range(len(polynom1)):
        group = []
        for j in range(len(polynom2)):
            group.append(polynom1[i] * polynom2[j])
        a = len(group)
        while len(group) < a + len(polynom1) - 1 - i:
            group.append(0)
        multipolynom.append(group)
        for i in range(len(multipolynom) - 1):
            while len(multipolynom[i]) > len(multipolynom[i + 1]):
                multipolynom[i + 1].insert(0, 0)
    final_polynom = []
    for j in range(len(multipolynom[0])):
        coef = 0
        for i in range(len(multipolynom)):
            coef += multipolynom[i][j]
        final_polynom.append(coef)
    return final_polynom


def pattern_number(sequence):
    """
    list -> tuple(list, int)
    str -> tuple(list, int)
    Return a tuple with a repeated sequence in a given one
    and a number of its occurences, if the given sequence cosists
    of repeated sequences only, and None otherwise.
    >>> pattern_number([])

    >>> pattern_number([42])

    >>> pattern_number([1,2])

    >>> pattern_number([1,1])
    ([1], 2)
    >>> pattern_number([1,2,1])

    >>> pattern_number([1,2,3,1,2,3])
    ([1, 2, 3], 2)
    >>> pattern_number([1,2,3,1,2])

    >>> pattern_number([1,2,3,1,2,3,1])

    >>> pattern_number(list(range(10))*20)
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 20)
    >>> pattern_number('мама')
    (['ма'], 2)
    >>> pattern_number('барабан')

    """
    if len(sequence) % 2 != 0:
        return None
    import copy
    remember_intheend = sequence
    if type(sequence) is str:
        sequence = list(sequence)
    seq2 = copy.copy(sequence)
    for i in range(len(sequence)-1):
        for j in range(len(sequence)):
            if j > 0:
                seq3 = []
                for n in range(0, int(round(len(seq2)/(j + 1)))):
                    seq3.append(seq2[((j + 1) * n):((j + 1) * (n + 1))])
                sequence = seq3
            a = sequence.count(sequence[i])
            if a > 1:
                pattern = sequence[i]
                while sequence.count(pattern) > 1:
                    sequence.remove(pattern)
                sequence.remove(pattern)
                if sequence == []:
                    if type(pattern) is float or type(pattern) is int:
                        return(([pattern], a))
                    elif type(remember_intheend) is str:
                        return(([''.join(pattern)], a))
                    else:
                        return((pattern, a))
                else:
                    continue
            elif len(sequence) > 2:
                continue
            else:
                return None


def one_swap_sorting(sequence):
    """
    list(number) -> bool
    Return True if after swapping two numbers in a list,
    it becomes sorted, and False otherwise.
    >>> one_swap_sorting([0,1,2,3])
    False
    >>> one_swap_sorting([])
    False
    >>> one_swap_sorting([42])
    False
    >>> one_swap_sorting([3,2])
    True
    >>> one_swap_sorting([2,2])
    True
    >>> one_swap_sorting([5,2,3,4,1,6])
    True
    >>> one_swap_sorting([1,2,3,5,4])
    True
    """
    if len(sequence) < 2:
        return False
    import copy
    first_sequence = copy.copy(sequence)
    for i in range(len(sequence)):
        sequence = copy.copy(first_sequence)
        for j in range(1, len(sequence) - i):
            sequence = copy.copy(first_sequence)
            sequence.insert(i+j, sequence[i])
            sequence.insert(i, sequence[i + j + 1])
            sequence.pop(i + 1)
            sequence.pop(i + j + 1)
            if sorted(first_sequence) == sequence:
                return True
            else:
                continue
    return False


def numbers_Ulam(n):
    """
    positive integers -> list
    Return a list of first n numbers from Ulam's sequence.
    >>> numbers_Ulam(10)
    [1, 2, 3, 4, 6, 8, 11, 13, 16, 18]
    >>> numbers_Ulam(5)
    [1, 2, 3, 4, 6]
    >>> numbers_Ulam(9)
    [1, 2, 3, 4, 6, 8, 11, 13, 16]
    >>> numbers_Ulam(7)
    [1, 2, 3, 4, 6, 8, 11]
    >>> numbers_Ulam(2)
    [1, 2]
    >>> numbers_Ulam(1)
    [1]
    """
    seq = [1, 2]
    if n == 1:
        return [seq[0]]
    if n == 2:
        return seq
    a = 200  # till that value Ulam's sequence will be calculated
    for m in range(3, a):
        waysget = 0
        for a in range(len(seq)):
            for b in range(a + 1, len(seq)):
                if seq[a] + seq[b] == m:
                    waysget += 1
                else:
                    continue
            if waysget > 1:
                break
        if n > 43:  #if a = 200, 43 numbers of Ulam's sequence are calculated.
            a += 20  #In this way m is always less than a.
        if waysget == 1:
            seq.append(m)
    if m > seq[-1] and waysget == 1:
        seq.append(m)
    return seq[:(n)]


def happy_number(n):
    """
    >>> happy_number(32)
    True
    >>> happy_number(33)
    False
    >>> happy_number(0b100001)
    True
    """

    return True


def sum_of_divisors(n, lst):
    """
    (int, list(int)) -> int
    Find and return sum of all odd numbers in the list, that are
    divisible by n.
    >>> sum_of_divisors(3, [2, 0, 1, 5])
    0
    >>> sum_of_divisors(5, [2, 0, 1, 5])
    5
    >>> sum_of_divisors(7, [])
    0

    """
    div_odds = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 1 and lst[i] % n == 0\
        and lst[i] != 0 and type(lst[i]) is int:
            div_odds += lst[i]
    return div_odds


def turn_over(n, lst):
    """
    ((int <= len(list)), list) -> list
    Reverse first n items of the list and return it. If n <= 0, return
    the empty list. Do not consume MORE than n items of iterable.

    >>> turn_over(4, ['f', 'o', 'o', 't', 'b', 'a', 'l', 'l'])
    ['t', 'o', 'o', 'f', 'b', 'a', 'l', 'l']
    >>> turn_over(5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]
    >>> turn_over(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    >>> turn_over(-5, [])
    []

    """
    if n <= 0:
        return []
    else:
        a = lst[n:]
        lst = list(reversed(lst[: n]))
        lst[len(lst):] = a
        return lst


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
