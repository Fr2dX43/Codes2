from math import pi


class circle: #classer
    def __init__(self, radie:int) -> None: #function
        self.__radius = radie
    
    def Area(self): #function
        return pi * self.__radius ** 2
        
    def Circumference(self): #function
        return 2 * pi * self.__radius 
        