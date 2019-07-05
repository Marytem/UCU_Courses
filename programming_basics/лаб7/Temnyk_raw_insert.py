def dyvo_insert(sentence, flag):
    """
    Inserting word 'dyvo' before every word that starts with flag.
    (str, str) -> None
    >>> dyvo_insert('Kyt kota po hvyliah katav - kyt u vodi, kit na kyti.','ky')
    Dyvo-Kyt kota po hvyliah katav - dyvo-kyt u vodi, kit na dyvo-kyti.
    >>> dyvo_insert('Vorona provoronyla voronenia.', 'vor')
    Dyvo-Vorona provoronyla dyvo-voronenia.
    >>> dyvo_insert('Pyliav Pylyp polina z lyp, prytupyv pylku Pylyp.', 'pyl')
    Dyvo-Pyliav Dyvo-Pylyp polina z lyp, prytupyv dyvo-pylku Dyvo-Pylyp.
    """
    if sentence.startswith(flag.lower())\
        or sentence.startswith(flag.capitalize())\
            or sentence.startswith(flag.swapcase())\
            or sentence.startswith(flag.upper())\
            or sentence.startswith(flag):
        sentence = 'Dyvo-' + sentence
    flag = flag.lower()
    sentence = sentence.replace((' ' + flag), (" dyvo-" + flag))
    flag = flag.capitalize()
    sentence = sentence.replace((' ' + flag), (" Dyvo-" + flag))
    flag = flag.swapcase()
    sentence = sentence.replace((' ' + flag), (" dyvo-" + flag))
    flag = flag.upper()
    sentence = sentence.replace((' ' + flag), (" dyvo-" + flag))
    print(sentence)


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
