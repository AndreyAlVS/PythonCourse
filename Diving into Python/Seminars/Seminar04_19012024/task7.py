# Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.

data = {
    "Рога": [42, -73, 12, 85, -15, 2000],
    "Копыта": [45, 25, -100, 22, 1000],
    "Хвосты": [-500, 123, 52, 45, 9300]
}


def is_all_profit(dct: dict) -> bool:
    return all(map(lambda v: sum(v) > 0, dct.values()))   # при помощи map() берём все значения из словоря
    # и лямбдой преобразуем каждое  значения словаря в тру или фолс. all() проверяет, если все знач. тру,
    # то вернёт тру, если хоть одно фолс, вернёт фолс.


print((is_all_profit(data)))
