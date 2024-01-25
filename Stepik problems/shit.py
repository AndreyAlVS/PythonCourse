s = input().split()
square = [int(i) ** 2 for i in s if int(i) % 2 == 0]
square_without_4 = [i for i in square if i % 10 != 4]
print(*square_without_4)
