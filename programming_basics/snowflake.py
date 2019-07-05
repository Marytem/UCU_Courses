def is_painted(row, column, k):
    '''
    (int, int, int) -> bool
    return True if mentioned coordinates can be used to draw
    a snowflake on a field k X k and False otherwise.
    >>> is_painted(4, 4, 7)
    False
    '''
    if k % 2  == 1:
        if row == column == round(k/2):
            return False
        elif row == column or row == k + 1 - column:
            return True
        elif row == round(k/2) and column == round(k/2) + 1:
            return True
        elif column == round(k/2) and row == round(k/2) + 1:
            return True
        elif row == round(k/2) and column == round(k/2) - 1:
            return True
        elif column == round(k/2) and row == round(k/2) - 1:
            return True
    else:
        if row == column or row == k + 1 - column:
            return True
print


def draw_snowflake(k):
    '''
    int -> list
    prints a snoflake on a given field and return
    a list of coordinates.
    >>> draw_snowflake(6)
    *    *
     *  *
      **
      **
     *  *
    *    *
    [[1, 1], [6, 1], [2, 2], [5, 2], [3, 3], [4, 3], [3, 4], [4, 4], [2, 5], [5, 5], [1, 6], [6, 6]]
    '''
    coord = []
    for row in range(1, k+1):
        for column in range(1, k+1):
            if is_painted(row, column, k):
                coord.append([column, row])
    for row in range(1, k+1):
        a = ''
        for column in range(1, k+1):
            if is_painted(row, column, k):
                a += '*'
            else:
                a += ' '
        print(a)
    return coord
print(draw_snowflake(13))
