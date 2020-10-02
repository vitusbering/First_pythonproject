"""Дан список. Создать новый список, сдвинутый на 1 элемент влево
Пример: 1 2 3 4 5 -> 2 3 4 5 1
"""
firstCollection = [1, 2, 3, 4, 5, 6]
newCollection = []
index = 1
print('while loop')
while index < len(firstCollection):
    num = firstCollection[index]
    newCollection.append(num)
    index += 1
newCollection.append(firstCollection[0])
print(newCollection)

print('for loop')
newCollection.clear()
for num in firstCollection:
    newCollection.append(num)
newCollection.pop(0)
newCollection.append(firstCollection[0])
print(newCollection)
