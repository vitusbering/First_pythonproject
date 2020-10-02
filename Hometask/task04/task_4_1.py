"""Дан список целых чисел. Создать новый список, каждый элемент которого равен исходному элементу
умноженному на - (минус) 2
"""
firstCollection = [-3, -2, -1, 0, 1, 2, 3]
secondCollection = []
print('using for loop')
for num in firstCollection:
    newNumber = num * -2
    secondCollection.append(newNumber)
print(secondCollection)

print('using while loop')
secondCollection.clear()
index = 0
while index < len(firstCollection):
    num = firstCollection[index]
    newNumber = num * -2
    secondCollection.append(newNumber)
    index += 1
print(secondCollection)
