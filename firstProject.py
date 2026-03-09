print("weclome to python");

message = "what a nice day"
print(message)
# notice: when declaring a variable, don't add a data type

x = 8
y = 5.5
# notice: y is a float, there is no double in python

z = False

string = "This is the first lecture in python"
print(string.upper())
print(string.lower())
print(string.title())

text = "    dalbah      "
print(text.strip())

print("my name is dalbah".upper())

a = 10
b = 20
print(a, b)

name = "acheron"
surname = "dalbah"

print(name, surname)
print(name + " " + surname)
# notice: two different ways to concatenate two strings

print(f"my name is {name} {surname}")
# notice: use 'f' to indicate formatting of placeholders
# notice: use curly brackets to indicate the variables

print(f"{a} + {b} = {a + b}")


# question: how to create a generalised format for adding two variables
c = 12
d = 61

f = 2.5
g = 4.3

eq = "{} + {} = {}"
print(eq.format(c, d, c + d))
print(eq.format(f, g, f + g))

first = "mada"
second = "big mo"

print("i'd like to invite {} and {}".format(first, second))
print("i'd like to invite {1} and {0}".format(first, second))

print('rene descartes said: "cogito ergo sum", which translates to "i think therefore i am".')