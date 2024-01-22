# Необходимо написать программу для автоматического перевода различных валютных счетов в рублевые.
# Начальные данные программы это три различных списка - Фамилии владельцев банковских счетов,
# указание валют счетов, соответствующее состояние счетов. То есть у Иголкина счет в евро и
# там лежит 50000, и так далее.
# Также вначале заданы отношения курса рубля к доллару и евро.
#
# surnames = ["Иванов", "Карпов", "Иголкин"]
# currency_name = ["рубль", "доллар", "евро"]
# balances = [30000, 40000, 50000]
# dollar = 90
# euro = 99
#
# Вам необходимо написать функцию calc, которая на входе принимает только один аргумент,
# далее надо применить ее в комбинациях с map и zip.
#
#  На выходе программы должны быть три пары значений - фамилии владельцев счетов
#     и состояние рублевого счета.
"""

def calc(currency, balance):
    if currency == "рубль":
        return balance
    elif currency == "доллар":
        return balance * dollar
    elif currency == "евро":
        return balance * euro

surnames = ["Иванов", "Карпов", "Иголкин"]
currency_name = ["рубль", "доллар", "евро"]
balances = [30000, 40000, 50000]
dollar = 90
euro = 99

result = list(map(calc, currency_name, balances))
print(result)
print()
output = list(zip(surnames, result))

for surname, balance in output:
    print(surname, ":", balance, "рублей")


#                           second way
"""


def calc(currency, balance):
    if currency == "рубль":
        return balance
    elif currency == "доллар":
        return balance * dollar
    elif currency == "евро":
        return balance * euro


surnames = ["Иванов", "Карпов", "Иголкин"]
currency_name = ["рубль", "доллар", "евро"]
balances = [30000, 40000, 50000]
dollar = 90
euro = 99


result = [(surname, calc(currency, balance)) for surname, currency, balance in zip(surnames, currency_name, balances)]

for surname, balance in result:
    print(surname, ":", balance, "рублей")
