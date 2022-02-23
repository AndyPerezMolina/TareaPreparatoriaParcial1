

try :
    print("Ingresar Numero 1")
    num1 = float(input())

    print("Ingresar Numero 2")
    num2 = float(input())

    print("Ingresar Numero 3")
    num3 = float(input())

    if num3==num2==num1:
        print("Todos los numeros son iguales")
    elif num2==num3:
        print("El numero",num1,"Es diferente")
    elif num1==num2:
        print("El numero",num3,"Es diferente")
    elif num1==num3:
        print("El numero",num2,"Es diferente") 
      
    elif num1> (num2 and num3) :
        suma = num1+num2+num3
        print("La suma es: ",suma)
    elif num2 > (num1 and num3):
        multiplicacion = num1*num2*num3
        print("La multiplicacion es: ",multiplicacion)
    elif num3 > (num1 and num2):
        print("La concatenacion es {:.0f}".format(num1),"{:.0f}".format(num2),"{:.0f}".format(num3))
except :
    print("Debe ingresar un numero ")
