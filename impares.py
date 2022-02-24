import psycopg2

def menu():
    print("Menu")
    print("1- Iniciar Conteo")
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
                valor= 100
                conteo=0
                for i in range(1,100):
                    if i%2 != 0:
                        print(i)
                        conteo = conteo+1
                        cursor.execute("INSERT INTO impares(valor,resultado) VALUES(%s,%s);",(i,conteo))
                        conexion.commit()
                print("El total de numero impares es: \n",conteo)
                 
        elif opcion==2:
            SQL = 'SELECT * FROM impares;'
            cursor.execute(SQL)
            valores = cursor.fetchall()
            print(valores)
        elif opcion==3:
            SQL = 'DELETE FROM impares;'
            cursor.execute(SQL)
            conexion.commit()
            print("Los registros han sido eliminados")
        elif opcion == 4:
            break
    except :
        print("Debe ingresar una opcion valida")

cursor.close()
conexion.close()