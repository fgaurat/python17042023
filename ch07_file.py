import json


def main():
    # Ecriture
    with open("le_fichier.txt","a") as f:
        # f.write("Bonjour\n")
        print("Bonjour",file=f)
    
    # Lecture
    with open("le_fichier.txt","r") as f:
        for line in f:
            print(line.strip())

    with open("le_fichier.txt","r") as f:
        all_lines = [l.strip() for l in f.readlines()]
        print(all_lines)
    
    d = {
        "name":"GAURAT",
        "firstname":"Fred"
    }

    with open("le_fichier.json","w") as f:
        json.dump(d,f)

    with open("le_fichier.json","r") as f:
        data = json.load(f)
        print(data['name'])


if __name__ == '__main__':
    main()