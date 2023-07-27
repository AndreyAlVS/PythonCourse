# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

input_string = 'a a a b c a a d c d d'
list_1 = input_string.split(' ')
dictionary = {}
final_string = ''
for i in list_1:
    if i in dictionary:
        dictionary[i] += 1
        final_string += f'{i}_{dictionary[i]} '
    else:
        dictionary[i] = 0
        final_string += f'{i} '

print(final_string)