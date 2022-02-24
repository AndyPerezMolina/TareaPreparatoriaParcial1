import psycopg2

conexion = psycopg2.connect(
    host = "localhost",
    port = "5432",
    user = "postgres",
    password = "1234",
    dbname = "tareap1"
)

def menu():
    print("Menu")
    print("1- Ingresar Lados")
    print("2- Consultar base de datos")
    print("3- Borrar base de datos")
    print("4- Salir")
    return()

def operaciones():
    print("Ingresar Lado 1")
    num1 = float(input())

    print("Ingresar Lado 2")
    num2 = float(input())

    print("Ingresar Lado 3")
    num3 = float(input())
    if num1<=0 or num2<=0 or num3<=0:
        print("Los lados deben ser positivos mayores a cero")
    else:
        if num3==num2==num1:
            resultado = "Triangulo Equilatero"
            print("El Triangulo es equilatero")
            cursor.execute("INSERT INTO tipotriangulo(lado1,lado2,lado3,tipo) VALUES(%s,%s,%s,%s);",(num1,num2,num3,resultado))
            conexion.commit()
        elif num1==num2 or num2==num3 or num1==num3:
            resultado = "Triangulo Isosceles"
            print("El Triangulo es Isosceles")
            cursor.execute("INSERT INTO tipotriangulo(lado1,lado2,lado3,tipo) VALUES(%s,%s,%s,%s);",(num1,num2,num3,resultado))
            conexion.commit()
        elif num1!=num2 and (num1!=num3) and (num2!=num3):
            resultado = "Triangulo Escaleno"
            print("El Triangulo Es escaleno")
            cursor.execute("INSERT INTO tipotriangulo(lado1,lado2,lado3,tipo) VALUES(%s,%s,%s,%s);",(num1,num2,num3,resultado))
            conexion.commit()
    return()

cursor = conexion.cursor()

while True:
    menu()
       
    try :
            opcion = float(input())
            if opcion == 1:
                operaciones()
            elif opcion==2:
                SQL = 'SELECT * FROM tipotriangulo;'
                cursor.execute(SQL)
                valores = cursor.fetchall()
                print(valores)
            elif opcion==3:
                SQL = 'DELETE FROM tipotriangulo;'
                cursor.execute(SQL)
                conexion.commit()
                print("Los registros han sido eliminados")  
            elif opcion == 4:
                break
    except :
        print("Debe ingresar una opcion valida")


cursor.close()
conexion.close()