import psycopg2

def menu():
    print("Menu")
    print("1- Ingresar Palabra")
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
                print("Ingresar Cadena de Palabras")
                cadena = str(input())
                contador = 0
                for i in range(0,len(cadena)):
                    if cadena[i]=='a' or cadena[i]=='e'or cadena[i]=='i' or cadena[i]=='o' or \
                        cadena[i]=='u' or cadena[i]=='A'or cadena[i]=='E' or cadena[i]=='I' or \
                        cadena[i]=='O'or cadena[i]=='U':
                            contador=contador+1
                print("En la cadena hay ",contador,"Vocales")
                cursor.execute("INSERT INTO conteovocales(cadena,contador) VALUES(%s,%s);",(cadena,contador))
                conexion.commit()
        elif opcion==2:
            SQL = 'SELECT * FROM conteovocales;'
            cursor.execute(SQL)
            valores = cursor.fetchall()
            print(valores)
        elif opcion==3:
            SQL = 'DELETE FROM conteovocales;'
            cursor.execute(SQL)
            conexion.commit()
            print("Los registros han sido eliminados")
        elif opcion == 4:
            break
    except :
        print("ingrese opcion valida.")

cursor.close()
conexion.close()