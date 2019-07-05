import random
art = ['a', 'this', 'the', 'her', 'his']
nouns = ['tree', 'parrot', 'plant', 'head', 'squirel']
verbs = ['keeps', 'runs', 'begs', 'bleeds', 'plays']
adv = ['quietly', 'strongly', 'fully', 'tightly', 'badly']
for a in range(5):
    if random.randint(0, 1) == 0:
        print(random.choice(art), random.choice(nouns), random.choice(verbs))
    else:
        print(random.choice(art), random.choice(nouns), random.choice(verbs), random.choice(adv))
