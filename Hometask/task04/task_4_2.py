# Дан список целых чисел. Подсчитать сколько четных чисел в списке
collection = [1, 2, 3, 4, 5, 6, 8, 10, 12]
index = 0
print('using while loop')
while index < len(collection):
    num1 = collection[index]
    if num1 % 2 == 0:
        print(num1)
    index += 1
# Дан список целых чисел. Подсчитать сколько четных чисел в списке
print('using for loop')
for num2 in collection:
    if num2 % 2 == 0:
        print(num2)


