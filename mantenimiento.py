import psycopg2

def menu():
    print("Menu")
    print("1- Consultar Mantenimiento")
    print("2- Consultar base de datos")
    print("3- Borrar base de datos")
    print("4- Salir")
    return()

def operaciones():
    print("Ingresar Año del taxi")
    modelo = int(input())

    print("Ingresar kilometraje")
    kilometraje = float(input())


    if (modelo<2007) and kilometraje>20000:
        resultado = "Renovarse"
        print("El Taxi debe Renovarse")
        cursor.execute("INSERT INTO mantenimiento(modelo,kilometraje,resultado) VALUES(%s,%s,%s);",(modelo,kilometraje,resultado))
        conexion.commit()
    elif (modelo>=2007)and(modelo<=2013)and (kilometraje==20000):
        resultado = "Mantenimiento"
        print("El Taxi debe recibir mantenimiento")
        cursor.execute("INSERT INTO mantenimiento(modelo,kilometraje,resultado) VALUES(%s,%s,%s);",(modelo,kilometraje,resultado))
        conexion.commit()
    elif (modelo>2013)and(kilometraje<10000):
        resultado = "Optimas Condiciones"
        print("El taxi esta en optimas condiciones")
        cursor.execute("INSERT INTO mantenimiento(modelo,kilometraje,resultado) VALUES(%s,%s,%s);",(modelo,kilometraje,resultado))
        conexion.commit()
    else:
        resultado = "Mecanico"
        print("Mecanico")
        cursor.execute("INSERT INTO mantenimiento(modelo,kilometraje,resultado) VALUES(%s,%s,%s);",(modelo,kilometraje,resultado))
        conexion.commit()
    
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
                operaciones()
            elif opcion==2:
                SQL = 'SELECT * FROM mantenimiento;'
                cursor.execute(SQL)
                valores = cursor.fetchall()
                print(valores)
            elif opcion==3:
                SQL = 'DELETE FROM mantenimiento;'
                cursor.execute(SQL)
                conexion.commit()
                print("Los registros han sido eliminados")  
            elif opcion == 4:
                break
    except :
        print("Debe ingresar una opcion valida")

cursor.close()
conexion.close()