from random import random, choice
import time
from abc import abstractmethod, ABC

class GameObject(ABC): 
    def __init__(self, name:str):
        self._name = name #egenskaper __ betyder private och _ betyder protected
        self._level = 0 #egenskaper i arv ska man bara ha _ 
    @abstractmethod
    def Act(self):
        pass

class Fly(GameObject):
    def __init__(self, name:str, color:str):
        super().__init__(name) #super är en refence från det man har arv ifrån dvs game object
        self.color = color
    def Act(self):
        actions = ["exelent","surrar","landar i maten","blir dödat"]
        action = choice(actions)
        print(self._name, action)


class Person(GameObject):
    def __init__(self, name:str):
        super().__init__(name)
        self.__lastAction = "" #egenskaper

    def Act(self):
        actions = ["äter","rapar","funderar","dricker"]
        action = choice(actions)
        print(self._name, action)
        self.__lastAction = action
        self.levelUp(action)
        # om vi rapar nu och vi rapade tvågoner på rad så lvlar man up
    def levelUp(self, action:str):
        if action == "rapar" and self.__lastAction == "rapar":
            self._level += 1
            print(f"Level up {self._name} to {self._level}") # bara _ när det arv 


stefan = Person("Stefan")
kerstin = Person("Kerstin")
oliver = Person("Oliver")
fly = Fly("fluga", "blå")


deltagare = [stefan,kerstin,oliver,fly]

while True:
    for person in deltagare:
        person.Act()
        time.sleep(0.2)


