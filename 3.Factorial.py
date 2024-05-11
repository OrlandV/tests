def factorial(n):
    if n == 1 or n == 0:
        return 1
    elif n > 1:
        return n * factorial(n - 1)


num = ''
while num != 'стоп':
    num = input('Введите целое положительное число для расчёта его факториала или «стоп» для выхода: ')
    if num.isdigit():
        num = int(num)
        print(f'{num}! = ', factorial(num))
    elif num != 'стоп':
        print('Ошибка ввода. Введено не целое положительное число.')
print('Завершение программы.')
