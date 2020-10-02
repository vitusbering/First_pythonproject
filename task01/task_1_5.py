from math import hypot
import sys

def main():
    #a3
    print ('Задача: Даны катеты прямоугольного треугольника. Найти гипотенузу и площадь треугольника.')
    if( len(sys.argv) == 3 ):
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        print ('Первый катет ='+str(a))
        print ('Второй катет ='+str(b))
        c = (a*b)/2
        print ('Гипотенуза треугольника ='+str(c))

        x =hypot(a,b)
        print('Площадь треугольника ='+str(x))
        
    else:
        print("Пожалуйста укажите длину катетов 'a' и 'b'")
    

    
if __name__ == "__main__":
    main()

    





