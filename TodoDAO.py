import sqlite3
from Todo import Todo
from pprint import pprint

class TodoDAO:

    def __init__(self,db_file) -> None:
        self._con = sqlite3.connect(db_file)

    def save(self,todo:Todo):
        sql = f"""INSERT INTO todos_tbl(user_id,title,completed)
VALUES({todo.userId},'{todo.title}',{todo.completed})
"""
        cur = self._con.cursor()
        cur.execute(sql)
        self._con.commit()

    def findAll(self):
        sql ="SELECT * FROM todos_tbl"
        cur = self._con.cursor()
        res = cur.execute(sql)
        data = res.fetchall()
        for id,title,completed,user_id in data:
            t = Todo(id,user_id,title,completed)
            yield t





    def __del__(self):
        self._con.close()

