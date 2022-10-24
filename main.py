
#class är en mall dvs bara en ritnig
#object utefrån class - object är en instans av en class

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
# import os
# from turtle import color
# os.system("cls")
# ############exemple på OOP##################
# class Ritning:
#     def __init__(self):
#         self.Color = ""
#     def Repaint(self, color:str):
#         self.__Color = color
#     def GetColor(self):
#         return self.__Color



# ayadsHus = Ritning()
# ayadsHus.Repaint("blue")
# annanHus = Ritning()
# annanHus.Repaint("Red")
# print(ayadsHus.GetColor())
# print(annanHus.GetColor())
##########################################
import os
os.system("cls")

#self används är för att särskilja olika objeckt

class Ritning:
    def __init__(self): #metod
        self.Color = ""
    def Repaint(self,color:str):
        self.__Color = color
    def GetColor(self):
        return self.__Color



stefansHus = Ritning()
stefansHus.Repaint("blue")
annasHus = Ritning()
annasHus.Repaint("Red")
print(stefansHus.GetColor())
print(annasHus.GetColor())

#######################################
class Student:
    def __init__(self, namn:str, age:int):#constutior #*
        #skapa alla propertties/Engenskaper/varibler
        #som hör till ritningen
        self.Namn = namn #* 
        self.__Age = 0 #* #priviate/protected variabel
        self.SetAge(age) #sätter age i början genom att anrompa metoden SetAge
        self.__postnr = "" #* #properties bäst och köra __ på allt
        self.Kurslista = []

    def SetAge(self, newAge:int): #för att ändra på __Age
        if newAge > 0:
            self.__Age = newAge
    def GetAge(self):
        return self.__Age

stefan = Student("Stefan", -12) #skapar en student
stefan.SetAge(-13)
#stefan.SetAge(132)
print(stefan.GetAge())


print(stefan.Namn, stefan.Age)
#print(stefan.__dict__) #varje object ligger som dict

# #Guide för att skapa en class
# # 1. class Namn
# # 2. def__init__(self)
# #         här skapar du properties för objecktet
# # 3. __ på alla propeties
# # 4. getter och setters med Vaildering
# # 5. constuctor - vad skicka in -vi måste definera vad är vaild state

# #lektion 1:24 min lektion 20221003_083217

#construtor parameterar vad krävs för att objekten ska vara vallied
#måste lägga de parametar som ibörjan måste vara satta för att objectet ska var vaild

class Person:
    def __init__(self, personnr:str ): 
        self.__Name = ""
        self.__Personnr = personnr
    def Setpersonnr(self, new:str): #sett personnummer
        self.__Personnr = new
    def Setname(self, new:str): #sett namn
        self.__Name = new

s = Person("21324213-32123")
