def factorial(n):
    if n == 1:
        return 1
    elif n > 1:
        return n * factorial(n - 1)


num = ''
while num != 'стоп':
    num = input('Введите целое положительное число для расчёта его факториала или «стоп» для выхода: ')
    if num.isdigit():
        num = int(num)
        if num == 0:
            print(f'Ошибка ввода. Введено не положительное число ({num}). 0! = 1')
        else:
            print(factorial(num))
    elif num != 'стоп':
        print('Ошибка ввода. Введено не целое положительное число.')
print('Завершение программы.')
