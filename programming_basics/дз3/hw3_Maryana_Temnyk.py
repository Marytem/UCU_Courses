# Complete all of the following functions. Currently they all just
# 'pass' rather than explicitly return value, which means that they
# implicitly return None. They all include doctests, which you can
# test by running this file.

# The doctests are just examples. Feel free to add your own doctests.

# ****************************************
# Problem 1
# ****************************************
def get_position(ch):
    """
    str -> int
    Return positon of letter in alphabet. If argument is not a letter, function
    should return None.

    >>> get_position('g')
    7
    >>> get_position('A')
    1
    >>> get_position('z')
    26
    >>> get_position('Dj')

    """

    from string import ascii_lowercase
    ch = ch.lower()
    if ascii_lowercase.find(ch)+1:
        return ascii_lowercase.find(ch)+1
    else:
        return None


# ****************************************
# Problem 2
# ****************************************
def compare_char(ch1, ch2):
    """
    (str, str) -> bool
    Compare two char by their position in alphabet. Return True if letter
    ch2 appears before ch1 and False otherwise. If neither ch1 nor ch2 are
    letters function should return None.

    >>> compare_char('a', 'z')
    False
    >>> compare_char('c', 'B')
    True
    >>> compare_char('d', 'ad')
    >>> compare_char('2', 2)

    """
    pass

# ****************************************
# Problem 3
# ****************************************
def compare_str(s1, s2):
    """
    (str, str) -> bool
    Compare two srings lexicographicly. Return True if string s1 is larger
    than string s2 and False otherwise. If arguments aren't string or function
    have different length function should return None.

    >>> compare_str('abc', 'Abd')
    False
    >>> compare_str('zaD', 'zab')
    True
    >>> compare_str('zaD', 'Zad')
    False
    >>> compare_str('aaa', 'aaaaa')
    >>> compare_str('2015', 2015)
    """
    pass

# ****************************************
# Problem 4
# ****************************************
def type_by_angles(a, b, c):
    """
    (float, float, float) -> str
    Detect the type of triangle by it's angles in degrees and return type as
    string ("right angled triangle", "obutuse triangle", "acute triangle").
    If there is no triangle with such angles, then function should return None.

    >>> type_by_sides(60, 60, 60)
    acute triangle
    >>> type_by_sides(90, 30, 60)
    right angled triangle
    >>> type_by_sides(2015, 2015, 2015)
    """
    pass

# ****************************************
# Problem 5
# ****************************************
def type_by_sides(a, b, c):
    """
    (number, number, number) -> str
    Detect the type of triangle by it's sides and return type as string
    ("right angled triangle", "obutuse triangle", "acute triangle").
    If there is no triangle with such sides, then function should return None.

    >>> type_by_sides(3, 2, 2)
    'obutuse triangle'
    >>> type_by_sides(3, 3, 3)
    'acute triangle'
    >>> type_by_sides(3, 4, 5)
    'right angled triangle'
    >>> type_by_sides(3, 3, 2015)

    """
    sides = sorted([a, b, c])
    if sides[2] >= sides[1] + sides[0]:
        return None
    elif sides[2]**2 == sides[1]**2 + sides[0]**2:
        return 'right angled triangle'
    elif sides[2]**2 > sides[1]**2 + sides[0]**2:
        return 'obutuse triangle'
    elif sides[2]**2 < sides[1]**2 + sides[0]**2:
        return 'acute triangle'

print('Testing compare_char...', end='')
assert(type_by_sides(3, 3, 3) == "acute triangle")
assert(type_by_sides(3, 4, 5) == "right angled triangle")
assert(type_by_sides(3, 3, 2015) == None)
assert(type_by_sides(4.454, 3.06, 1.975) == "acute triangle")
print('Passed!')
# ***************************************
# Problem 6
# ****************************************
def remove_spaces(s):
    """
    str -> str
    Remove all additional spaces in string and return a new string without
    additional spaces. If argument is not a string function should return None.

    >>> remove_spaces("I'll make     him an     offer he can't refuse.")
    I'll make him an offer he can't refuse.
    >>> remove_spaces("Great    men     are    not born great, they grow great...")
    Great men are not born great, they grow great...
    >>> remove_spaces(2015)
    """
    pass

