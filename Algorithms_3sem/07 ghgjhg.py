from copy import deepcopy


def knapsack(items, capacity):
    """
    :param items:  [(value, weight), (value, weight), (value, weight)]
    :param capacity: capacity of the knapsack
    :return: total_value = result value
             result_items = array of indices according to items[]
    """
    lst = [{0: 0}]
    result_items = []
    for value, weight in items:
        curr_dict_copy = deepcopy(lst[-1])
        for key_wght in lst[-1]:

            if key_wght + weight > capacity:
                continue
            if key_wght + weight not in lst[-1]:
                curr_dict_copy[key_wght + weight] = lst[-1][key_wght] + value
            else:
                curr_dict_copy[key_wght + weight] = max(curr_dict_copy[key_wght + weight], lst[-1][key_wght] + value)
        lst.append(curr_dict_copy)

    i = len(items) - 1
    w = capacity
    while i > 0 and w > 0:
        print(lst[i-1][w])
        if :
            result_items.append(i)
            w -= items[i][1]
            i -= 1
        else:
            i -= 1

    total_value = max(lst[-1][key] for key in lst[-1])
    return total_value, result_items


items1 = [[7, 5], [8, 4], [9, 3], [10, 2], [1, 10]]
weight1 = 10
print(knapsack(items1, weight1))  # result 27

items2 = [[7, 5], [8, 4], [9, 3], [10, 2], [1, 10], [3, 15], [8, 10], [6, 4], [5, 3], [7, 3]]
weight2 = 20
print(knapsack(items2, weight2))  # result 46