def dict_reader_tuple(file_dict):
    '''
    str -> list(tuples)

    Return a list of tuples, each contains a word, a number of
    transcription and a list of word's syllables from the file.
    '''
    with open(file_dict, 'r') as file:
        vocab = file.read().split('\n')
        vocab.remove('')
        vocab_lst = []
        for line in vocab:
            line = line.split()
            vocab_lst.append((line[0], int(line[1]), line[2:]))
        return vocab_lst


def dict_reader_dict(file_dict):
    '''
    str -> dict

    Return a dicrionary, the keys of which are words from the given
    file and the values are sets of tuples of word's syllables.
    '''
    with open(file_dict, 'r') as file:
        vocab = file.read().split('\n')
        vocab.remove('')
        vocab_dct = {}
        for line in vocab:
            line = line.split()
            if line[0] in vocab_dct:
                vocab_dct[line[0]].add(tuple(line[2:]))
            else:
                vocab_dct[line[0]] = {tuple(line[2:])}
        return vocab_dct


def dict_invert(vocab):
    '''
    list -> dict
    dict -> dict

    Return a dicrionary, keys of which are numbers of transcriptions for
    one word, and values are sets of tuples with a word and a list of its
    syllables.
    '''
    vocab_dct = {}
    for word in vocab:
        if len(vocab[word]) not in vocab_dct:
            vocab_dct[len(vocab[word])] = set()
        for trans in vocab[word]:
            vocab_dct[len(vocab[word])].add((word, list(trans)))
    return vocab_dct
