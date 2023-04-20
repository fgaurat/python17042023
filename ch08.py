import traceback


class DivBy12Error(Exception):

    def __init__(self):
        super().__init__("Erreur Division par 12 !")


def div(a,b):
    if b==12:
        raise DivBy12Error()
    return a/b

def call_div(a,b):
    try:
        result = div(a,b)
    finally:
        print("LOG")
    return result


def main():
    try:
        a=2
        b=int(input("b :"))
        c = call_div(a,b)
        print(c)
    except ZeroDivisionError as e:
        print("Erreur !",e)
        traceback.print_exc()
    except TypeError as e:
        print("Erreur !",e)
        traceback.print_exc()
    except ValueError as e:
        print("Erreur !",e)
        traceback.print_exc()
    except DivBy12Error as e:
        print("DivBy12Error !",e)
        traceback.print_exc()

    except Exception as e:
        print("Erreur !",e)
        traceback.print_exc()
        
    else:
        print("else")

    print("après les erreurs")

    
if __name__=='__main__':
    main()
