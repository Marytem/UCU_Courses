def read_data(path_file):
    """
    (str) -> (list)
    Return list of words and list of sents from files
    """
    f = open(path_file, 'r', encoding ='utf-8')
    sequence = f.readlines()
    sequence = [w.strip() for w in sequence]
    f.close()
    
    return sequence
    
def seq_stat(sequence):
    """
    (sequence) -> int, int 
    Return amount sequence elements and amount sequence unique elements 
    """
    return len(sequence), len(set(sequence))

def skey(item):
    return item[1]
    
def dict_freq(sequence):
    d_freq = dict()
    for word in sequence:
        if word in d_freq:
            d_freq[word] += 1
        else:
            d_freq[word] = 1

    tdict = [(i, d_freq[i]) for i in d_freq]
    sorted_dict = sorted(tdict, key = skey, reverse = True)
    return sorted_dict

words = read_data('D:\Oles\Python34\Scripts\Week9\Romanyuk_wordslist.txt')
sents = read_data('D:\Oles\Python34\Scripts\Week9\Romanyuk_list.txt')

words_stat = seq_stat(words)
sents_stat = seq_stat(sents)
print('''tokens in text {} 
         unique tokens in text {}'''.format(words_stat[0], words_stat[1]))
print('''sents in text {} 
         unique sents in text {}'''.format(sents_stat[0], sents_stat[0]))

#words = [w for w in words if w.isalpha()]
words_stat = seq_stat(words)
print ('''words in text {} 
         voc of text {} '''.format(words_stat[0], words_stat[1]))

freq_words = dict_freq(words)
print('items in frequence distribution of words {}'.format(len(freq_words)))
#print(freq_words[:10], freq_words[-10:])

bigrams_list = []
for sent in sents:
    sent1 = [s for s in sent.split() if sent.split() and s.isalpha()]
    #if len(sent1)%2 != 0:
     #   sent1 = sent1 + [None]
    
    sent1 = iter(sent1)
    n = 2
    history = []
    
    while n > 1:
        history.append(next(sent1))
        n -= 1
    
    for item in sent1:
        history.append(item)
        bigrams_list.append(tuple(history))
        del history[0]

print(len(bigrams_list))
print(len(set(bigrams_list)))

tdict = dict_freq(bigrams_list)
#print(tdict[:10])
n = 10
next_word = 'молоко'
while n:
    print(next_word, end = " ")
    next_x = []
    for i in tdict:
        #print(i,i[0][0])
        if next_word == i[0][0]:
            if i[0]:
                next_x.append((i[0][1],i[1]))
    #print(next_x)

    #next_x = sorted(next_x, key = skey, reverse = True)
    #print(next_word, next_x)
    if next_x: 
        next_word = next_x[0][0]
    n -= 1 


