import psycopg2

def menu():
    print("Menu")
    print("1- Ingresar numeros")
    print("2- Salir")
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

cursor = conexion.cursor()
while True:
    menu()
       
    try :
            opcion = int(input())
            if opcion == 1:
                operacion()  
            elif opcion == 2:
                break
    except :
        print("Debe ingresar una opcion valida")

cursor.close()
conexion.close()