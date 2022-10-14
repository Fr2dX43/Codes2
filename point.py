class Robot:
    def introduce_self(self):
        print(f"My name is {self.name}")

r1 = Robot()
r1.name = "tom"
r1.color = "red"
r1.weight = 30

r2 = Robot()
r2.name = "jerry"
r2.color = "blue"
r2.weight = 18 

r1.introduce_self()
r2.introduce_self()
    


