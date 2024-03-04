def diff(lst: list) -> int | float:
    total = 0
    counter = 0
    for i in range(len(lst)):
        for j in lst[i]:
            total += j
    for i in range(len(lst)):
        counter += len(lst[i])
    res = total / counter
    return res


if __name__ == '__main__':
    list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
    print(diff(list1))
