import sys
import random
art = ['a', 'this', 'the', 'her', 'his']
nouns = ['tree', 'parrot', 'plant', 'head', 'squirel']
verbs = ['keeps', 'runs', 'begs', 'bleeds', 'plays']
adv = ['quietly', 'strongly', 'fully', 'tightly', 'badly']
r = int(sys.argv[1])
if 1 <= r <= 10:
    for a in range(r):
        if random.randint(0, 1) == 0:
            print(random.choice(art), random.choice(nouns), random.choice(verbs))
        else:
            print(random.choice(art), random.choice(nouns), random.choice(verbs), random.choice(adv))
else:
    print('enter a number between 1 and 10')
