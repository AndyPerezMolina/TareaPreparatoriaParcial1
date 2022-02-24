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
                contadora = 0
                contadore = 0
                contadori = 0
                contadoro = 0
                contadoru = 0
                for i in range(0,len(cadena)):
                    if cadena[i]=='a' or cadena[i]=='A':
                                contadora=contadora+1
                    if cadena[i]=='e' or cadena[i]=='E':
                        contadore = contadore +1
                    if cadena[i]=='i' or cadena[i]=='I':
                        contadori = contadori +1
                    if cadena[i]=='o' or cadena[i]=='O':
                        contadoro = contadoro +1
                    if cadena[i]=='u' or cadena[i]=='U':
                        contadoru = contadoru +1
                print("A= ",contadora)
                print("E= ",contadore)
                print("I= ",contadori)
                print("O= ",contadoro)
                print("O= ",contadoru)
                cursor.execute("INSERT INTO conteovoc(cadena,A,E,I,O,U) VALUES(%s,%s,%s,%s,%s,%s);",(cadena,contadora,contadore,contadori,contadoro,contadoru))
                conexion.commit()
        elif opcion==2:
            SQL = 'SELECT * FROM conteovoc;'
            cursor.execute(SQL)
            valores = cursor.fetchall()
            print(valores)
        elif opcion==3:
            SQL = 'DELETE FROM conteovoc;'
            cursor.execute(SQL)
            conexion.commit()
            print("Los registros han sido eliminados")
        elif opcion == 4:
            break
    except :
        print("Opcion invalida")

cursor.close()
conexion.close()