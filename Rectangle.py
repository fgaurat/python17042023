from CalcGeo import CalcGeo

class Rectangle(CalcGeo):
    
    def __init__(self,longueur,largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self,longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self,largeur):
        self.__largeur = largeur

    def calc_surface(self):
        return self.__longueur*self.__largeur
    
    def __str__(self):
        return f"{__class__.__name__} : {self.__longueur=}, {self.__largeur=}"
    
    def __eq__(self, v):
        return self.__longueur == v.__longueur and self.__largeur == v.__largeur