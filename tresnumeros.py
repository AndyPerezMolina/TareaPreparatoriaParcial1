import psycopg2

def menu():
    print("Menu")
    print("1- Ingresar numeros")
    print("2- Salir")
    return()

def operaciones():
    print("Ingresar Numero 1")
    num1 = float(input())

    print("Ingresar Numero 2")
    num2 = float(input())

    print("Ingresar Numero 3")
    num3 = float(input())

    if num3==num2==num1:
        resultado = "Todos son Iguales"
        print("Todos los numeros son iguales")
        cursor.execute("INSERT INTO tresnumeros(num1,num2,num3,resultado) VALUES(%s,%s,%s,%s);",(num1,num2,num3,resultado))
        conexion.commit()
    elif num2==num3:
        resultado = num1
        print("El numero",num1,"Es diferente")
        cursor.execute("INSERT INTO tresnumeros(num1,num2,num3,resultado) VALUES(%s,%s,%s,%s);",(num1,num2,num3,resultado))
        conexion.commit()
    elif num1==num2:
        resultado = num3
        print("El numero",num3,"Es diferente")
        cursor.execute("INSERT INTO tresnumeros(num1,num2,num3,resultado) VALUES(%s,%s,%s,%s);",(num1,num2,num3,resultado))
        conexion.commit()
    elif num1==num3:
        resultado = num2
        print("El numero",num2,"Es diferente")
        cursor.execute("INSERT INTO tresnumeros(num1,num2,num3,resultado) VALUES(%s,%s,%s,%s);",(num1,num2,num3,resultado))
        conexion.commit()
    elif num1> (num2 and num3) :
        resultado = num1+num2+num3
        print("La suma es: ",resultado)
        cursor.execute("INSERT INTO tresnumeros(num1,num2,num3,resultado) VALUES(%s,%s,%s,%s);",(num1,num2,num3,resultado))
        conexion.commit()
    elif num2 > (num1 and num3):
        resultado = num1*num2*num3
        print("La multiplicacion es: ",resultado)
        cursor.execute("INSERT INTO tresnumeros(num1,num2,num3,resultado) VALUES(%s,%s,%s,%s);",(num1,num2,num3,resultado))
        conexion.commit()
    elif num3 > (num1 and num2):
        resultado = str(num1)+str(num2)+str(num3)
        print("La concatenacion es {:.0f}".format(num1),"{:.0f}".format(num2),"{:.0f}".format(num3))
        cursor.execute("INSERT INTO tresnumeros(num1,num2,num3,resultado) VALUES(%s,%s,%s,%s);",(num1,num2,num3,resultado))
        conexion.commit()
    return()



conexion = psycopg2.connect(
    host = "localhost",
    port = "5432",
    user = "postgres",
    password = "1234",
    dbname = "tareap1"
)

cursor = conexion.cursor()
while True:
    menu()
       
    try :
            opcion = float(input())
            if opcion == 1:
                operaciones()  
            elif opcion == 2:
                break
    except :
        print("Debe ingresar una opcion valida")

cursor.close()
conexion.close()