# functions! part 2

def showGrade(name, grade = "nope"):
    print(f"Student: {name}, grade: {grade}")
# notice: use default parameters when certain parameters are non-applicable
# notice: when defining default parameters, write them after the non-default parameters (if applicable)
showGrade("Acheron", 99)
showGrade(grade = 95, name = "Ahmad")
# notice: use keywords to send arguments without considering the order of parameters
showGrade("Qusai")
# notice: sending one value to the function results in using the default values

# exercise from powerpoint
def shirt(size = "Large", message = "I love Python"):
    print(f"The shirt's size is {size}, and the message on the shirt is {message}.")
shirt("X-Large", "Cogito ergo sum")
shirt(size = "Medium")
shirt(message = "God is dead")
shirt(message = "Pink Freud", size = "Small")

# end of exercise

def fullName(first, last, middle = ""):
    # notice: optional argument, if user enters any value for 'middle', if statement would return true
    if middle:
        print(f"Your name is {first} {middle} {last}.")
    else:
        print(f"Your name is {first} {last}.")

fullName("Acheron", "Dalbah", middle = "Ahmad")
fullName("Acheron", "Dalbah")
fullName(input("Enter first name: "), input("Enter last name: "), input("Enter middle name (optional): "))

def mltpSquare (e, f = None):
    if f != None:
    # notice: or 'if f':
        return e * f
    else:
        return e ** 2

print(mltpSquare(2, 3))
print(mltpSquare(2, 0))
print(mltpSquare(2))

def calculate(x, y):
    add = x + y
    sub = x - y
    mult = x * y
    div = x / y
    
    return add, sub, mult, div

value = calculate(6, 2)
print(calculate(6, 2))
# notice: multiple values in a return statement are returned as a tuple
a, b, c, d = calculate(8, 2)
print(a, b, c, d)
# notice: use multiple assignment to return each value individually
g, h, *i = calculate(20, 5)
print(g, h, i)
# notice: use extended sequence unpacking

def stdDic(name, major, age, grade):
    student = {"Name": name, "Major": major, "Age": age, "Grade": grade}
    return student
print(type(stdDic("Acheron", "Astrophysics", 20, 99)))
print(stdDic("Acheron", "Astrophysics", 20, 99))

def updateNum(n):
    n += 2
    print(n)
w = 3
updateNum(w)
print(w)
# notice: "primitive" data types are call by value, whereas objects (e.g., lists, dictionaries) are call by reference

def updateList(listA):
    for i in range(len(listA)):
        listA[i] += 5
    print("the function", listA)
    return listA
theList = [1, 2, 3, 4, 5]
notTheList = updateList(theList[:])
# notice: using the slicing notation [:] transforms the handling of the list to call by value
print("the list", theList)
updateList(theList)
print("the list, after", theList)
print("not the list", notTheList)