# ****************************************
# Problem 7
# ****************************************
def convert_to_column(s):
    """
    str -> str
    Convert string to a column of words.
    If argument is not a string function should return None.

    >>> print_column("Revenge is a dish that tastes best when served cold.")
    revenge
    is
    a
    dish
    that
    tastes
    best
    when
    served
    cold
    >>> print_column("Never hate your enemies. It affects your judgment.")
    never
    hate
    your
    enemies
    it affects
    your
    judgment
    >>> print_column(2015)
    """
    pass

# ****************************************
# Problem 8
# ****************************************
def number_of_sentences(s):
    """
    str -> str
    Return number of sentence in the string. If argument is not a string
    function should return None.

    >>> number_of_sentences("Revenge is a dish that tastes best when served cold.")
    1
    >>> number_of_sentences("Never hate your enemies. It affects your judgment.")
    2
    >>> number_of_sentences(2015)

    """
    pass

# ****************************************
# Problem 9
# ****************************************
def replace_with_starts(s):
    """
    str -> str
    Replace symbols in string with starts. If argument is not a string
    function should return None.

    >>> number_of_sentences("Revenge is a dish that tastes best when served cold.")
    ****************************************************
    >>> number_of_sentences("Never hate your enemies. It affects your judgment.")
    **************************************************
    >>> number_of_sentences(2015)

    """
    pass

# ****************************************
# Problem 10
# ****************************************
def encrypt_message(s):
    """
    str -> str
    Replace all letters in string with next letters in aplhabet.
    If argument is not a string function should return None.

    >>> encrypt_message("Revenge is a dish that tastes best when served cold.")
    'Sfwfohf jt b ejti uibu ubtuft cftu xifo tfswfe dpme.'
    >>> encrypt_message("Never hate your enemies. It affects your judgment.")
    'Ofwfs ibuf zpvs fofnjft. Ju bggfdut zpvs kvehnfou.'
    >>> encrypt_message(2015)

    """
    if type(s) is not str:
        return None
    else:
        from string import ascii_lowercase
        from string import ascii_uppercase
        for i in range(len(s)):
            if s[i] == s[i].lower() and ascii_lowercase.find(s[i]) >= 0:
                s = s[:i] + ascii_lowercase[(ascii_lowercase.find(s[i]) + 1)]\
                    + s[i+1:]
            elif s[i] == s[i].upper() and ascii_uppercase.find(s[i]) >= 0:
                s = s[:i] + ascii_uppercase[(ascii_uppercase.find(s[i]) + 1)]\
                    + s[i+1:]
        return s

# ****************************************
# Problem 11
# ****************************************
def decrypt_message(s):
    """
    str -> str
    Replace all letters in string with previous letters in aplhabet.
    If argument isn't a string function should return None.

    >>> decrypt_message("Sfwfohf jt b ejti uibu ubtuft cftu xifo tfswfe dpme.")
    Revenge is a dish that tastes best when served cold.
    >>> decrypt_message("Ofwfs ibuf zpvs fofnjft. Ju bggfdut zpvs kvehnfou.")
    Never hate your enemies. It affects your judgment.
    >>> decrypt_message(2015)

    """
    pass

# ****************************************
# Problem 12
# ****************************************
def exclude_letters(s1, s2):
    """
    (str, str) -> str
    Delete all letter from string s2 in string s1. If arguments aren't strings
    function should return None.

    >>> exclude_letters("aaabb", "b")
    aaa
    >>> exclude_letters("abcc", "cczzyy")
    ab
    >>> exclude_letters(2015, "sasd")

    """
    pass


