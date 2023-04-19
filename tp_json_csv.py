import json
from pprint import pprint

def main():
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
