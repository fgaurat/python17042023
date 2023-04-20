from tkinter import *
from tkinter import ttk
import argparse
import configparser
from TodoDAO import TodoDAO

def main():
    parser = argparse.ArgumentParser(description='TP TKInter DB.')
    parser.add_argument('-config_file',help="Configuration file",default='config.ini')
    args = parser.parse_args()
    
    config = configparser.ConfigParser()
    config.read(args.config_file)

    data_file = config['DB']['data_file']


    root = Tk()
    tree = ttk.Treeview(root,columns=('id','userId','title','completed'),show='headings')
    tree.heading('id',text="#")
    tree.heading('userId',text="User ID")
    tree.heading('title',text="Title")
    tree.heading('completed',text="Done ?")

    for todo in dao.findAll():
        tree.insert("",index=todo.id,values=[todo.id,todo.userId,todo.title,todo.completed])
    
    tree.pack(fill=BOTH,expand=True)
    
    root.mainloop()


def sayHello():
    print("Hello")

def main_hello():
    root = Tk()

    frm = ttk.Frame(root, padding=10)
    frm.grid()
    
    ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    ttk.Button(frm, text="Hello", command=sayHello).grid(column=0, row=1)
    
    root.mainloop()

if __name__ == '__main__':
    main()