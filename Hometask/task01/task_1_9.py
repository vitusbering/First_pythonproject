import sys

def main():
    #a3
    if( len(sys.argv) == 3 ):
        a = int(sys.argv[1])
        b = int(sys.argv[2])
       
        print(a)
        print(b)
    else:
        print("Пожалуйста укажите парметры переменных 'a' и 'b'")
    
    
if __name__ == "__main__":
    main()
