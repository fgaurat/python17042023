

class RectangleProp:
    
    def __init__(self,longueur,largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    @property
    def longueur(self):
        return self.__longueur
    
    @longueur.setter
    def longueur(self,longueur):
        self.__longueur = longueur
    
    @property
    def largeur(self):
        return self.__largeur
    
    @largeur.setter
    def largeur(self,largeur):
        self.__largeur = largeur
    
    @property
    def surface(self):
        return self.__longueur*self.__largeur
    
    def __str__(self):
        return f"{__class__.__name__} : {self.__longueur=}, {self.__largeur=}"
    
    def __eq__(self, v):
        return self.__longueur == v.__longueur and self.__largeur == v.__largeur