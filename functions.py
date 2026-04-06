# functions!

# type 1: non-parameterised, no return
def printNumbers():
# notice: there is no return data type
    # # using for loop
    # for i in range(1, 11):
    #     print(i)
    
    # using while loop
    i = 1
    while True:
        print(i)
        i += 1
        if(i == 11):
            break

# type 2: parameterised, no return
def printRange(start, end):
    # # using for loop
    # for i in range(start, end + 1):
    #     print(i)

    # using while loop
    while start != end + 1:
        print(start)
        start += 1

# type 3: parameterised, return
def returnSum(a, b):
    if type(a) == str:
        return 0
    return a + b

# type 4: non-parameterised, return
def returnInput():
    e = int(input("Enter first number: "))
    f = int(input("Enter second number: "))
    return e + f

# function invocation
printNumbers()
print("======")
printRange(5, 15)
x = int(input("Enter start value: "))
y = int(input("Enter end value: "))
printRange(x, y)
print("======")
print(returnSum(5, 7))
print(returnSum("hello", "world"))
c = float(input("Enter first value: "))
d = float(input("Enter second value: "))
added = returnSum(c, d)
print(added)
print("======")
print(returnInput())

def showGrade(name, grade):
    print(f"Student: {name}, grade: {grade}")
    
showGrade("Acheron", 99)
showGrade(98, "Ahmad")
# notice: no syntax error, but logical error
showGrade(grade = 95, name = "Qusai")
# notice: use keywords to send arguments without considering the order of parameters