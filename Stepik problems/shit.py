num_str = '1 2 3 4 5'.split()
num_lst = [int(i) for i in num_str]


if len(num_lst) % 2 == 0:
    for i in range(1, len(num_lst), 2):
        num_lst[i], num_lst[i - 1] = num_lst[i - 1], num_lst[i]
    print(*num_lst)
elif len(num_lst) > 1 and len(num_lst) % 2 != 0:
    for i in range(1, len(num_lst) - 1, 2):
        num_lst[i], num_lst[i - 1] = num_lst[i - 1], num_lst[i]
    print(*num_lst)
elif len(num_lst) == 1:
    print(*num_lst)

# 216 39 87 0 0 1 0
# 39 216 0 87 1 0 0