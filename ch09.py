from Rectangle import Rectangle
from RectangleProp import RectangleProp
from Carre import Carre

def main():
    r = Rectangle(2,3)
    print(r.calc_surface())

    
def main_old2():
    r = RectangleProp(2,5)
    print(r.longueur)
    r.longueur = 12
    print(r.longueur)
    print(r.surface)
    print(50*"-")
    c = Carre(3)
    print(c.get_cote())
    print(c.surface())
    print(c)


def old_main():
    r = Rectangle(2,5)
    r1 = Rectangle(2,5)
    
    # print("surface",r.surface())
    print(r.get_longueur())
    r.set_longueur(4)
    # print("surface",r.surface())
    # print(r.get_longueur())
    # s = str(r)
    # print(s)

    # if r.__eq__(r1):
    if r==r1:
        print("ok")
    else:
        print("ko")

if __name__=='__main__':
    main()
