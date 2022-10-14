from point import CoolFunction, Point #point from the point
from rectangle import rectangle #rectangle from the rectangle
from circle import circle #take form the file circle
from person import Person #take from the file person

Ayad = Person("Ayad", 19)
if Ayad.IsAdult(): 
    print("du är vuxen")

Stefan = Person("Stefan",14)
if Stefan.IsAdult():
    print("du är inte vuxen")

s = Stefan.GreetAsRovearSpark()
print(s)


c = circle(12)
d = circle(2342)
omkrets = c.Circumference()
print(f"Omkrets {omkrets}")
print(f"Area {c.Area()}")
print(f"Omkrets {d.Circumference()}")
print(f"Area {d.Area()}")



width = 12
height = 13
print(f"Arean är {width*height}")

rect = rectangle(width,height)
print(f"Arean är {rect.CalculateArea()}")

mario = Point(100,20) #vart han börjar
# När Mario för i spelet - sätt point to 0,0 (reset)
mario.Reset()
# om VK_RIGHT + VK_DOWN
mario.Move(xDelta = 1,yDelta= 1) #method xDelta är nameparamiter

luigi = Point(50,50) #flyttar luigi som object i point
# om VK_RIGHT + VK_DOWN
luigi.Move(xDelta = 2,yDelta= 1) #method



start = Point(1,1)

end = Point(10,10)

print(f"Vi startar labyinten på {start.GetX()}, {start.GetY()}")
print(f"Vi slutar labyinten på {end.GetX()}, {end.GetY()}")

start.Add(end)
print(f"Efter plus är starten {start.GetX()}, {start.GetY()}")


print(CoolFunction(12))