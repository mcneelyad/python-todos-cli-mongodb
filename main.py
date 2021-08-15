from datetime import datetime

from database import *

todos = []

def create_todo():
    """
    Create a new todo.
    """
    todo_title = input("Enter a new item: ")
    new_todo = {
        "id" : len(todos) + 1,
        "title": todo_title,
        "completed": False,
        "date_added": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }
    todos.append(new_todo)

def print_todos():
    """
    Print all todos.
    """
    if len(todos) == 0:
        print("No todos for today.")
    else:
        for todo in todos:
            print("----------------------")
            print("{} - {} - Completed: {}".format(todo["id"], todo["title"], todo["completed"]))
            print("----------------------")
            print(todos)

def edit_todo(todo_id):
    """
    Edit a todo.
    """
    for todo in todos:
        if todo["id"] == todo_id:
            todo["title"] = input("Enter a new title: ")
        else:
            print("No todo found with that id.")

def mark_todo_completed(todo_id):
    """
    Mark a todo as completed.
    """
    for todo in todos:
        if todo["id"] == todo_id:
            todo["completed"] = True
        else: 
            print("No todo found with that id.")
    
def delete_todo(todo_id):
    """
    Delete a todo.
    """
    for todo in todos:
        if todo["id"] == todo_id:
            todos.remove(todo)
            break
        else: 
            print("No todo found with that id.")

def print_menu():
    """
    Print the menu.
    """
    print("""
        1. Create a new todo
        2. Print all todos
        3. Edit a todo
        4. Mark a todo as completed
        5. Delete a todo
        6. Quit
    """)
    

if __name__ == '__main__':
    try:
        while True:
            print_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                create_todo()
            elif choice == "2":
                print_todos()
            elif choice == "3":
                todo_id = int(input("Enter todo id: "))
                edit_todo(todo_id)
            elif choice == "4":
                todo_id = int(input("Enter todo id: "))
                mark_todo_completed(todo_id)
            elif choice == "5":
                todo_id = int(input("Enter todo id: "))
                delete_todo(todo_id)
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")
    except KeyboardInterrupt:
        print("Exiting...")