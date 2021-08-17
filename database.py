import pymongo 

def connect(url):
    client = pymongo.MongoClient(url)
    return client

# insert todo in database
def insert(client, todo):
    db = client.tododb
    db.tododb.insert(todo)

def edit_todo(client, todo):
    db = client.tododb
    db.tododb.update({'_id': todo['_id']}, {'$set': todo})

def delete_todo(client, todo):
    db = client.tododb
    db.tododb.remove({'_id': todo['_id']})

def mark_todo_completed(client, todo):
    db = client.tododb
    db.tododb.update({'_id': todo['_id']}, {'$set': {'completed': True}})

def get_todos(client):
    db = client.tododb
    todos = db.tododb.find({'completed': False})
    return todos

def get_todo(client, todo_id):
    db = client.tododb
    todo = db.tododb.find_one({'_id': todo_id})
    return todo

def get_todos_by_user(client, user_id):
    db = client.tododb
    todos = db.tododb.find({'user_id': user_id, 'completed': False})
    return todos

def get_todo_by_id(client, todo_id):
    db = client.tododb
    todo = db.tododb.find_one({'_id': todo_id})
    return todo