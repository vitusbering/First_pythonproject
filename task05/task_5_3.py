"""Два натуральных числа называют дружественными, если каждое из них
равно сумме всех делителей другого, кроме самого этого числа. Найти все
пары дружественных чисел, лежащих в диапазоне от 200 до 300.
"""

a = {}
for i in range(200,300 + 1):
    summ_of_devidors = 0
    for devider in range(1,i + 1):
        if devider != i and i % devider == 0:
            summ_of_devidors += devider
    if summ_of_devidors in range(200, 300 +1):
        a[i] = summ_of_devidors
# print(a)
# print('*****************************************************')
for i,k in a.items():
    for t,n in a.items():
        if i == n and k == t:
            print(i,k)

