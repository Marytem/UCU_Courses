def read_ratings():
    '''
    returns a dictionary, where keys are films, and values are their ratings
    '''
    with open('ratings.list', encoding = 'utf-8',  errors='ignore') as f:
        ratings = f.readline()
        while not ratings.startswith('MOVIE RATINGS REPORT'):
            ratings = f.readline()
        lst = []
        while not ratings.startswith('----------------'):
            ratings = f.readline().strip()
            lst.append(ratings)
        lst = list(map(lambda x: x.split('  '), lst))
        rat_dict = dict(list(map(lambda x: (x[-1],x[-2]) , lst[2:-2])))
    return rat_dict


def read_composers():
    '''
    returns a dictionary, where keys are composers, and values are films
    with their music
    '''
    with open('composers.list', encoding='utf-8', errors='ignore' ) as f:
        data = f.read().split('\n\n')
        begin_compos = data.index("'Abd al-Samad, 'Abd al-Basit\tPrivilege (2002)")
        end_compos = data.index(' Heygum, Heidrik\tTimerne med Christine (2013)')
        composers = data[(begin_compos - 1):(end_compos + 1)]
        composers = list(map(lambda x: x.replace('\n', '').strip().split('\t'), composers))
        comp_dict = dict(list(map(lambda x: (x[0], set(x[1:])), composers)))
        return comp_dict


def data_analisys():
    '''
    returns a dictionary, where keys are composers, and values
    are their scores
    '''
    comp_dct = read_composers()
    rating_dct = read_ratings()
    comp_rating_dct = {}
    for comp in comp_dct:
        comp_score = 0
        for film in comp_dct[comp]:
            try:
                if film in rating_dct:
                    comp_score += eval(rating_dct[film])
            except SyntaxError:
                continue
            except NameError:
                continue
        comp_rating_dct[comp] = comp_score
    return comp_rating_dct


def print_results():
    '''
    prints the results of calculations
    '''
    try:
        num = input("enter how much of the list the program must print")

    except ValueError as err:
        print(err)
    composers_rating_dct = data_analisys()
    dct_for_printing = composers_rating_dct.copy()
    for i in range(int(num)):
        best_comp = max(dct_for_printing, key=lambda x: dct_for_printing[x])
        print(best_comp, composers_rating_dct[best_comp])
        del dct_for_printing[best_comp]


print_results ( )
