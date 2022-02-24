import psycopg2

def menu():
    print("Menu")
    print("1- Ingresar Notas")
    print("2- Consultar base de datos")
    print("3- Borrar base de datos")
    print("4- Salir")
    return()

def operaciones():
    print("Ingresar Numero 1")
    num1 = float(input())

    print("Ingresar Numero 2")
    num2 = float(input())

    print("Ingresar Numero 3")
    num3 = float(input())
    if num1<0 or num2<0 or num3<0:
        print("no se aceptan notas negativas")
    else:
        if ((num1+num2+num3)/3)>=60:
            estado = "Aprobado"
            resultado = (num1+num2+num3)/3
            print(estado," El Promedio es :",resultado)
            cursor.execute("INSERT INTO promedio(nota1,nota2,nota3,promedio,estado) VALUES(%s,%s,%s,%s,%s);",(num1,num2,num3,resultado,estado))
            conexion.commit()
        else:
            estado="No Aprobado"
            resultado = (num1+num2+num3)/3
            print(estado," El Promedio es :",resultado)
            cursor.execute("INSERT INTO promedio(nota1,nota2,nota3,promedio,estado) VALUES(%s,%s,%s,%s,%s);",(num1,num2,num3,resultado,estado))
            conexion.commit()




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
                operaciones()
            elif opcion==2:
                SQL = 'SELECT * FROM promedio;'
                cursor.execute(SQL)
                valores = cursor.fetchall()
                print(valores)
            elif opcion==3:
                SQL = 'DELETE FROM promedio;'
                cursor.execute(SQL)
                conexion.commit()
                print("Los registros han sido eliminados")  
            elif opcion == 4:
                break
    except :
        print("Debe ingresar una opcion valida")

cursor.close()
conexion.close()