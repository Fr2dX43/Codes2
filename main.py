from point import CoolFunction, Point
from rectangle import Rectangle
from circle import Circle

c = Circle(12)
d = Circle(2342)
omkrets = c.Circumference()
print(f"Omkrets {omkrets}")
print(f"Area {c.Area()}")
print(f"Omkrets {d.Circumference()}")
print(f"Area {d.Area()}")




width = 12
height = 13
print(f"Arean är {width*height}")

rect = Rectangle(width,height)
print(f"Arean är {rect.CalculateArea()}")

mario = Point(100,20)
# När Mario för i spelet - sätt point to 0,0 (reset)
mario.Reset()
# om VK_RIGHT + VK_DOWN
mario.Move(xDelta = 1,yDelta= 1) 

luigi = Point(50,50)
# om VK_RIGHT + VK_DOWN
luigi.Move(xDelta = 2,yDelta= 1) 



start = Point(1,1)

end = Point(10,10)

print(f"Vi startar labyinten på {start.GetX()}, {start.GetY()}")
print(f"Vi slutar labyinten på {end.GetX()}, {end.GetY()}")

start.Add(end)
print(f"Efter plus är starten {start.GetX()}, {start.GetY()}")


print(CoolFunction(12))