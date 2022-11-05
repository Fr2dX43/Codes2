
#grön är class , gul är function, blå en function
from point import Point, Coolfunction
 
start = Point()
end = Point(10,10)

print(f"we start at {start.GetX()} {start.GetY()}")
print(f"we start at {end.GetX()} {end.GetY()}")

start.Add(end)
print(f"after add is the start {start.GetX()} {start.GetY()}")

print(Coolfunction(12))