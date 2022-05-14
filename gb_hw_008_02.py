#   2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
#   Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве делителя программа должна
#   корректно обработать эту ситуацию и не завершиться с ошибкой.

class Division:
    def __init__(self, first_num, second_num):
        self.f = first_num
        self.s = second_num

    @staticmethod
    def div(first_num, second_num):
        try:
            return (first_num / second_num)
        except:
            return f'Делить на ноль нельзя'


a = Division(5, 20)
print(Division.div(10, 0))
print(Division.div(10, 0.1))
print(a.div(5, 20))