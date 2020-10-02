from math import sqrt
import sys

def main():
    
    print ('Даны два действительных числа a и b')
    print ('Найти их среднеарифметическое число')
    print ('Найти их среднегеометрическое число')
    print ('')
    
    if( len(sys.argv) == 3 ):
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        print ('Действительное число a: ' +str(a))
        print ('Действительное число b: ' +str(b))
        c = (a+b)/2
        print ('Среднеарифметическое число: '+str(c))

        x = sqrt(a * b)
        print ('Среднегеометрическое число: '+str(x))
    else:
        print("Пожалуйста укажите два действительных числа 'a' и 'b'")


    
if __name__ == "__main__":
    main()
