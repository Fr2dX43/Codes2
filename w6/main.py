from person import Person
from christmaspresent import ChristmasPresent

p1 = Person("Ayad")
present = ChristmasPresent("PS5", 4800)
p1.AddChristmasPresent(present) # det betyder att stefan ska få PS5 som kostar 4800kr

p2 =  Person("Aryan")
p2.AddChristmasPresent(ChristmasPresent("Nissan skyline", 2000000))

p3 =  Person("Didar")
p3.AddChristmasPresent(ChristmasPresent("Ferrari aventador", 2500000))

p4 =  Person("Maria")
p4.AddChristmasPresent(ChristmasPresent("Lägenhet i spanien", 2000000))
 
personList = [p1,p2,p3,p4]

for person in personList:
    print(f"{person.GetName()} {person.GetTotal()} kr")