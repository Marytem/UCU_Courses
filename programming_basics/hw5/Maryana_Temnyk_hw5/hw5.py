# Complete all of the following functions. Currently they all just
# 'pass' rather than explicitly return value, which means that they
# implicitly return None.

# The doctests are just examples. Feel free to add your own doctests.

# ****************************************
# Useful links
# ****************************************

# Luhn algorithm: https://en.wikipedia.org/wiki/Luhn_algorithm
# Caesar cipher: https://en.wikipedia.org/wiki/Caesar_cipher
# Binary number: https://en.wikipedia.org/wiki/Binary_number


# ****************************************
# Problem 1
# ****************************************
def clear_list(lst):
    r"""
    (list(str)) -> (list(str))

    Delete all empty strings or string with whitespaces from list and return
    updated list. If argument is incorrect, function should return None.

    >>> clear_list(['  ', 'alphabet', 'lion', 'king\t', '\t'])
    ['alphabet', 'lion', 'king\t']
    """
    if type(lst) is not list:
        return None
    for strings in reversed(lst):
        if strings.count(' ') == len(strings)\
                or strings.count('\t') == len(strings):
            lst.remove(strings)
        elif type(strings) is not str:
            return None
    return lst


# ****************************************
# Problem 2
# ****************************************
def get_board(lst):
    r"""
    (list) -> (str)

    Convert matrix of numbers to the board of the game Tic-Tac-Toe (1 -> "x",
    -1 -> "o", 0 -> " ") and return it as string. If argument is incorrect,
    function should return None.

    >>> get_board([[1, -1, 0], [0, 0, 0], [1, -1, 0]])
    'xo \n   \nxo \n'
    """
    if type(lst) is not list:
        return None
    for raw in range(len(lst)):
        if type(lst[raw]) is not list:
            return None
        for symb in range(len(lst[raw])):
            if lst[raw][symb] != 1 and lst[raw][symb] != -1\
                    and lst[raw][symb] != 0:
                return None
            lst[raw][symb] = str(lst[raw][symb])
        lst[raw].append('\n')
        lst[raw] = ''.join(lst[raw])
        lst[raw] = lst[raw].replace('-1', 'o')
        lst[raw] = lst[raw].replace('1', 'x')
        lst[raw] = lst[raw].replace('0', ' ')
    lst = ''.join(lst)
    return lst


# ****************************************
# Problem 3
# ****************************************
def find_prime(number):
    """
    (int) -> (int)
    Preconditions: number > 1

    Find and return the smallest prime number that doesn't divide number. If
    argument is incorrect, function should return None.

    >>> find_prime(510510)
    19
    """
    pr = 2
    while True:
        counter = 0
        for i in range(2, pr):
            if pr % i == 0:
                counter += 1
        if counter == 0 and number % pr != 0:
            return pr
            break
        else:
            pr += 1
            continue


# ****************************************
# Problem 4
# ****************************************
def convert_date(s):
    """
    (str) -> (str)
    Convert date in format dd-mm-yyyy to mmmm d, yyyy. If argument is incorrect,
    function should return None.

    >>> convert_date("01-11-1996")
    'November 1, 1996'
    >>> convert_date("12-07-4567")
    'July 12, 4567'
    """
    if type(s) is not str:
        return None
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',\
        'August', 'September', 'October', 'November', 'December']
    s = s.split('-')
    for i in range(len(s)):
        if not int(s[i]) + 1:
            return None
        s[i] = int(s[i])
    a = str(s[0])
    s[0] = months[s[1] - 1]
    s[1] = a + ','
    s[2] = str(s[2])
    s = ' '.join(s)
    return s


# ****************************************
# Problem 5
# ****************************************
def validate_credit_card(s):
    """
    (str) -> (bool)

    Validate 16-digit credit card number with Luhn algorithm. If according to
    Luhn algorithm card number is valid function return True, False otherwise.

    >>> validate_credit_card("4385822056110988")
    True
    >>> validate_credit_card("4561261212345467")
    True
    """
    if len(s) != 16 or type(s) is not str:
        raise ValueError('Card number has 16 digits, enter them as string.')
    check = 0
    for place in range(len(s)):
        if place % 2 == 0:
            if int(s[place]) * 2 > 9:
                check += int(s[place]) * 2 - 9
            else:
                check += int(s[place]) * 2
        else:
            check += int(s[place])
    if check % 10 == 0:
        return True
    else:
        return False


# ****************************************
# Problem 6
# ****************************************
def check_word(s):
    """
    (str) -> (int)

    Return True if word is written correctly and False otherwise.

    >>> check_word("Apple")
    True
    """
    if s != s.capitalize() and s != s.lower():
        return True
    s = s.lower()
    with open('en', 'r') as file:
        words = file.read().split('\n')
        if s in words:
            return True
        else:
            return False


