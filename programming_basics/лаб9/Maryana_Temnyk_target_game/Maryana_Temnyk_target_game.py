import random


def letters_generation():
    '''
    Return a list of 9 randomly generated letters.
    >>> letters_generation()
    ['t', 'b', 't', 'u', 'i', 'l', 'f', 'a', 'e']
    '''
    given_ch = random.sample(['a', 'e', 'i', 'o', 'u', 'y', 'a',
        'e', 'i', 'o', 'u', 'y'], random.randint(3, 4))
    given_ch.extend(random.sample(['b', 'c', 'd', 'f', 'g', 'h', 'j',
        'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x',
            'z', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
                'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x',
                    'z'], 9 - len(given_ch)))
    random.shuffle(given_ch)
    return given_ch
given_ch = letters_generation()


def game_board(given_ch):
    '''
    list -> None
    Print a game board with 9 letters.
    >>> game_board(['t', 'b', 't', 'u', 'i', 'l', 'f', 'a', 'e'])
    -----------------
    | t  |  b  |  t |
    | ------------- |
    | u  |  i  |  l |
    | ------------- |
    | f  |  a  |  e |
    -----------------
    '''
    print('   ', '-----------------')
    print('    |', given_ch[0], ' | ', given_ch[1], ' | ', given_ch[2], '|')
    print('    |', '-------------', '|')
    print('    |', given_ch[3], ' | ', given_ch[4], ' | ', given_ch[5], '|')
    print('    |', '-------------', '|')
    print('    |', given_ch[6], ' | ', given_ch[7], ' | ', given_ch[8], '|')
    print('   ', '-----------------')
game_board(given_ch)


def read_vocab():
    '''
    Return a list with 9-character length words with central letter
    from gameboard, chosen from file en.txt.
    '''
    with open('en', 'r') as file:
        vocab = []
        filelist = file.read().split('\n')
        for word in filelist:
            if word.find(given_ch[4]) + 1 and 10 > len(word) >= 4\
                    and word.lower() == word:
                vocab.append(word)
    return vocab
norm_vocab = read_vocab()


def word_inp():
    '''
    Return a list with entered by a player words.
    >>> Enter a word or press 'Enter' to finish: lily
    >>> Enter a word or press 'Enter' to finish: wave
    >>> Enter a word or press 'Enter' to finish: run
    >>> Enter a word or press 'Enter' to finish:
    ['lily', 'wave', 'run']
    '''
    your_words = []
    while True:
        your_w = input("Enter a word or press 'Enter' to finish: ")
        if your_w:
            your_words.append(your_w)
        else:
            break
    return your_words
your_words = word_inp()


def get_correct_words(vocab, given_ch):
    '''
    list, list -> list
    Return a list with words, which can be composed from a list of
    9 given letters and are chosen from a given list of words,
    according to the rules of game.
    >>> get_correct_words(vocab, ['w', 'h', 'i', 'a', 'i', 'q', 'u', 'm', 'f'])
    ['hami', 'huia', 'maqui', 'waif', 'whim']
    '''
    corrwords = []
    for word in vocab:
        ch = given_ch[:]
        checklet = True
        for letter in word:
            if ch.count(letter) > 0:
                ch.remove(letter)
            else:
                checklet = False
                break
        if checklet:
            corrwords.append(word)
    return corrwords

    word = len(vocab) - 1
    while word + 1 > 0:
        if vocab[word].find(given_ch[4]) + 1 and len(vocab[word]) >= 4:
            ch = given_ch[:]
            checklet = True
            for letter in vocab[word]:
                if ch.count(letter) > 0:
                    ch.remove(letter)
                else:
                    checklet = False
                    break
            if not checklet:
                vocab.remove(vocab[word])
            word -= 1
        else:
            vocab.remove(vocab[word])
            word -= 1
    return vocab
vocab = get_correct_words(norm_vocab, given_ch)


def get_results(your_words, vocab):
    '''
    list, list -> None
    Print number of words, which are present in both given lists,
    and two lists without these words.
    >>> get_results(['whim', 'waife'], ['hami', 'maqui', 'waif', 'whim'])
    number of correct words -  1
    missing words:
    hami
    maqui
    waif
    incorrect words:
    waife
    '''
    num_of_correct = 0
    missing_words = []
    incorr_words = []
    for word in your_words:
        if word in vocab:
            num_of_correct += 1
            vocab.remove(word)
        else:
            incorr_words.append(word)
        missing_words = vocab
    print('number of correct words - ', num_of_correct)
    print('missing words:')
    for word in missing_words:
        print(word)
    print('incorrect words:')
    for word in incorr_words:
        print(word)

    with open('results.txt', 'w') as output_file:
        output_file.write('number of correct words - ')
        output_file.write(str(num_of_correct))
        output_file.write('/n')
        output_file.write('missing words:/n')
        for word in missing_words:
            output_file.write(word + '  ')
        output_file.write('incorrect words:/n')
        for word in incorr_words:
            output_file.write(word + '  ')

get_results(your_words, vocab)
