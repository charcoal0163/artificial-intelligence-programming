class Date:
    def __init__(self, day = 1, month = 1, year = 1990):
        self.day = day
        self.month = month
        self.year = year
    
    def setDay(self, day):
        self.day = day
    def setMonth(self, month):
        self.month = month
    def setYear(self, year):
        self.year = year
    def getDate(self):
        return f"{self.day}/{self.month}/{self.year}."

class Student:
    def __init__(self, ID, name, major, position, admitDay, admitMonth, admitYear):
        self.ID = ID
        self.name = name
        self.major = major
        self.position = position
        self.birth = Date()
        # defined birth as an object of date, takes default values
        self.admit = Date(admitDay, admitMonth, admitYear)
        # defined hired as an object of date, while providing data at building student
        
    def setBirth(self, day, month, year):
        self.birth.setDay(day)
        self.birth.setMonth(month)
        self.birth.setYear(year)
    def printDeets(self):
        print(f"Student ID: {self.ID}, student name: {self.name}.")
        print(f"Student major: {self.major}, student position: {self.position}.")
        print(f"Date of birth: {self.birth.getDate()} Date admitted: {self.admit.getDate()}")

class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.setAge(age)
        
    def describe(self):
        if self.age != 0:
            print(f"User's name is {self.first} {self.last}, and they are {self.age} years old.")
        else:
            print(f"User's name is {self.first} {self.last}.")
    def setAge(self, age):
        if age >= 18:
            self.age = age
        else:
            print("haha nope")
            self.age = 0

class Privileges:
    def __init__(self, priv1, priv2, priv3):
        self.priv1 = priv1
        self.priv2 = priv2
        self.priv3 = priv3
    
    def showPriv(self):
        print(f"Privileges:\n1. {self.priv1}.\n2. {self.priv2}.\n3. {self.priv3}")
        # ["can add post", "can delete post", "can ban user"]
        
class Admin(User):
    def __init__(self, first, last, age, priv1, priv2, priv3 = None):
        super().__init__(first, last, age)
        self.privileges = Privileges(priv1, priv2, priv3)

class Rectangle:
    # constructor:
    def __init__(self, length = 1, width = 1, colour = "colourless"):
        self.length = length
        self.width = width
        self.colour = colour
        self.name = "julianne"
        # notice: there's no need to define all variables to use them

    # notice: all methods must take 'self' as a first parameter
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