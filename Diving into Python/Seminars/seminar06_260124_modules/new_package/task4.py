#  Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

def secrets(ridden: str, answers: [str], counter: int) -> int:
    print(ridden)
    for i in range(counter):
        answer = input('Введите ответ: ')
        if answer in answers:
            return i + 1
    return 0


def test_storage():
    dict_riddle = {
                   'Зимой и летом одним цветом': ['Пальма', 'ёлка', 'крокодил'],
                   "Не лает, не кусает, в дом не пускает": ["замок", "фантомас"],
                   "Сидит дед во сто шуб одед": ["лук", "дед в шубах"],
                   }
    for test_data in dict_riddle.items():
        print(secrets(*test_data, counter=3))


if __name__ == '__main__':
    # print(secrets('Зимой и летом одним цветом', ['Пальма', 'ёлка', 'крокодил'], 3))
    test_storage()
