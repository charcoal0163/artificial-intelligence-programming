x = 10
y = 20

# operations in python:
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(y / x)
# notice: int / int = float

print(7 % 2)
print(3 ** 2)
print(2 ** 3)
print(3 ** 2 - 1)
print(16 /2)

print(30 / 20)
print(30 // 20)
# notice: double forward slash '//' indicates the floor value

# logical relationships in python:
print(False and True)
print(False or True)
print(True or True)
print(False or False)
print(not False)
print(not True)

a = 10_000_000
print(a)
# notice: use an underscore in large numbers for readability

# multiple/tupple assignments:
f, g, h = 3, 7, 11
b, c, d, e = 5, 3.9, "test", False

x = input("enter something fuckers\n")
print("you entered:", x)
# notice: any input value is string, conversion is necessary

age = input("enter age\n")
if int(age) > 18:
    print("adult fucker")

grade = int(input("input first grade\t"))
grade2 = int(input("input second grade\t"))
average = (grade + grade2) / 2
print(average)

num = int(input("enter a number:\t"))
print(num ** 2)

# changing the default format:
print(1, 2, 3, 4)
print(1, 2, 3, 4, sep = "!")
print(1, 2, 3, 4, sep = " *** ", end = "\nthe end\n")

# swapping:
j = 12
k = 79
j, k = k, j
print(j, k)

# extended sequence unpacking:
one, two, three, four, five, six = "python"
p, q, *r = "python"
*p, q, r = "python"
p, *q, r = "python"
