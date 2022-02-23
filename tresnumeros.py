import psycopg2

try :
    conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "1234",
        dbname = "tareap1"
    )
    print("Conexion exitosa")
    cursor = conexion.cursor()
    print("Ingresar Numero 1")
    num1 = float(input())

    print("Ingresar Numero 2")
    num2 = float(input())

    print("Ingresar Numero 3")
    num3 = float(input())

    if num3==num2==num1:
        resultado = "Todos son Iguales"
        print("Todos los numeros son iguales")
        cursor.execute("INSERT INTO tresnumeros(num1,num2,num3,resultado) VALUES(%s,%s,%s,%s);",(num1,num2,num3,resultado))
        conexion.commit()
    elif num2==num3:
        resultado = num1
        print("El numero",num1,"Es diferente")
        cursor.execute("INSERT INTO tresnumeros(num1,num2,num3,resultado) VALUES(%s,%s,%s,%s);",(num1,num2,num3,resultado))
        conexion.commit()
    elif num1==num2:
        resultado = num3
        print("El numero",num3,"Es diferente")
        cursor.execute("INSERT INTO tresnumeros(num1,num2,num3,resultado) VALUES(%s,%s,%s,%s);",(num1,num2,num3,resultado))
        conexion.commit()
    elif num1==num3:
        resultado = num2
        print("El numero",num2,"Es diferente")
        cursor.execute("INSERT INTO tresnumeros(num1,num2,num3,resultado) VALUES(%s,%s,%s,%s);",(num1,num2,num3,resultado))
        conexion.commit()
    elif num1> (num2 and num3) :
        resultado = num1+num2+num3
        print("La suma es: ",resultado)
        cursor.execute("INSERT INTO tresnumeros(num1,num2,num3,resultado) VALUES(%s,%s,%s,%s);",(num1,num2,num3,resultado))
        conexion.commit()
    elif num2 > (num1 and num3):
        resultado = num1*num2*num3
        print("La multiplicacion es: ",resultado)
        cursor.execute("INSERT INTO tresnumeros(num1,num2,num3,resultado) VALUES(%s,%s,%s,%s);",(num1,num2,num3,resultado))
        conexion.commit()
    elif num3 > (num1 and num2):
        resultado = num3
        print("La concatenacion es {:.0f}".format(num1),"{:.0f}".format(num2),"{:.0f}".format(num3))
        cursor.execute("INSERT INTO tresnumeros(num1,num2,num3,resultado) VALUES(%s,%s,%s,%s);",(num1,num2,num3,resultado))
        conexion.commit()
except psycopg2.Error as e:
    print("Ocurrio un error en la conexion")
    print("verifique los parametros")
    print("Debe ingresar un numero ")

cursor.close()
conexion.close()