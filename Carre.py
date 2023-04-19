from Rectangle import Rectangle

class Carre(Rectangle):


    def __init__(self, cote):
        super().__init__(cote, cote)
        self.__cote = cote
    
    def get_cote(self):
        return self.__cote

    def set_cote(self,cote):
        self.__cote = cote
    
    def __str__(self):
        return f"{__class__.__name__} {self.__cote=}"       