# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии.


def bonus_calc(name: list[str], salary: list[int], bonus: list[str]) -> dict[str, float]:
    res = {}
    for name, salary, bonus in zip(name, salary, bonus):   # zip сливает три списка
        res[name] = round(salary * float(bonus.replace("%", "")) / 100, 2)
    return res


if __name__ == '__main__':
    names = ['Ivanov', 'Petrov', 'Sidorov']
    sal = [100_000, 105_000, 98_000]
    bonus_percent = ['10.25%', '11.46%', '9.85%']
    f = bonus_calc(names, sal, bonus_percent)
    print(f)
