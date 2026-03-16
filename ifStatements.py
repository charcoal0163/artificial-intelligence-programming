# tupples:
(x, y, z) = (1, 2, 3)

# lists:
[a, b, c, d, e] = [43.8, "test", -92, 12.02, False]
# notice: elements in the list can have different data types

# slicing of a string
message = "spam"
j = message[0:2]
k = message[2:4]
print(j, k)

# augmented assignment:
sum = 10
sum += 5
sum /= 3
sum **= 2
# notice: augmented assignments work with all operations

# if statements:
mark = int(input("enter mark: "))
if mark >= 90 and mark <= 100:
    print("yay")
elif mark >= 80 and mark < 90:
    print("less yay")
elif 70 <= mark < 80:
    print("almost")
elif mark >= 50:
    print("wow really?")
else:
    print("lol nope")

# more if statements:
country = input("enter country: ")
if country.lower() == "germany":
    print("german")
elif country.lower() == "ireland":
    print("irish")
else:
    print("foreigner")

alienColour = input("what colour is the alien?\t")
if alienColour.lower() == "green":
    print("you have earned five (5) points! :)")
elif alienColour.lower() == "yellow":
    print("you have earned ten (10) points! :O")
elif alienColour.lower() == "red":
    print("you have earned fifteen (15) points! :D")
else:
    print("you have earned zero (0) points. :(")