"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime, timedelta

def print_days():
    today = datetime.today()
    print(today)

    yesterday = today - timedelta(days=1)
    print(yesterday)

    yesterday_30 = today - timedelta(days=30)
    print(yesterday_30)



def str_2_datetime(date_string):
    date_dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
    return date_dt

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
