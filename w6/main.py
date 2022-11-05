from person import Person
from christmaspresent import ChristmasPresent

p1 = Person("Ayad")
present1 = ChristmasPresent("PS5", 4800)
p1.AddChrismasPresent(present1) # det betyder att stefan ska få PS5 som kostar 4800kr

p2 =  Person("Aryan")
present2 = ChristmasPresent("Nissan skyline", 2000000)
p2.AddChrismasPresent(present2)

p3 =  Person("Didar")
present3 =  ChristmasPresent("Ferrari aventador", 2500000)
p3.AddChrismasPresent(present3)

p4 =  Person("Maria")
present4 = ChristmasPresent("Lägenhet i spanien", 2000000)
p4.AddChrismasPresent(present4)
 
personList = [p1,p2,p3,p4]

for person in personList:
    print(f"{person.GetName()} {person.GetChrismasPresentTotal()} ")