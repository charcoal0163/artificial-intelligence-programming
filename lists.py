# lists :)
theList = ["acheron", "ahmad", "rafat", "dalbah"]
print(type(theList))
# notice: theList is considered an object, and therefore it has its own methods

automobiles = ["car", "truck", "motorcycle"]
print(len(automobiles))
# notice: function 'len' returns the length of the list

marks = [90, 79, 45, 87]
print(marks)
print(type(marks))

secondList = ["rafat", 2.5, 10, False]
# notice: lists are heterogenous, they can contain different data types

print(secondList[0])
print(type(secondList[3]))

secondList[1] = 3.5
print(secondList)
# notice: lists are mutable, their content can be changed

# printing the last element of the list:
print(secondList[len(secondList) - 1])
print(secondList[-1])

secondList[2] += 4
print(secondList)

words = ["dionysos", "mythologise", "probability and statistics"]
print(words[0].upper())
print(words[-1].title())

# exercise from powerpoint
friends = ["acheron", "ahmad", "dalbah"]
print("i would like to invite", friends[0])
print(f"i would like to invite {friends[1]}")
print(friends[-1], "is invited to dinner")

for i in range(len(friends)):
    print(f"i would like to invite {friends[i].title()} to dinner")

friends[1] = "antony"
print(f"i would like to invite {friends[1].title()} instead")

friends.insert(0, "apollo")
friends.insert(2, "theodore")
friends.append("emmanuel")
print("new invitations:")
for i in range(len(friends)):
    print(f"i would like to invite {friends[i].title()} to dinner")
# end of exercise

names = []
names.append("julianne")
names.append("hamlet")
names.append("roberto")
names.insert(2, "cordelia")
names.insert(1, "hamish")
# notice: 'append' adds an element to the end of the list, whereas 'insert' adds an element to a specific index

del names[1]
names.pop()
x = names.pop(1)
# notice: 'del' removes a specific element
# notice: 'pop' can be used in two different ways; removing the last element of the list, or removing an element from a specific position
# notice: elements using 'pop' can be saved into different variables

names.remove("hamish")
# notice: 'remove' can be used to delete an element based on its content rather than its index
# notice: unlike 'pop', 'remove' cannot return a value, therefore its content cannot be stored into a different variable
