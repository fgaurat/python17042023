import json
from pprint import pprint

def main():
    all_todos = []
    with open("todos.csv","r") as f:
        lines = [line.strip() for line in f.readlines()]
        header = lines[0].split(';')
        rows = lines[1:]
        for row in rows:
            values = row.split(';')
            todo = dict(zip(header,values))
            todo['projects'] = ['project1','project1','project1']
            all_todos.append(todo)

    with open("all_todos.json","w") as f:
        json.dump(all_todos,f,indent=4)

def main_write_csv():
    todos=[]
    with open("todos.json","r") as f:
        todos = json.load(f)
    
    header = todos[0].keys()
    print(*header,sep=";")
    header_2 = ";".join(header) 
    
    with open("todos.csv",'w') as f:
        # print(*header,sep=";",file=f)
        # f.write(header_2+"\n")
        print(header_2,file=f)
   
        for todo in todos:
            values = [str(v) for v in todo.values()]
            line  = ";".join(values) 
            print(line,file=f)
            # print(*todo.values(),sep=";",file=f)

if __name__=='__main__':
    main()
