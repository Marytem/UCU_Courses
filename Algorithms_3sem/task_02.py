def count_inversions(table, user_num):
    """
    sets users list of films by given marks
    and evaluates invs for every other user
    then sorts them by inv_num

    #return invresions : [[usernum, invnum], [] , []] sorted by inv_num
    """
    user_invs = []
    main_rating = table[user_num]
    for user in table:
        if user is table[user_num]:
            continue
        rating = set_order(main_rating, user)
        invs = count_inv(rating)
        user_invs.append([table.index(user), invs[1]])
        user_invs.sort(key=lambda x: x[1])
    return user_invs


def set_order(main_lst, lst_to_set):
    """
    takes the order of a main user and makes
    other user's list ready for finding invs
    deletes a mark from both lists if user haven't seen the film
    """
    rating = []
    for film_num in range(len(main_lst)):
        if main_lst[film_num] == 0 or lst_to_set[film_num] == 0:
            main_lst.pop(film_num)
            lst_to_set.pop(film_num)
        rating.append(lst_to_set[main_lst.index(film_num + 1)])
    return rating


def count_inv(rating):
    """
    takes a ready list and
    returns inv_num for user
    """
    div_index = int(len(rating)/2)
    if len(rating) > 1:
        (left, num_of_left) = count_inv(rating[:div_index])
        (right, num_of_right) = count_inv(rating[div_index:])
        (rating, num_of_splitted) = count_splitted(left, right)
        inversions_num = num_of_left + num_of_right + num_of_splitted
        return rating, inversions_num
    else:
        return rating, 0


def count_splitted(L_lst, R_lst):
    """
    merges R and L & finds splitted inverses in them
    """
    merged = []
    spl_invs = 0
    i = j = 0

    while i < len(L_lst) and j < len(R_lst):
        if L_lst[i] < R_lst[j]:
            merged.append(L_lst[i])
            i += 1
        else:
            merged.append(R_lst[j])
            j += 1
            spl_invs += len(L_lst) - i
    return merged + L_lst[i:] + R_lst[j:], spl_invs




table = [[3, 2, 10, 6, 9, 1, 5, 7, 4, 8],
         [2, 10, 8, 9, 5, 4, 3, 7, 6, 1],
         [2, 4, 9, 6, 10, 7, 5, 1, 3, 8],
         [3, 9, 10, 6, 7, 4, 1, 2, 5, 8],
         [7, 3, 8, 6, 5, 4, 10, 1, 2, 9]]

print(count_inversions(table, 1))
