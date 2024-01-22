s = 'affective'
countf = 0
for i in s:
    if i == 'f':
        countf += 1
        if countf == 2:
            print(s.index(i))
            break
            if countf == 1:
                print('1')
            else:
                print('2')