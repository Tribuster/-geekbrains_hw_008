#   1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
#   В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
#   Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
#   Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
#   Проверить работу полученной структуры на реальных данных.


class Date(object):

    def __init__(self, day=1, month=1, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def type(cls, date):
        day, month, year = map(int, date.split('-'))
        return f"{type(day), day}\n{type(month), month}\n{type(year), year}"

    @staticmethod
    def valid(date):
        day, month, year = map(int, date.split('-'))
        if day <= 31 and day != 0 and month <= 12 and month != 0 and year <= 2022:
            print(date)
            return day, month, year
        else:
            print('Неверная дата')


date_1 = '20-04-2022'
print(Date.type(date_1))
data_1 = Date.valid(date_1)
date_2 = '01-12-2223'
print(Date.type(date_2))
data_2 = Date.valid(date_2)