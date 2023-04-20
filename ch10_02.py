import json
from Todo import Todo
from TodoDAO import TodoDAO

def main():
    dao = TodoDAO("todos_db.db")
    todos = dao.findAll()
    l = list(todos)
    for todo in l:
        print(todo)

def main_insert():
    todos=[]
    with open("todos.json","r") as f:
        todos = json.load(f)
    
    dao = TodoDAO("todos_db.db")
    for todo in todos:
        t = Todo(**todo)
        dao.save(t )
        




if __name__=='__main__':
    main()
