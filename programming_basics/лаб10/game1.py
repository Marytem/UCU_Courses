import time
import random
import Maryana_Temnyk_number_operations
print('INVITATION')
choice1 = input('print "start", "quit" or "how to play" ')
if choice1 == 'quit':
    print('press ctrl + Z + Enter')
elif choice1 == 'how to play':
    print('rules')
    choice1 = input('print "start", "quit", "how to play" ')
elif choice1 == ('start'):
    choice2 = int(input('how many numbers do you want? print 20, 50 or 100 '))
    score = 0
    clock = 0
    while clock <= 100:
        print(Maryana_Temnyk_number_operations.game_board(choice2))
        a = random.choice(("even number", "Ulam's number"))
        print(a)
        st = time.time()
        ch = input()
        end = time.time()
        clock += end - st
        if a == "even number" and ch in Maryana_Temnyk_number_operations.even(int(choice2/2)):
            score += 10
        elif a == "Ulam's number" and ch in Maryana_Temnyk_number_operations.numbers_Ulam(int(choice2/2)):
            score += 10
    print('your score: ', score)
