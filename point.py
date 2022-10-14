from typing import Type


class Point:
    def __init__(self, x:int = 0, y:int = 0):
        self.__x = x
        self.__y = y

    def move(self, xDelta:int = 0, yDelta:int = 0):
        self.__x += xDelta
        self.__y += yDelta

    def Reset(self): #anropas till main.py
        self.__x = 0
        self.__y = 0
    
    def GetX(self) -> int:
        return self.__x

    def GetY(self) -> int:
        return self.__y

    def Add(self, otherPoint):
        self.__x = self.__x + otherPoint.GetX()
        self.__y = self.__y + otherPoint.GetY()

    


def CoolFunction(tal:int) -> int:
    return tal * 123