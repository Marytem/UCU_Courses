import random


def students_pair():
    '''
    () -> tuple(str)
    Create a list of pairs of students

    >>> students_pair()
    Type students names, each followed by Enter; or ^D or ^Z to finish
    Annabelle Valentine
    Janice Moore
    Diana Wyatt
    ('Annabelle Valentine', 'Teacher')
    ('Janice Moore', 'Diana Wyatt')

    >>> students_pair()
    Type students names, each followed by Enter; or ^D or ^Z to finish
    Annabelle Valentine
    Janice Moore
    Diana Wyatt
    Neil Maldonado
    ('Annabelle Valentine', 'Janice Moore')
    ('Diana Wyatt', 'Neil Maldonado')
    '''

    def list_input():
        '''
        Return list "init_list" of input students names

        >>> list_input()
        Type students names, each followed by Enter; or ^D or ^Z to finish
        Annabelle Valentine
        Janice Moore
        Diana Wyatt
        '''
        print("Type students names, each followed by Enter; or ^D or ^Z to finish")
        init_list = []
        while True:
            try:
                line = input()
                if line:
                    init_list.append(str(line))
            except ValueError as err:
                print(err)
                continue
            except EOFError:
                break
        return init_list

    def simple_division():
        '''
        (init_list) -> list(tuple(str))

  -------------initial list in two halves.
        Create a list of tuples. Let each tuple contain one item from
        list1 and the other from list2.
        Choose items for each half uniformly at random.

        >>> simple_division()
        [('Janice Moore', 'Annabelle Valentine'), ('Diana Wyatt', 'Neil Maldonado') ]
        '''

        init_list = list_input()
        if len(init_list) % 2 != 0:
            init_list.insert(0, 'teacher')
        list1 = init_list[:len(init_list) // 2]
        list2 = init_list[(len(init_list) // 2):]
        random.shuffle(list1)
        list3 = []
        for i in range(len(list1)):
            list3.append((list1[i], list2[i]))
        return(list3)
    print(simple_division())
students_pair()
