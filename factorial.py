from math import factorial
import psycopg2

def menu():
    print("Menu")
    print("1- Ingresar Numero")
    print("2- Consultar base de datos")
    print("3- Borrar base de datos")
    print("4- Salir")
    return()

def operaciones():
    print("Ingresar Numero")
    num1 = int(input())
    if num1%7==0:
        resultado = factorial(num1)
        print(" El Factorial es :",resultado)
        cursor.execute("INSERT INTO factorial(numero,factorial) VALUES(%s,%s);",(num1,resultado))
        conexion.commit()
    else:
        print("El numero no es divisible entre 7")



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
            opcion = int(input())
            if opcion == 1:
                operaciones()
            elif opcion==2:
                SQL = 'SELECT * FROM factorial;'
                cursor.execute(SQL)
                valores = cursor.fetchall()
                print(valores)
            elif opcion==3:
                SQL = 'DELETE FROM factorial;'
                cursor.execute(SQL)
                conexion.commit()
                print("Los registros han sido eliminados")  
            elif opcion == 4:
                break
    except :
        print("Debe ingresar una opcion valida")

cursor.close()
conexion.close()