def knapsack(items, capacity):
    """
    :param items:  [(value, weight), (value, weight), (value, weight)]
    :param capacity: capacity of the knapsack
    :return: total_value = result value
             result_items = array of indices according to items[]
    """
    previous = [0] * (capacity + 1)
    result_items = []
    for value, weight in items:
        current = previous[:weight]
        for ind in range(weight, capacity+1):
            current.append(max(previous[ind], previous[ind-weight] + value))

            # if items.index([value, weight]) not in result_items and max(previous[item], previous[item-weight] + value) == previous[item]:
            #     result_items.append(items.index([value, weight]))
        # if max(previous[item], previous[item-weight] + value) == previous[item] and previous[-1] != current[-1]:
        # print(previous[idx], previous[idx-weight] + value)
        previous = current
    total_value = previous[-1]
    return total_value, result_items

items1 = [[7, 5], [8, 4], [9, 3], [10, 2], [1, 10]]
weight1 = 10
print(knapsack(items1, weight1))  # result 27

items2 = [[7, 5], [8, 4], [9, 3], [10, 2], [1, 10], [3, 15], [8, 10], [6, 4], [5, 3], [7, 3]]
weight2 = 20
print(knapsack(items2, weight2))  # result 46
