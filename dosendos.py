import psycopg2

def menu():
    print("Menu")
    print("1- Ingresar numeros")
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
                print("Ingresar Inicio")
                inicio = int(input())
                print("Ingresar Final")
                final = int(input())
                conteo = inicio
                for i in range(inicio,final+1,2):
                    print (conteo)
                    conteo = conteo+2
                    cursor.execute("INSERT INTO conteo2(inicio,fin,conteo) VALUES(%s,%s,%s);",(inicio,final,conteo))
                    conexion.commit()
            elif opcion==2:
                SQL = 'SELECT * FROM conteo2;'
                cursor.execute(SQL)
                valores = cursor.fetchall()
                print(valores)
            elif opcion==3:
                SQL = 'DELETE FROM conteo2;'
                cursor.execute(SQL)
                conexion.commit()
                print("Los registros han sido eliminados")
            elif opcion == 4:
                break
    except :
        print("Debe ingresar una opcion valida")

cursor.close()
conexion.close()