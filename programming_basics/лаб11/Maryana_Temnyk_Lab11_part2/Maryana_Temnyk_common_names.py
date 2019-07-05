# File: Maryana_Temnyk_common_names.py
# A program which gives a set of both male and female names


def names_read(file_name):
    '''
    str -> list

    Return a list of names in a file with a given name.
    '''
    with open(file_name, 'r') as file:
        names = file.read().split('\n')
    return names


def common_names(female_names, male_names):
    '''
    list, list -> set

    Return a set of names, present in both female_names
    and male_names.
    '''
    female_names = set(female_names)
    male_names = set(male_names)
    common_names = female_names.intersection(male_names)
    common_names.discard('')
    return common_names


female_names = names_read('female.txt')
male_names = names_read('male.txt')
print(common_names(female_names, male_names))