# ****************************************
# Problem 7
# ****************************************
def number_of_mistakes(s):
    """
    (str) -> (int)

    Compute the number of mistakes. The word can't have more than one mistake.
    If argument is incorrect, function should return None.

    >>> number_of_mistakes("Easy peasy japanesey.")
    1
    >>> number_of_mistakes("My hgfkfkif, is japanesey.")
    2
    """
    if type(s) is not str:
        return None
    from string import ascii_lowercase
    mist = 0
    if s.find(',') != -1:
        s = s.replace(',', '')
    elif ascii_lowercase.find(s[-1]) == -1:
        s = s.replace(s[-1], '')
    s = s.split()
    for word in s:
        if check_word(word) == False:
            mist += 1
    return mist


# ****************************************
# Problem 8
# ****************************************
def decrypt_word(s):
    """
    (str) -> (list(str))

    Preconditions: s is the word encrypted with shifting letter to n position to
    the right in the alphabet (see Caesar cipher).

    Return list of all possible decryption of this word. If argument is
    incorrect, function should return None.

    >>> decrypt_word('hdvb')
    ['easy']
    """
    if type(s) is not str:
        return None
    from string import ascii_lowercase
    abc = ascii_lowercase
    s = s.lower()
    copy_s = s.strip()
    decryptions = []
    for key in range(1, 26):
        s = copy_s
        for letter in s:
            s = s.replace(letter, abc[- 26 + abc.find(letter) + key])
        if check_word(s) == True:
            decryptions.append(s)
    if decryptions == []:
        return None
    else:
        return decryptions


# ****************************************
# Problem 9
# ****************************************
def guess_word(s):
    """
    (str) -> (list)

    Preconditions: s is word some letter of which are replaced with stars.

    Return list of all possible initial words by comparing word s with words
    from the file en.txt. If argument is incorrect, function should return
    None.

    >>> guess_word('d*g')
    ['dig', 'dog', 'dug']
    """
    if type(s) is not str:
        return None
    s.lower()
    changes = s.count('*')
    copy_s = s.strip()
    for i in range(changes):
        s = s[:(s.find('*') + 1)].replace('*', str(i)) + s[(s.find('*') + 1):]
    guesses = []
    with open('en', 'r') as file:
        voc = file.read().split('\n')
        for word in voc:
            word = word.lower()
            s = copy_s
            for i in range(changes):
                if len(s) == len(word) and s[:s.find(str(i))] + s[(s.find(str(i)) + 1):] == word[:s.find(str(i))] + word[(s.find(str(i)) + 1):]:
                    guesses.append(word)
                s = word[:(s.find(str(i)) + 1)] + s[(s.find(str(i)) + 1):]
    if guesses == []:
        return None
    else:
        return guesses


# ****************************************
# Problem 10
# ****************************************
def check_anagrams(s1, s2):
    """
    (str, str) -> (bool)

    Preconditions: s1 and s2 are words.

    Return True if s2 is an anagram of s1 and False otherwise. If argument are
    incorrect, function should return None.

    >>> check_anagrams('Mary', 'army')
    True
    >>> check_anagrams('tire', 'iter')
    True
    """
    if not check_word(s1):
        return None
    if not check_word(s2):
        return None
    s1 = s1.lower()
    s2 = s2.lower()
    counter = 0
    if len(s1) == len(s2):
        for ch in s1:
            if ch not in s2:
                return False
            else:
                counter += 1
        for ch in s2:
            if ch not in s1:
                return False
            else:
                counter += 1
        if counter == len(s1) * 2:
            return True
    else:
        return False


# ****************************************
# Problem 11
# ****************************************
def is_anagram(s):
    """
    (str) -> (bool)

    Preconditions: s is word.

    Return True if s is anagram of another word and False otherwise. If argument
    is incorrect, function should return None.

    >>> is_anagram('Mary')
    True
    >>> is_anagram('tire')
    True
    >>> is_anagram('compliment')
    False
    """
    if not check_word(s):
        return None
    s = s.lower()
    with open('en', 'r') as file:
        voc = file.read().split('\n')
        for word in voc:
            counter = 0
            if len(word) == len(s) and word != s:
                for letter in s:
                    if letter in word and s.count(letter) == word.count(letter):
                        counter += 1
                for letter in word:
                    if letter in s:
                        counter += 1
                if counter == len(s) * 2:
                    return True
                elif word == voc[-1]:
                    return False
                else:
                    continue
            elif word == voc[-1]:
                return False
            else:
                continue


# ****************************************
# Problem 12
# ****************************************
def create_words_1(lst):
    """
    (list(str)) -> (lisr(str))

    Preconditions: lst is a list of small letters
    Return list of all possible words that could be created from letters of
    list lst. Each letters can be used many times. If argument is
    function should return None.

    >>> create_words_1(['d', 'o'])
    ['do', 'dod', 'dodd', 'dodo', 'od', 'odd']
    >>> create_words_1(['l', 'o'])
    ['lo', 'loll', 'loo']
    """
    if type(lst) is not list:
        return None
    for ch in lst:
        if type(ch) is not str or len(ch) > 1:
            return None
    create = []
    with open('en', 'r') as file:
        voc = file.read().split('\n')
        for word in voc:
            counter = 0
            if len(word) > 1:
                for letter in word:
                    if letter in lst:
                        counter += 1
                    else:
                        break
            else:
                continue
            if counter == len(word):
                create.append(word)
    return create


