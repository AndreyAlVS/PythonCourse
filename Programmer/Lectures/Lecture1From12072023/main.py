  кому  Все
list_of_dicts = [{"V": "S001"},
                 {"V": "S002"},
                 {"VI": "S001"},
                 {"VI": "S005"},
                 {"VII": "S005"},
                 {" V ": "S009"},
                 {" VIII ": "S007"}]
uniq_el = set()
for i in list_of_dicts:
    for key in i:
        element = i[key]
        uniq_el.add(element)
print(uniq_el)
nums = [1, 2, 3, 1, 2]
count = 0
for i in range(0, len(nums)):
    if nums[i - 1] < nums[i]:
        count += 1
print(count)

Николай Гаврилов  кому  Все 11:22
import random
length = int(input('Set the length of your sequence:'))
list_of_numbers = []
i = 0
for i in range(length):
    list_of_numbers.append(int(input(f'Input number {i}: ')))
print(list_of_numbers)

count = 0
for i in range(length):
    temp_1 = list_of_numbers[i]
    temp_2 = list_of_numbers[i+1]
    if list_of_numbers[i] > list_of_numbers[i+1]:
        count +=1
        print (f"{temp_2} < {temp_1}")
print(f"Result: {count} counts" )

        
print (f"There are {count} different numbers in your list!")
# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

import random
length = int(input('Set the length of your sequence:'))
list_of_numbers = []
i = 0
for i in range(length):
    list_of_numbers.append(int(input(f'Input number {i}: ')))
print(list_of_numbers)

count = 0
for i in range(length-1):
    temp_1 = list_of_numbers[i]
    temp_2 = list_of_numbers[i+1]
    if list_of_numbers[i] < list_of_numbers[i+1]:
        count +=1
        print (f"{temp_1} < {temp_2}")
print(f"Result: {count} counts" )

        
print (f"There are {count} different numbers in your list!")

while list_number != 0:
    last_digit =list_number[i]%10
    if last_digit == number_to_check:
        count += 1

# Задача №21. 
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}


list_of_dicts = [{"V": "S001"},
                 {"V": "S002"},
                 {"VI": "S001"},
                 {"VI": "S005"},
                 {"VII": " S005 "},
                 {" V ": " S009 "},
                 {" VIII ": " S007 "}]
uniq_el = set()
for i in list_of_dicts:
    for key in i:
        element = i[key].strip(" ")
        uniq_el.add(element)
print(uniq_el)