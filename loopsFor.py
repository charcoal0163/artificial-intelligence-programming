# loops! part 2
# for loops

fruits = ["apples", "bananas", "strawberries", "kiwis"]
for i in fruits:
    print(i)
# notice: i is not an index, it's a variable that stores the value of each element in the list

grades = [92, 87, 94, 96, 91]
index = 0
for grade in grades:
    grades[index] += 2
    index += 1
    print(grade)

tup = (10, 20, 30, 40)
for t in tup:
    print(t + 5)
else:
    print("lol nope")
print(tup)

points = [(2, 3), (4, -1), (0, 0.5), (-1, -2)]
# notice: we can mix lists and tuples and dictionaries
# notice: each element in the list is a tuple

# accessing a certain element of the tuple from the list
print(points[1][0])

# accessing all elements -- as tuples
for p in points:
    print(p)
    x = p[0]
    y = p[1]
    print("elements of the tuple:", x, y)
    
# accessing all elements -- as individual elements
for a in points:
    for b in a:
        print(b)

for (e, f) in points:
    print(e, f)

std1 = {"ID": 202420163, "Name": "Acheron", "Major": "Astrophysics", "Grade": 98}
std2 = {"ID": 202410178, "Name": "Ahmad", "Major": "Mathematics", "Grade": 96}
std3 = {"ID": 202324020, "Name": "Frederick", "Major": "Data Science", "Grade": 89}
std4 = {"ID": 202512003, "Name": "Julianne", "Major": "Psychology", "Grade": 94}

# for loops on a dictionary
for key in std1:
    print(key, end = ": ")
    print(std1[key])

students = [std1, std2, std3, std4]
print(students)
# notice: each element in the list is a dictionarry

for dic in students:
    for (key2, deets) in dic.items():
        print(key2, deets, sep = ": ")

print(std3.items())
# notice: items() method returns a list of tuples
# use items() method to access elements in the dictionary using tuple assignment
for (key, value) in std3.items():
    print(key, value, sep = ": ")
    if (key == "Grade" and value < 90):
        std3[key] = value + 2
print(std3)

for c in "onomatopoeia":
    print(c, end = "  ")


# basics of indexed for loops
for first in range(5):
    print(first)
for second in range(5, 11):
    print(second)
for third in range(0, 101, 10):
    print(third)
for fourth in range(10, -1, -2):
    print(fourth)

numbers = [10, 20, 30, 40, 50]
# using index with for to access the list
for i in range(len(numbers)):
    numbers[i] += 5
    print(f"index {i}", numbers[i], sep = " - ")
print(numbers)

tullab = {"IDs": [202420163, 202410178, 202324020, 202512003],
          "Names": ["Acheron", "Ahmad", "Frederick", "Julianne"],
          "Majors": ["Astrophysics", "Mathematics", "Data Science", "Psychology"],
          "Grades": [98, 96, 89, 94]}
for (key3, values) in tullab.items():
    print(key3, end = ":")
    for i in values:
        print(i)

nomnom = ["apple", "banana", "kiwi", "strawberry", "crepe", "waffle"]
# slicing
print(nomnom[1])
print(nomnom[1:3])
print(nomnom[:3])
print(nomnom[1:3][0])
print(nomnom[1][0:4])
print(nomnom[3:])
print(nomnom[-1])
print(nomnom[-2])
print(nomnom[-3:])

for o in nomnom[2:5]:
    print(o)
