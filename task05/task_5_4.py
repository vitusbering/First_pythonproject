"""Для заданного числа N составьте программу вычисления суммы
S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число.
"""
num = int(input('Enter the number grated than 1: '))
if num > 1:
    sum = 1
    for i in range(2, num + 1):
        sum += 1/i
    print('Сумма равна', sum)

