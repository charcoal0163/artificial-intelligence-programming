# # writing and appending on a text file using write and writelines

# file = open("test.txt", "w")
# file.write("This is a test document.\n")
# file = open("test.txt", "a")
# file.write("This has been appended.\n")
# file.close()

# files = open("secondTest.txt", "w")
# files.write("What is your name?\n")
# files.write("Tony!\n")
# files.write("What?\n")
# files.close()

# greetings = ["Hello", "Bonjour", "Guten Tag"]
# third = open("thirdTest.txt", "w")
# third.writelines("\n".join(greetings))
# third.writelines(" *** ".join(greetings))
# third.close()

# # reading from a text document using read, readline, and readlines

# file = open("test.txt", "r")
# lines = file.read()
# print(lines)
# print(type(lines))
# file.close()

# line = file.readline()
# print(line)
# print(type(line))

# theLine = file.readline()
# while theLine != "":
#     print(theLine)
#     theLine = file.readline()
# else:
#     print("end of file.")
# file.close()

# file = open("test.txt", "r")
# theLines = file.readlines()
# print(theLines)
# print(type(theLines))
# print(len(theLines))
# file.close()

# # notice: this isn't a loop -- it opens the file and automatically closes it
# with open("test.txt", "r") as file:
#     one = file.read(15)
#     print(one)
#     two = file.read(15)
#     print(two)

# with open("test.txt", "r") as file:
#     one = file.readline(15)
#     print(one)
#     two = file.readline(15)
#     print(two)
    
# with open("test.txt", "r") as file:
#     one = file.readlines(15)
#     print(one)
#     two = file.readlines(15)
#     print(two)

# with open("test.txt", "r+") as file:
#     a = file.readline()
#     print(a)
#     file.write("This is a new sentence.")

# with open("test.txt", "a+") as file:
#     b = file.readline()
#     print(b)
#     file.write("This is another new sentence.")

with open("exerciseFile.txt", "w") as textFile:
    textFile.write("This is the first line.\n")
    textFile.write("This is the second line.\n")
    textFile.write("This is the third line.\n")

with open("exerciseFile.txt", "a") as textFile:
    textFile.write("This is the fourth line.")
    
with open("exerciseFile.txt", "r") as textFile:
    nextLine = textFile.readline()
    theList = []
    while nextLine != "":
        print(nextLine)
        theList.append(nextLine)
        nextLine = textFile.readline()
        
    print(theList)
    print(len(theList))