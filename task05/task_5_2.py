# Дано число. Найти сумму и произведение его цифр
num = int(input('Enter the number grated than 1: '))
if num > 1:
    sum = 1
    pr = 1
    for i in range(2, num + 1):
        sum += i
        pr *= i
    print('Сумма равна', sum)
    print('Произведение равно', pr)



