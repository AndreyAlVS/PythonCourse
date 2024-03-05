# Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату.
from datetime import datetime, date
from task3 import log_decor

MONTHS = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
          'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
DAYS = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']


@log_decor
def string_to_date(s: str) -> datetime:
    weeks, weekday, month = s.split()

    weeks = int(weeks[0])
    y = datetime.now().year
    month_num = MONTHS.index(month) + 1
    weekday = DAYS.index(weekday) + 1
    first_day = date(day=1, month=month_num, year=y).isoweekday()

    day_by_date = ((1 + 7 * weeks - (first_day - weekday))
                   if weekday < first_day else 1 + 7 * (weeks - 1) - (first_day - weekday))

    return datetime(day=day_by_date, month=month_num, year=y)


if __name__ == '__main__':
    print(string_to_date('1-й четверг ноября'))
    print(string_to_date('5-й четверг февраля'))
