class Shape:
    def __init__(self, colour):
        self.colour = colour
    def describe(self):
        print(f"The shape is {self.colour}.")
    def getArea(self):
        return 0
        
class Rectangle(Shape):
    def __init__(self, colour, length, width):
        super().__init__(colour)
        self.length = length
        self.width = width
    
    def describeRect(self):
        print(f"The rectangle is {self.length} by {self.width}.")
        super().describe()
    def getArea(self):
        return self.length * self.width
        
firstRec = Rectangle("blue", 2.5, 3)
firstRec.describeRect()

# overriding methods:
print(firstRec.getArea())
firstShape = Shape("green")
print(firstShape.getArea())

# exercise 7 from powerpoint
class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.setAge(age)
        
    def describe(self):
        if self.age != 0:
            print(f"user's name is {self.first} {self.last}, and they are {self.age} years old.")
        else:
            print(f"user's name is {self.first} {self.last}.")
    def setAge(self, age):
        if age >= 18:
            self.age = age
        else:
            print("haha nope")
            self.age = 0
    
class Admin(User):
    def __init__(self, first, last, age):
        super().__init__(first, last, age)
        self.privileges = ["can add post", "can delete post", "can ban user"]
    def showPriv(self):
        for i in range(len(self.privileges)):            
            print(f"This admin can {self.privileges[i]}.")

admin = Admin("Acheron", "Dalbah", 27)
admin.describe()
admin.showPriv()
# end of exercise