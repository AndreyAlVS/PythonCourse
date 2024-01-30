# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.


def bubble_sort(arr: list[int]) -> None:
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


numbers = [1, 1001, 50, 2, 900]
bubble_sort(numbers)
print(numbers)
