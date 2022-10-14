class Person:
    def __init__(self, namn:str,age: int) -> None:
        self.__Namn = namn
        self.__Age = age
    
    def IsAdult(self) -> bool:
        return self.__Age >= 18
    
    def GreetAsRovearSpark(self) -> str:
        result = ""
        text = "hi" + self.__Namn
        for letter in text:
            if self.isvokal(letter.lower):
                result += letter
            elif letter == " ":
                result += letter
            else:
                result += letter + "o" + letter.lower()
        return result

    def isvokal(self, ch) -> bool:
        vokaler = ["a","O","u","Ö","ä","å","e","i","ä"]
        if ch in vokaler:
            return True
        return False
