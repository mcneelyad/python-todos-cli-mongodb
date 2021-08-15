import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

# connect to MySQL database
def connect_db():
    connection_open = False
    try:
        with mysql.connect(
            host="localhost",
            user="root",
            password=os.getenv("DB_PASSWORD"),
            database="python_todos"
        ) as connection:
            connection_open = True
    except mysql.Error as e:
        print(e)
    return connection_open, connection

# connect to MySQL database and query all todos
def get_all_todos():
    connection_open, connection = connect_db()
    if connection_open:
        try:
            with connection.cursor(prepared=True) as cursor:
                query = "SELECT * FROM todos"
                cursor.execute(query)
                todos = cursor.fetchall()
                return todos
        except mysql.Error as e:
            print(e)
    return None

#connect to MySQL database and query todos by id
def get_todo_by_id(id):
    connection_open, connection = connect_db()
    if connection_open:
        try:
            with connection.cursor(prepared=True) as cursor:
                query = "SELECT * FROM todos WHERE id = %s"
                cursor.execute(query, (id,))
                todo = cursor.fetchone()
                return todo
        except mysql.Error as e:
            print(e)
    return None

#connect to MySQL database and insert a new todo
def insert_todo(todo):
    connection_open, connection = connect_db()
    if connection_open:
        try:
            with connection.cursor(prepared=True) as cursor:
                query = "INSERT INTO todos (title, description, status) VALUES (%s, %s, %s)"
                cursor.execute(query, (todo['title'],))
                connection.commit()
                return True
        except mysql.Error as e:
            print(e)
    return False
