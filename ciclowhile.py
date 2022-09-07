import math
#CICLO MIENTRAS

##DECLARAR LA VARIABOE CENTINELA
#O VARIABLE DE CONTROL
#LA EJECUCION DE MI CICLO

i=0


#MENU DE OPCIONES
#progrmar la estructura del ciclo minetras
print("****MENU*****")
print("1.sumar dos numeros")
print("2.restar dos numeros")
print("3.encontrar la raiz cuadrada de un numero")
print("4.multiplicar 2 numeros")
print("5.salir")

while(i!=5):
    i=int(input("digite una opcion del menu: "))
    
    if(i==1):
        numero= int(input("ingrese el numero 1: "))
        numero2= int(input("ingrese el numero 2: "))
        suma =numero+numero2
        print("la suma es ",suma)

    elif(i==2):
        numero= int(input("ingrese el numero 1: "))
        numero2= int(input("ingrese el numero 2: "))
        resta=numero-numero2
        print("la resta es ",resta)
    elif(i==3):
        numero= int(input("ingrese el numero 1: "))
        raiz= math.sqrt(numero)

        print("la raiz es ",raiz)
    elif(i==4):
        numero= int(input("ingrese el numero 1: "))
        numero2= int(input("ingrese el numero 2: "))
        multipl=numero-numero2
        print("la multi es ",multipl)
        break
    else:
        print("digite una opcion valida")


print("salimos del while")   