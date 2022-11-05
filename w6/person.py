class Person:
    def __init__(self, name:str): #anvönd konstruktor på tentan
        self.__Name = name
        self.__Presents = []

    def AddChrismasPresent(self, present):
        self.__Presents.append(present)


    def GetChrismasPresentTotal(self):
        sum = 0
        for person in self.__Presents:
            sum = sum + person.GetPrice()
        return sum

    def GetName(self):
        return self.__Name
