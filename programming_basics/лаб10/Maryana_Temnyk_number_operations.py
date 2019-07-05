def numbers_Ulam(n):
    """
    positive integers -> list
    Return a list of first n numbers from Ulam's sequence.
    >>> numbers_Ulam(10)
    [1, 2, 3, 4, 6, 8, 11, 13, 16, 18]
    >>> numbers_Ulam(5)
    [1, 2, 3, 4, 6]
    """
    seq = [1, 2]
    if n == 1:
        return [seq[0]]
    if n == 2:
        return seq
    a = 2000  # till that value Ulam's sequence will be calculated
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
    return seq[:n]

    
def even(n):
    ev = []
    for i in range(n):
        ev.append(2 * i)
    return ev


def game_board(choice2):
    import random
    numbers = []
    numbers.extend(numbers_Ulam(int(choice2/2)))
    numbers.extend(even(int(choice2/2)))
    random.shuffle(numbers)
    return numbers
