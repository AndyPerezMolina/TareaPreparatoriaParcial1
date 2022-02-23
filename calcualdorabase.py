import psycopg2
from decimal import DivisionByZero

def suma():
    operacion="Suma"
    print("Ingrese el primer numero")
    valor1=float(input())
    print("Ingrese el segundo numero")
    valor2=float(input())
    resultado=valor1+valor2
    print("El resultado es", resultado)
    cursor.execute("INSERT INTO datos(operacion,valor1,valor2,resultado) VALUES(%s,%s,%s,%s);",(operacion,valor1,valor2,resultado))
    conexion.commit()
    return()

def resta():
    operacion="Resta"
    print("Ingrese el primer numero")
    valor1=float(input())
    print("Ingrese el segundo numero")
    valor2=float(input())
    resultado=valor1-valor2
    print("El resultado es", resultado)
    cursor.execute("INSERT INTO datos(operacion,valor1,valor2,resultado) VALUES(%s,%s,%s,%s);",(operacion,valor1,valor2,resultado))
    conexion.commit()
    return()

def multiplicacion():
    operacion="Multiplicacion"
    print("Ingrese el primer numero")
    valor1=float(input())
    print("Ingrese el segundo numero")
    valor2=float(input())
    resultado=valor1*valor2
    print("El resultado es", resultado)
    cursor.execute("INSERT INTO datos(operacion,valor1,valor2,resultado) VALUES(%s,%s,%s,%s);",(operacion,valor1,valor2,resultado))
    conexion.commit()
    return()

def division():
    
    try:
        operacion="Division"
        print("Ingrese el primer numero")
        valor1=float(input())
        print("Ingrese el segundo numero")
        valor2=float(input())
        resultado=valor1/valor2
        print("El resultado es", resultado)
        cursor.execute("INSERT INTO datos(operacion,valor1,valor2,resultado) VALUES(%s,%s,%s,%s);",(operacion,valor1,valor2,resultado))
        conexion.commit()
    except:
        DivisionByZero
        print("No se puede realizar la division por cero, intente de nuevo")   
    return()

def potencia():
    operacion="Potencia"
    print("Ingrese la base")
    valor1=float(input())
    print("Ingrese el exponente")
    valor2=float(input())
    resultado=valor1**valor2 
    print("El resultado es", resultado)
    cursor.execute("INSERT INTO datos(operacion,valor1,valor2,resultado) VALUES(%s,%s,%s,%s);",(operacion,valor1,valor2,resultado))
    conexion.commit()
    return()

def raiz():
    operacion="Raiz"
    print("Ingrese el indice de la raiz")
    valor2=float(input())
    print("Ingrese el numero al cual desea calcular la raiz")
    valor1=float(input())
    resultado=valor1**(1/valor2)
    print("El resultado es", resultado)
    cursor.execute("INSERT INTO datos(operacion,valor1,valor2,resultado) VALUES(%s,%s,%s,%s);",(operacion,valor1,valor2,resultado))
    conexion.commit()
        
    return()

def menu():
    print("Menu de opciones")
    print("1- Suma")
    print("2- Resta")
    print("3- Multiplicacion")
    print("4- Division")
    print("5- Potencia")
    print("6- Raiz")
    print("7- Consultar la base de datos")
    print("8- Borrar datos")
    print("9- Salir")

try:
    conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "1234",
        dbname = "calculadora"
    )
    print("Conexion exitosa") 
except psycopg2.Error as e:
    print("Ocurrio un error en la conexion")
    print("verifique los parametros")

cursor = conexion.cursor()

while True:
    menu()
    try:
        opcion=int(input())  
        if opcion==1:
            suma()
        elif opcion==2:
            resta()
        elif opcion==3:
            multiplicacion()
        elif opcion==4:
            division()
        elif opcion==5:
            potencia()
        elif opcion==6:
            raiz()
        elif opcion==7:
            SQL = 'SELECT * FROM datos;'
            cursor.execute(SQL)
            valores = cursor.fetchall()
            print(valores)
        elif opcion==8:
            SQL = 'DELETE FROM datos;'
            cursor.execute(SQL)
            conexion.commit()
            print("Los registros han sido eliminados")
        elif opcion==9:
            print("vuelva pronto")
            break
        else:
            print("Coloque una opcion del menu")
    except:
        print("Debes ingresar una opcion valida")


cursor.close()
conexion.close()