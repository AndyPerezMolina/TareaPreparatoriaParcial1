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
                print("Ingresar Numero 1")
                valor1 = int(input())
                print("Ingresar Numero 2")
                valor2 = int(input())
                if valor1 > valor2:
                    conteo = valor1+1
                    for i in range(valor2,valor1+1):
                        conteo = conteo-1
                        print("---------")
                        print (conteo)
                        cursor.execute("INSERT INTO conteomayor(valor1,valor2,conteo) VALUES(%s,%s,%s);",(valor1,valor2,conteo))
                        conexion.commit()
                elif valor2 > valor1:
                    conteo = valor2+1
                    for i in range(valor1,valor2+1):
                        conteo = conteo-1
                        print("---------")
                        print (conteo)
                        cursor.execute("INSERT INTO conteomayor(valor1,valor2,conteo) VALUES(%s,%s,%s);",(valor1,valor2,conteo))
                        conexion.commit()
            elif opcion==2:
                SQL = 'SELECT * FROM conteomayor;'
                cursor.execute(SQL)
                valores = cursor.fetchall()
                print(valores)
            elif opcion==3:
                SQL = 'DELETE FROM conteomayor;'
                cursor.execute(SQL)
                conexion.commit()
                print("Los registros han sido eliminados")
            elif opcion == 4:
                break
    except :
        print("Debe ingresar una opcion valida")

cursor.close()
conexion.close()