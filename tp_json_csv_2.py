import csv
import json
from pprint import pprint
def main():
    with open('todos_2.csv', 'r', newline='') as csvfile:
        reader = list(csv.DictReader(csvfile,delimiter=";",quoting=csv.QUOTE_MINIMAL))
        pprint(reader)

def main_write_csv():
    with open("todos.json") as f:
        todos = json.load(f)
    with open('todos_2.csv', 'w', newline='') as csvfile:
        fieldnames = todos[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,delimiter=";",dialect="excel",quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        writer.writerows(todos)



if __name__=='__main__':
    main()
