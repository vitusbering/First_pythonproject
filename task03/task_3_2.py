"""
В семье N свадьба. Они решили выбрать заведение, где будут праздновать в
зависимости от количества людей, которое прибудет к утру.
Если их будет больше 50 - закажут ресторан, если от 20 до 50 -то кафе, а если
меньше 20 то отпраздную дома.
Вывести "ресторан", "кафе", "дом" в зависимости от количества гостей (прочитать
переменную с консоли)
"""
guests = int(input('Enter number of quests: '))
if guests > 50:
    print('restaurant')
elif 20 <= guests <= 50:
    print('cafe')
elif guests > 0:
    print('celebrate at home')
else:
    print('celebrate at home without guests')
