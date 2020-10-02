"""Ввести строку. Если длина строки больше 10 символов, то создать новую
строку с 3 восклицательными знаками в конце ('!!!') и вывести на экран.
Если меньше 10, то вывести на экран второй символ строки
"""
String = input('Enter a string: ')
StrLength = len(String)
if StrLength > 10:
    NewString = String + '!!!'
    print(NewString)
elif 1 < StrLength < 10:
    print(String[1])
else:
    print ('your string has to be more than 1 symbol' )
