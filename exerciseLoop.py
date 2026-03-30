# sentinel
price = 0
while 1:
    age = int(input("enter age (-1 to exit): "))
    if age == -1:
        break
    if age <= 3:
        pass
    elif 3 < age <= 12:
        price += 10
    else:
        price += 15
        
print(f"total cost is ${price}")

# flag
flag = False
cost = 0
while not flag:
    age = input("enter age (quit to exit): ")
    if age.lower() != "quit":
        age = int(age)
        if age <= 3:
            pass
        elif 3 < age <= 12:
            cost += 10
        else:
            cost += 15
    else:
        flag = not flag
print(f"total cost is ${cost}")