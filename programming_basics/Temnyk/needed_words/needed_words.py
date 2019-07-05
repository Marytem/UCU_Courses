def find_chars():

    with open('words.txt', 'r') as file:
        all_words = file.read().split('\n')
        lst_len = []
        for word in range(len(all_words)):
            lst_len.append(len(all_words[word]))
        longest = []
        for ind in range(len(lst_len)):
            if max(lst_len) == lst_len[ind]:
                longest.append(all_words[ind])
        str_of_longest = ''
        for word in longest:
            str_of_longest += word
        char_set = set(str_of_longest)
        return char_set, all_words

length = int(input('Enter the length of words: '))
def write_words(needed, length):
    with open('words_needed.txt', 'w') as file:
        for word in needed[1]:
            if set(word) <= needed[0] and len(word) == length:
                file.write(word+'\n')

write_words(find_chars(), length)
    