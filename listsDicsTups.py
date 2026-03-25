# lists!
names = ["ahmad", "acheron", "dalbah", "augustine"]
if "acheron" in names:
    print("name's there")
else:
    print("name's not there")

name = input("enter a name\t")
if name not in names:
    print("lol nope")
else:
    print("yay")

message = "welcome to artificial intelligence programming using python"
tokens = message.split()
print(tokens)
# notice: 'split' method tokenises a text into separate words

second = "welcome. this is a new semester. we're using python. enjoy."
sentences = second.split(sep = ". ")
print(sentences)
# notice: specify the separator to split the string using different ways (e.g. punctuation, stop words, etc.)

students = ["zohran", "ahmad", "julianne", "alexandrine", "dalbah", "jean-jacques"]
students.sort()
print(students)
# notice: 'sort' method sorts the data in ascending order
students.sort(reverse = True)
print(students)
# notice: 'reverse' parameter sorts the data in descending order.
# notice: 'reverse' is false by default, changing it to true will sort in desceneding order. like an on/off switch.

# notice: ordered isn't the same as sorted. ordered means they have specific places, whereas sorted means they're ordered based on the data

sortedStudents = sorted(students)
print(students)
print(sortedStudents)

reverseStudents = sorted(students, reverse = True)
print(reverseStudents)
# notice: 'sorted' method doesn't alter the original list
# notice: rather it returns the changed list to a variable and keeps the original the way it is
# notice: 'sort' alters the list

students.reverse()
print(students)
# notice: 'reverse' method only reverses the positions of the objects in the list, with no regard to the contents

# exercise from powerpoint
countries = ["germany", "ireland", "austria", "switzerland", "finland"]

print("regular:\t\t\t", countries)
countries.sort()

print("sort():\t\t\t\t", countries)
countries.sort(reverse = True)

print("sort() + reverse:\t", countries)
sortedCountries = sorted(countries)

print("sorted():\t\t\t", sortedCountries)
reverseCountries = sorted(countries, reverse = True)

print("sorted() + reverse:\t", reverseCountries)
countries.reverse()

print("reverse():\t\t\t", countries)
print("length:\t\t\t\t", len(countries))
# end of exercise

# end of lists.

# dictionaries!
stdDic = {"Student ID": 202420163, "Name": "Acheron", "Major": "DSAI", "Average": 97.6}
print(stdDic)
stdDic["Average"] = 98.2
print(stdDic)
print(stdDic["Average"])
stdDic["Address"] = "Zarqa"
print(stdDic["Address"])
del stdDic["Address"]
print(stdDic)

# tuples!
fish = ("big", "small", "yellow", "blue")
print(fish)
print(type(fish))
print(fish[1])
x = fish[0]
print(x)
# notice: tuples, unlike lists and disctionaries, are immutable

# notice: to alter a value in the tuple, cast it as a list first, alter, then cast back to tuple
discount = (.05, .2, .35)
discount = list(discount)
discount[0] = 0.1
discount.append(.5)
discount = tuple(discount)
print(discount)