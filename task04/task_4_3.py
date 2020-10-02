"""Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’:
‘value’}). Чтобы получить список ключей - использовать метод .keys()
"""
original_collection = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
b = second_collection
index = 0
keys = list(original_collection.keys())
while index < len(keys):
    key = keys[index]
    original_collection[key + str(len(key))] = original_collection[key]
    del original_collection[key]
    index += 1
print(original_collection)

original_collection = b
for key in b:
    b[key + str(len(key))] = b[key]
    del b[key]
    index += 1
print(b)








