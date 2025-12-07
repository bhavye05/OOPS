import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def distance(self, p2):
        return math.sqrt((self.x - p2.x)**2 + (self.y - p2.y)**2)

p1 = Point(2, 3)
p2 = Point(5, 7)
print(p1, p2)
print("Distance:", p1.distance(p2))
