import psycopg2
from psycopg2 import Error
import os
os.system('cls||clear')

try:
    # Connect to an existing database
    connection = psycopg2.connect(user="postgres",
                                  password="admin",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="Lanchonete")

    # Create a cursor to perform database operations
    cursor = connection.cursor()
    # Executing a SQL query
    print("SELECT")
    cursor.execute("SELECT * FROM cliente;")
    # Fetch result
    sel = cursor.fetchall()
    print(sel, "\n")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
