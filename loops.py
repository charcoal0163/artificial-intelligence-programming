# loops!
# while loops

# 1: counter controlled
i = 1
while i <= 10:
    print(i)
    i += 1
else:
    print("finished")
# notice: else statement is optional in while loop

count = 0
summation = 0
while count < 3:
    mark = float(input("enter a mark: "))
    summation += mark
    count += 1
average = summation / 3
print(average)

# 2: sentinel controlled
marks = float(input("enter a mark, otherwise -1: "))
counter = 0
summed = 0
while marks != -1:
    summed += marks
    counter += 1
    marks = float(input("enter a mark, otherwise -1: "))
else:
    if counter == 0:
        print("no marks were entered")
if counter != 0:
    averageSent = summed / counter
    print(averageSent)

# 3: flag controlled
flag = False
counting = 0
total = 0
while not flag:
    grade = input("enter a mark, otherwise 'quit': ")
    if grade.lower() != "quit":
        total += float(grade)
        counting += 1
    else:
        flag = not flag
averageFlag = total / counting
print(averageFlag)

# 4: break statement -- not flag controlled
counting = 0
total = 0
while 1:
# equivalent to "while True:"
    grade = input("enter a mark, otherwise 'quit': ")
    if grade.lower() != "quit":
        total += float(grade)
        counting += 1
    else:
        break
averageFlag = total / counting
print(averageFlag)

# 5: continue statement
i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        continue
    print(i)