def board_generation():
    '''
    Return a list of lists, which represents 'Eternas' game-board.
    >>> board_generation()
    [[0, '"', '"', '"'], ['"', '"', '"', '"'], [0, 0, 0, 1], [0, 1, 0, '"'],
    [1, 0, 1, '"'],[0, 0, 1, 1], [0, 1, 0, '"'], [1, 0, 0, 1],
    ['"', '"', '"', '"'], ['"', '"', '"', '"'],[1, 1, 1, 1],
    [0, '"', '"', '"'], ['"', '"', '"', '"'], ['"', '"', '"', '"'],
    [1, 0, '"', '"'], ['"', '"', '"', '"']]
    '''
    import random
    board = []
    num_of_0 = 0
    num_of_1 = 0
    for balls_num in random.sample([0, 1, 2, 3, 4] * 16, 16):
        stick = []
        for ball in range(balls_num):
            if num_of_0 < 16 and num_of_1 < 16:
                stick.append(random.randrange(2))
            elif num_of_0 == 16 and num_of_1 == 16:
                stick = []
            elif num_of_0 == 16 and num_of_1 < 16:
                stick.append(1)
            else:
                stick.append(0)
            if stick != []:
                if stick[ball] == 0:
                    num_of_0 += 1
                else:
                    num_of_1 += 1
        while len(stick) < 4:
            stick.append('"')
        board.append(stick)
    return board


def winning_combination(board):
    '''
    finds out a winning combinaton on 'Eternas' game-board.
    If there is no winning combination on the board returns False,
    otherrwise returns True, a list with tuples of coordinares of thefirst
    and the last ball in winning combination and a type of the ball (0 or 1).
    Horisontal coordinates are represented in two ways: either counted from
    beginning(first coordinate = 0), or from the end (last ball i the row has
    coordinate -1).
    >>> winning_combination([[0, 1, 0, '"'], [1, 0, 0, 0], [0, 0, 0, 1],
    [1, 1, '"', '"'], [0, 0, 0, '"'], ['"', '"', '"', '"'], [0, 0, 0, '"'],
    [0, 0, 1, 1], [1, 1, '"', '"'], [1, 1, '"', '"'], ['"', '"', '"', '"'],
    [1, '"', '"', '"'], [1, 1, '"', '"'], [1, '"', '"', '"'],
    ['"', '"', '"', '"'], ['"', '"', '"', '"']])
    False
    '''
    win_comb = []
    for i in range(-4, 12):
        vert = 0
        horiz = 0
        diagon1 = 0
        diagon2 = 0
        for j in range(3):
            if board[i][j] == board[i][j + 1] and board[i][j] != '"':
                vert += 1
        if vert == 3:
            win_comb.append([(i, 0), (i, 3), board[i][0]])

        for j in range(4):
            if board[i][j] == board[i + 1][j] == board[i + 2][j]\
                    == board[i + 3][j] and board[i][j] != '"':
                horiz += 1
                win_comb.append([(i, j), (i + 3, j), board[i][j]])

        if board[i][0] == board[i + 1][1] == board[i + 2][2]\
                == board[i + 3][3] and board[i][0] != '"':
            win_comb.append([(i, 0), (i + 3, 3), board[i][0]])
        if board[i][0] == board[i - 1][1] == board[i - 2][2]\
                == board[i - 3][3] and board[i][0] != '"':
            win_comb.append([(i, 0), (i - 3, 3), board[i][0]])

    if win_comb != []:
        return True, win_comb
    else:
        return False
a = board_generation()
print(winning_combination(a))
print(a)
