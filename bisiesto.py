import calendar
import psycopg2

def menu():
    print("Menu")
    print("1- Ingresar Año")
    print("2- Consultar base de datos")
    print("3- Borrar base de datos")
    print("4- Salir")
    return()

def operaciones():
    print("Ingresar Año")
    an = int(input())
    resultado =""
    if calendar.isleap(an) == False :
        resultado = "No Es bisiesto"
        print(" El año :",an,"No es bisiesto")
        cursor.execute("INSERT INTO bisiesto(year,resultado) VALUES(%s,%s);",(an,resultado))
        conexion.commit()
    else:
        resultado = "Si Es bisiesto"
        print(" El año :",an,"Si es bisiesto")
        cursor.execute("INSERT INTO bisiesto(year,resultado) VALUES(%s,%s);",(an,resultado))
        conexion.commit()



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
                SQL = 'SELECT * FROM bisiesto;'
                cursor.execute(SQL)
                valores = cursor.fetchall()
                print(valores)
            elif opcion==3:
                SQL = 'DELETE FROM bisiesto;'
                cursor.execute(SQL)
                conexion.commit()
                print("Los registros han sido eliminados")  
            elif opcion == 4:
                break
    except :
        print("Debe ingresar una opcion valida")

cursor.close()
conexion.close()