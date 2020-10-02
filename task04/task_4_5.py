"""Составить список чисел Фибоначчи содержащий 15 элементов.
(Подсказка: Числа Фибоначчи - последовательность, в которой первые два числа равны
либо 1 и 1, а каждое последующее число равно сумме двух предыдущих чисел.
Пример: 1, 1, 2, 3, 5, 8, 13, 21, 34... )
"""
fnumb1 = 1
fnumb2 = 1
limit = 15
count = 0
print('while loop')
while count < limit:
    count += 1
    SumFib = fnumb1
    if count > 2:
        SumFib = fnumb1 + fnumb2
    fnumb1 = fnumb2
    fnumb2 = SumFib
    print(fnumb2, end=' ')
print('')

print('for loop')
fnumb1 = 1
fnumb2 = 1
for count in range(limit):
    SumFib = fnumb1
    if count > 1:
        SumFib = fnumb1 + fnumb2
    fnumb1 = fnumb2
    fnumb2 = SumFib
    print(fnumb2, end=' ')