# ****************************************
# Problem 13
# ****************************************
def create_string(lst):
    """
    list -> str
    Create and return string from histogrma of letters. If argument isn't list of 26 positive
    integer numbers function should return None.

    >>> create_string([0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    bcc
    >>> create_string([4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4]])
    aaaazzzz
    >>> create_string([4, 0, 0, 0, 0, 0])

    """
    pass

# ****************************************
# Problem 14
# ****************************************
def get_letters(n):
    """
    int -> str
    Create and return string of first n letters of an alphabet. If
    arguments isn't positive integer number function should return None.

    >>> get_letters(7)
    'abcdefg'
    >>> get_letters(0)

    >>> get_letters(1)
    'a'
    >>> get_letters(-2015)

    """
    from string import ascii_lowercase
    if 0 < n < 27 and type(n) is int:
        return ascii_lowercase[:n]
    else:
        return None


# ****************************************
# Problem 15
# ****************************************
def find_intersection(s1, s2):
    """
    (str, str) -> str
    Find and returs string of all letters in alphabetic order that
    are present in both strings. If arguments aren't strings function
    should return None.
    >>> find_intersection("dfgjhjkjjj", "DFthfkgh")
    'dfghk'
    >>> find_intersection("aaabb", "bbbcccc")
    'b'
    >>> find_intersection("aZAbc", "zzYYxp")
    'z'
    >>> find_intersection("sfdfsdf", 2015)

    """
    from string import ascii_lowercase
    if type(s1) is str and type(s2) is str:
        s1 = s1.lower()
        s2 = s2.lower()
        a = ''
        for i in range(26):
            if s1.find(ascii_lowercase[i]) >= 0\
                and s2.find(ascii_lowercase[i]) >= 0:
                a += ascii_lowercase[i]
        return a
    else:
        return None

# ****************************************
# Problem 16
# ****************************************
def find_union(s1, s2):
    """
    (str, str) -> str
    Find and return string of all letters in alphabetic order that
    are present at least in one of strings. If arguments aren't strings,
    function should return None.

    >>> find_union("aaabb", "bbbbccc")
    'abc'
    >>> find_union("aZAbc", "zzYYxp")
    'abcpxyz'
    >>> find_union("sfdfsdf", 2015)

    """
    from string import ascii_lowercase
    if type(s1) is str and type(s2) is str:
        s1 = s1.lower()
        s2 = s2.lower()
        a = ''
        for i in range(26):
            if s1.find(ascii_lowercase[i]) >= 0\
                or s2.find(ascii_lowercase[i]) >= 0:
                a += ascii_lowercase[i]
        return a
    else:
        return None


# ****************************************
# Problem 17
# ****************************************
def number_of_occurence(lst, s):
    """
    (list, str) -> int
    Find and return number of occurence of string s in all elements of the
    list lst. If lst isn't list of strings or s isn't string function should
    return None.

    >>> number_of_occurence(["man", "girl", "women", "boy"], "m")
    2
    >>> number_of_occurence(["ab", "aba", "a", "b", "ba"], "ba")
    2
    >>> number_of_occurence([1, 2, 2015, 1, 3], "1")

    """
    pass


# ****************************************
# Problem 18
# ****************************************
def number_of_capital_letters(s):
    """
    str -> int
    Find and return number of capital letters in string.
    If argument isn't string function should return None.
    >>> number_of_capital_letters("I 2gFdbfYS,F")
    5
    >>> number_of_capital_letters("ArithmeticError")
    2
    >>> number_of_capital_letters("EOFError")
    4
    >>> number_of_capital_letters(1)

    """
    from string import ascii_uppercase
    if type(s) is str:
        a = ''
        for i in range(len(s)):
            if ascii_uppercase.find(s[i]) >= 0:
                a += ascii_uppercase[i]
        return len(a)
    else:
        return None


if __name__ == '__main__':
    import doctest
    doctest.testmod()


