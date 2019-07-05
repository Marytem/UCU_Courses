def sort(lst):
    for i in range(len(lst)):
        crnt = lst.pop(i)
        ins_place = i
        for j in reversed(range(i)):
            if crnt >= lst[j] and lst[j] % 2 == 0:
                ins_place = j + 1
                break
            elif crnt % 2 == 0 and (lst[j] % 2 != 0 or crnt <= lst[j]):
                ins_place = j - 1
            elif crnt % 2 != 0 and crnt <= lst[j]:
                ins_place = j + 1
                break
            elif crnt % 2 != 0 and lst[j] % 2 != 0 and crnt >= lst[j]:
                ins_place = j - 1
        if ins_place < 0:
            ins_place = 0
        lst.insert(ins_place, crnt)
    return lst


