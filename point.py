from typing import Type

class Point: #class 
    def __init__(self, x:int = 0, y:int = 0): #kontruktor
        self.__x = x
        self.__y = y
        
    def GetX(self) -> int:
        return self.__x

    def GetY(self) -> int:
        return self.__y

    def Add(self, otherPoint ): #class typehinting
        self.__x = self.__x + otherPoint.GetX()
        self.__y = self.__y + otherPoint.GetY()

def Coolfunction(tal:int) -> int:
    return tal*123
    

  