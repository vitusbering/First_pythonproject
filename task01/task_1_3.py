import sys

def HasInternetConnection():
    return "test"

def main():

    print ('Задача: Дана длина ребра куба')
    print ('Найти объем куба')
    print ('Найти площадь боковой поверхности')

    


    s=10
    if( HasInternetConnection() == "Test" ):
        s= 100


    print("Internet connection "+str(s))
        
    if( len(sys.argv) == 2 ):
        print (sys.argv[0] )
        a=int(sys.argv[1])
        print ('Длина ребра куба ='+str(a))
        c=a**3
        print('Обьем куба:'+str(c))
        c=a**2
        c*=6
        print ('Площадь боковой поверхности:'+str(c))
    else:
        print ('Пожалуйста укажите длину ребра')
    

    
if __name__ == "__main__":
    main()

