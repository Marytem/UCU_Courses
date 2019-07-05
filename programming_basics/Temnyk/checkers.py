def create_checkboard(size):
    size = int(input('enter 6,8,10 or 12'))
    st = 'abcdefghijkl'
    checkboard = []
    for i in range(1, size):
        for ch in st[:(size-1)]:
        checkboard.append([ch, i])
    return checkboard

    
def add_checcers(checkboard):
    import math
    for i in range(len(checkboard)):
        if i%2 != 0 and i<= math.sqrt(len(checkboard)):
            checkboard[i].append('black')
    for i in reversed(range(len(checkboard))):
        if i%2 != 0 and i<= math.sqrt(len(checkboard)):
            checkboard[i].append('white')