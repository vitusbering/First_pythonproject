import sys

def main():
    #(x-y)/(1+(x*y))
    print ('Даны действительные числа X и Y. Найти (x-y)/(1+(x*y))')
    if( len(sys.argv) == 3 ):
        x=int(sys.argv[1])
        y=int(sys.argv[2])
        #(x-y)
        print ('X='+str(x))
        print ('Y='+str(y))
        a=x-y
        b=x*y
        c=1+b
        d=a/c
        
        print('Результат: '+str(d))
        
    else:

        print("Пожалуйста укажите парметры переменных 'X' и 'Y'")
    
if __name__ == "__main__":
    main()
