from typing import Type


class Point:
    def __init__(self, x:int = 0, y:int = 0):
        self.__x = x
        self.__y = y

    def Move(self, xDelta:int = 0, yDelta:int = 0):
        self.__x = self.__x + xDelta
        self.__y = self.__y + yDelta


    def Reset(self):
        self.__x = 0
        self.__y = 0
    
    def GetX(self) -> int:
        return self.__x

    def GetY(self) -> int:
        return self.__y

    def Add(self, otherPoint:type[Point]):
        self.__x = self.__x + otherPoint.GetX()
        self.__y = self.__y + otherPoint.GetY()

    


def CoolFunction(tal:int) -> int:
    return tal * 123