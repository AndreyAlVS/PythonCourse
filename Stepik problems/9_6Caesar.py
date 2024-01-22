n = 1
s = 'bwfusvfupdbftbs'
decode = []
for i in s:
    num = ord(str(i))
    num -= n
    decode.append(num)
for i in decode:
    print(chr(i), end='')
