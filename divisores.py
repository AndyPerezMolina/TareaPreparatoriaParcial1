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


def operacion():
    print("Ingresar Numero")
    valor = int(input())

    for i in range(1,valor+1):
        if valor % i == 0:
            print (i)
            cursor.execute("INSERT INTO divisores(valor,resultado) VALUES(%s,%s);",(valor,i))
            conexion.commit() 

cursor = conexion.cursor()
while True:
    menu()
       
    try :
            opcion = int(input())
            if opcion == 1:
                operacion()
            elif opcion==2:
                SQL = 'SELECT * FROM divisores;'
                cursor.execute(SQL)
                valores = cursor.fetchall()
                print(valores)
            elif opcion==3:
                SQL = 'DELETE FROM divisores;'
                cursor.execute(SQL)
                conexion.commit()
                print("Los registros han sido eliminados")
            elif opcion == 4:
                print("Vuelva pronto")
                break
    except :
        print("Debe ingresar una opcion valida")

cursor.close()
conexion.close()