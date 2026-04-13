# classes!

class Rectangle:
    # constructor
    def __init__(self, length = 1, width = 1, colour = "colourless"):
        self.length = length
        self.width = width
        self.colour = colour
        self.name = "julianne"
        # notice: there's no need to define all variables to use them
        
    def area(self):
        return self.length * self.width
    def details(self):
        print(f"length = {self.length}, width = {self.width}\ncolour = {self.colour}, name = {self.name}\narea = {self.area()}")
    # notice: use setters to validate, and to make variables known as private (since there is no private keyword)
    def setLength(self, length):
        if length > 0:
            self.length = length
        else:
            print("lol nope")
            self.length = 1
    def setWidth(self, width):
        if width > 0:
            self.width = width
        else:
            print("lol nope")
            self.width = 1
    
obj1 = Rectangle(5, 6, "blue")
print("details of first rectangle")
obj1.details()
print("area of first rectangle")
print(obj1.area())
print(Rectangle.area(obj1))

obj2 = Rectangle()
print("details of second rectangle")
obj2.details()

obj2.setLength(-3)
obj2.setWidth(4)
print(obj2.area())

# exercise 5 from powerpoint
class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        
    def describe(self):
        print(f"user's name is {self.first} {self.last}, and they are {self.age} years old.")

obj3 = User("Sadeen", "Abed", 18)
obj3.describe()
# end of exercise