"""Ввести строку. Вывести на экран букву, которая находится в середине этой
строки. Также, если эта центральная буква равна первой букве в строке, то создать и
вывести часть строки между первым и последним символами исходной строки.
(подсказка: для получения центральной буквы, найдите длину строки и разделите
ее пополам. Для создания результирующий строки используйте срез)
"""
String = input('Enter a string: ')
StrLength = len(String)
FirstLetter = String[0]
if StrLength % 2 != 0:  # odd
    MidIndex = int(StrLength / 2)
    MidLetter = String[MidIndex]
    print(MidLetter)
    if MidLetter == FirstLetter:
        print(String[1:-1])
    else:
        print('First letter is not found in the middle of the string')
else:  # even
    # Если строка имеет четное количество букв, посредине стоит 2 буквы
    # Если одна из этих букв = 1 букве строки, создать строку между 1 и последним символом исх. строки
    FirstIndex = int(StrLength / 2)-1
    SecondIndex = FirstIndex+1
    MidLetter1 = String[FirstIndex]
    MidLetter2 = String[SecondIndex]
    print(MidLetter1)
    print(MidLetter2)
    if MidLetter1 == FirstLetter or MidLetter2 == FirstLetter:
        print(String[1:-1])
    else:
        print('First letter is not found in the middle of the string')

