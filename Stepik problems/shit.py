def quick_merge(n: int) -> str:
    s = ''
    for i in range(n):
        a = input()
        s += a + ' '
    lst = s.split()
    list_of_integers = [int(x) for x in lst]
    list_of_integers.sort()
    return ' '.join(str(x) for x in list_of_integers)


num = int(input())
print(quick_merge(num))
