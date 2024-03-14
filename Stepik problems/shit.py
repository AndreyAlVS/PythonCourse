n = 5
k = 2
l = []

for i in range(1, n + 1):
    l.append(i)
for _ in l:
    while len(l) != 1:
        l.remove(l[k - 1])
print(*l)
