#!/usr/bin/python

import sys

def main ():
    print ('Даны два действительных числа a и b')
    print ('Найти их сумму')
    print ('Найти их разность')
    print ('Найти их произведение')
    print ('')

    if( len(sys.argv) == 3 ):
       
        variableA = int(sys.argv[1])
        variableB = int(sys.argv[2])

        print ("a="+str(variableA))
        print ("b="+str(variableB))
        print ("")

        
        variableC = variableA+variableB
        print ('Cумма: '+ str(variableC))

        variableC = variableA-variableB
        print ('Разность: '+str(variableC))

        variableC =  variableA*variableB
        print ('Произведение: '+str(variableC))

    else:
        
        print ("Пожалуйста укажите два действительных числа 'a' и 'b'")

if __name__ == "__main__":
    main ()
