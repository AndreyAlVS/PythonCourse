A = 61_570_068
B = 1_617_462_603
plus = []
minus = []

for i in range(A, B + 1):
    if i % 2 == 0:
        plus.append(i)
    else:
        minus.append(i)

res = sum(plus) - sum(minus)

print(res)
