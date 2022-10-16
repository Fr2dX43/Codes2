#class är en mall dvs bara en ritnig
#object utefrån class 

########Exempel på hur man inte ska göra########
#dålig object
# from dataclasses import dataclass

# @dataclass
# class StudentV1:
#     namn: str
#     personnummer: int
#     kurser: list

# stefan = StudentV1("Stefan",197208030000,["datavetenskap","mattematik"])
# ayad = StudentV1("Ayad",198208030000,["historia","mattematik"])
# ###############################################
#object orgineting handlar om att man ska se till så
#programmet inte kan köras på fel set.

#en metod är en funktion fast som ligger i en class

#acess modiferier = hur man ska komma åt sakerna
#innåt i en object (priviate/protected variabel)

# konstoktor __init__
import os
os.system("cls")
class Student:
    def __init__(self, namn:str, age:int):
        #skapa alla propertties/Engenskaper/varibler
        #som hör till ritningen
        self.Namn = namn 
        #self.Age = age
        self.__Age = age #priviate/protected variabel 
        self.Kurslista = []

stefan = Student("Stefan", -12) #skapar en student

stefan.Age = -123 #för att sätta värde
stefan.__Age = -34
print(stefan.__Age)
print(stefan.Namn, stefan.Age)