# ****************************************
# Problem 13
# ****************************************
def create_words_2(lst):
    """
    (list) -> (lisr(str))

    Preconditions: lst is a list of lowercase letters.

    Return list of all possible words (from file en.txt) that could be
    created from letters of the list lst. Each letters can be as many times as
    they occur in list. If argument is incorrect, function should return None.

    >>> create_words_2(['d', 'o', 'g'])
    ['dog', 'god']
    >>> create_words_2(['r', 'i', 't', 'e'])
    ['iter', 'reit', 'rite', 'tier', 'tire']
    """
    if type(lst) is not list:
        return None
    for ch in lst:
        if type(ch) is not str or len(ch) > 1:
            return None
    import copy
    first_lst = copy.copy(lst)
    create = []
    with open('en', 'r') as file:
        voc = file.read().split('\n')
        for word in voc:
            counter = 0
            lst = copy.copy(first_lst)
            if len(word) == len(first_lst):
                for letter in word:
                    if letter in lst:
                        counter += 1
                        lst.remove(letter)
                    else:
                        break
            else:
                continue
            if counter == len(first_lst):
                create.append(word)
    return create


# ****************************************
# Problem 14
# ****************************************
def create_new(s):
    """
    (str) -> (lst(str))

    Preconditions: s is a word.

    Return a list of new words by conctatenating this word with one new letter.
    Plural of the word is not considered.
    If argument is incorrect, function should return None.

    >>> create_new('cat')
    ['cate', 'scat']
    """
    if not check_word(s):
        return None
    from string import ascii_lowercase
    s = s.lower()
    new_w = []
    for ch in ascii_lowercase:
        if check_word(ch + s):
            new_w.append(ch + s)
        elif check_word(s + ch):
            new_w.append(s + ch)
    return new_w


# ****************************************
# Problem 15
# ****************************************
def max_sum(lst, n):
    """
    (list(number), int) -> (tuple(number))

    Preconditions: n >= 0.

    Return tuple of n elements with maximal sum. If argument is incorrect,
    function should return None.

    >>> max_sum([3, 1, 2, 8, 11, 10], 3)
    (8, 10, 11)
    """
    if type(lst) is not list and type(n) is not int:
        return None
    for num in lst:
        if type(num) is not int and type(num) is not float:
            return None
    lst = sorted(lst)
    return tuple(lst[- n:])


# ****************************************
# Problem 16
# ****************************************
def max_product(lst, n):
    """
    (list(number), int) -> (tuple(number))

    Preconditions: n >= 0.

    Return tuple of n elements with maximal product. If argument is incorrect,
    function should return None.

    >>> max_product([3, 1, 2, 8, 11, 10], 3)
    (8, 10, 11)
    >>> max_product([-6, -4, 0, 4, 9, 15], 3)
    (15, 9, 4)
    >>> max_product([-277, -5, -3, 0, 1, 2, 4, 6], 4)
    (-277, -5, 6, 4)
    """
    if type(lst) is not list and type(n) is not int:
        return None
    for num in lst:
        if type(num) is not int and type(num) is not float:
            return None
    lst = sorted(lst)
    nums = []
    if lst[1] < 0:
        if n % 2 == 0:
            for i in range(int(n/2)):
                if lst[0] * lst[1] > lst[-1] * lst[-2]:
                    nums.append(lst[0])
                    nums.append(lst[1])
                    lst = lst[2:]
                else:
                    nums.append(lst[-1])
                    nums.append(lst[-2])
                    lst = lst[:-2]
            return tuple(nums)
        else:
            for i in range(round(n/2) - 1):
                if lst[0] * lst[1] > lst[-1] * lst[-2]:
                    nums.append(lst[0])
                    nums.append(lst[1])
                    lst = lst[2:]
                else:
                    nums.append(lst[-1])
                    nums.append(lst[-2])
                    lst = lst[:-2]
            nums.append(max(lst))
            return tuple(nums)
    else:
        return tuple(lst[- n:])


# ****************************************
# Problem 17
# ****************************************
def symmetric_difference(lst1, lst2):
    """
    (list(number), list(number)) -> (list(number))

    Return symmetric difference of two sets of numbers that are represented by
    lists lst1 and lst2. If argument are incorrect, function should return None.

    >>> symmetric_difference([0, 1, 2, 3], [2, -1, 3, 4])
    [0, 1, -1, 4]
    """
    if type(lst1) is not list or type(lst2) is not list:
        return None
    for num in lst1:
        if type(num) is not int and type(num) is not float:
            return None
    for num in lst2:
        if type(num) is not int and type(num) is not float:
            return None
    dif = []
    for item in lst1:
        if item not in lst2:
            dif.append(item)
    for item in lst2:
        if item not in lst1:
            dif.append(item)
    return dif


# ****************************************
# Problem 18
# ****************************************
def to_decimal(s):
    """
    (str) -> (int)

    Preconditions: s is a binary number.

    Convert binary number to decimal and return result.

    >>> to_decimal('10')
    2
    >>> to_decimal('110001')
    49
    """
    res = 0
    for i in range(len(s)):
        res += (2 ** (len(s) - 1 - i)) * int(s[i])
    return res


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
