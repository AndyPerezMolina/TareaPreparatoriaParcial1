import psycopg2

def menu():
    print("Menu")
    print("1- Ingresar numero")
    print("2- Consultar base de datos")
    print("3- Borrar base de datos")
    print("4- Salir")
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
        opcion = int(input())
        if opcion == 1:
                print("Ingrese un numero")
                numero = int(input())
                suma = 0
                for i in range(1,numero+1):
                    suma = suma + i
                print("La suma es ",suma,)
                cursor.execute("INSERT INTO sumanumero(numero,suma) VALUES(%s,%s);",(numero,suma))
                conexion.commit()
        elif opcion==2:
            SQL = 'SELECT * FROM sumanumero;'
            cursor.execute(SQL)
            valores = cursor.fetchall()
            print(valores)
        elif opcion==3:
            SQL = 'DELETE FROM sumanumero;'
            cursor.execute(SQL)
            conexion.commit()
            print("Los registros han sido eliminados")
        elif opcion == 4:
            break
    except :
        print("ingrese opcion valida")

cursor.close()
conexion.close()