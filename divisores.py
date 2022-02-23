import psycopg2



conexion = psycopg2.connect(
    host = "localhost",
    port = "5432",
    user = "postgres",
    password = "1234",
    dbname = "tareap1"
)



print("Ingresar Numero")
valor = float(input())
