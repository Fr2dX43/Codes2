from math import pi


class Circle:
    def __init__(self, radie:int) -> None:
        self.__radius = radie
    
    def Area(self):
        return pi * self.__radius ** 2
        
    def Circumference(self):
        return 2 * pi * self.__radius 
        