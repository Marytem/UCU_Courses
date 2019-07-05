def encrypting(message, key):
    from string import printable
    encrypted = printable[printable.find(message[-1]) + key%9 - printable.find(message[0])]
    for i in range(1, len(message)):
        encrypted += printable[printable.find(encrypted[i-1]) + key%9 - printable.find(message[i])]
    encrypted = ''.join(encrypted)
    return encrypted
a = encrypting('what is the problem12345?!@#$%^&*()', 4567)

def decrypting(encrypted, key):
    from string import printable
    decrypted = list(map(lambda x: printable[printable.find(encrypted[x-1]) + key%9 - printable.find(encrypted[x])], reversed(range(len(encrypted)))))
    decrypted = ''.join(reversed(decrypted))
    decrypted = printable[printable.find(decrypted[-1]) + key%9 - printable.find(encrypted[0])] + decrypted[1:]
    return decrypted
print(decrypting(a, 4567))
print(decrypting(encrypting('what is the problem12345?!@#$%^&*()', 4567), 4567))
#may be find or index (whatever u choose)
def num_gen():
    import random
    def randprime():
        randline = random.randint(1, 78473)
        with open('primes.txt', 'r') as primes:
            lineind = 1
            for line in primes:
                if lineind == randline:
                    return int(line[:-1])
                else:
                    lineind += 1
    Y = random.randrange(8, 16)
    P = randprime()
    return Y, P 
print(num_gen())


def halfkey_gen(tup):
    import secrets
    A = secrets.choice(range(100,150))
    a = (tup[0]**A) % tup[1]
    return a
print(halfkey_gen(num_gen()))
