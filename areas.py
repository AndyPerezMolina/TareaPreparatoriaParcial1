from cmath import pi
import psycopg2

def menu():
    print("Menu")
    print("1- Area Circulo")
    print("2- Area Triangulo")
    print("3- Area Cuadrado")
    print("4- Area Rectangulo")
    print("5- Consultar base de datos")
    print("6- Borrar base de datos")
    print("7- Salir")
    return()

conexion = psycopg2.connect(
    host = "localhost",
    port = "5432",
    user = "postgres",
    password = "1234",
    dbname = "tareap1"
)


def circulo():
    figura="Circulo"
    print("Ingresar Radio")
    radio=float(input())
    if radio >=0:
        area=2*pi*radio
        print("El area es: \n",area)
        cursor.execute("INSERT INTO areas(figura,area) VALUES(%s,%s);",(figura,area))
        conexion.commit() 
    else:
        print("No Se aceptan Valores Negativos")
    return()

def triangulo():
    figura="Triangulo"
    print("Ingrese Base")
    base=float(input())
    print("Ingrese Altura")
    altura = float(input())
    if base <=0 or altura<=0:
        print("No Se aceptan Valores Negativos")
    else:
        area=0.5*base*altura
        print("El area es: \n",area)
        cursor.execute("INSERT INTO areas(figura,area) VALUES(%s,%s);",(figura,area))
        conexion.commit()
       
    return()

def cuadrado():
    figura="Cuadrado"
    print("Ingrese Lado")
    lado=float(input())
    if lado >=0:
        area=lado**2
        print("El area es: \n",area)
        cursor.execute("INSERT INTO areas(figura,area) VALUES(%s,%s);",(figura,area))
        conexion.commit() 
    else:
        print("No Se aceptan Valores Negativos")
    return()

def rectangulo():
    figura="Rectangulo"
    print("Ingrese Ancho")
    ancho=float(input())
    print("Ingrese Altura")
    altura = float(input())
    if ancho <=0 or altura<=0:
       print("No Se aceptan Valores Negativos")  
    else:
        area=ancho*altura
        print("El area es: \n",area)
        cursor.execute("INSERT INTO areas(figura,area) VALUES(%s,%s);",(figura,area))
        conexion.commit()
    return()

cursor = conexion.cursor()
while True:
    menu()
       
    try :
        opcion = int(input())
        if opcion == 1:
            circulo()
        elif opcion==2:
            triangulo()
        elif opcion==3:
            cuadrado()
        elif opcion==4:
            rectangulo()
        elif opcion==5:
            SQL = 'SELECT * FROM areas;'
            cursor.execute(SQL)
            valores = cursor.fetchall()
            print(valores)
        elif opcion==6:
            SQL = 'DELETE FROM areas;'
            cursor.execute(SQL)
            conexion.commit()
            print("Los registros han sido eliminados")
        elif opcion == 7:
            break
    except :
        print("Debe ingresar una opcion valida")

cursor.close()
conexion.close()