# Функция с произвольным числом параметров разного типа.
def test(*args, **kwargs):
    i = 0
    for v in args:
        print(f'{i}: {v}')
        i += 1
    for k, v in kwargs.items():
        print(f'{k}: {v}')


def factorial(n):
    if n == 1 or n == 0:
        return 1
    elif n > 1:
        return n * factorial(n - 1)


# Вызов функции с произвольным числом параметров разного типа.
test('r', {'f': 15, 'y': 'h'}, l=[2, 't', (4, 7)], d={1: 5})

num = ''
while num != 'стоп':
    num = input('Введите целое положительное число для расчёта его факториала или «стоп» для выхода: ')
    if num.isdigit():
        num = int(num)
        print(f'{num}! = ', factorial(num))
    elif num != 'стоп':
        print('Ошибка ввода. Введено не целое положительное число.')
print('Завершение программы.')
