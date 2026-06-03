from tkinter import *

root = Tk()
root.title("welcome")

# to specify the dimensions of the root screen (number of columns x number of rows)
# to specify the coordinates of the root screen (+x +y) moving from the top leftmost corner
root.geometry("240x200+400+350")
root.geometry("640x600+400+350")

# notice: using (-x -y) to specify coordinates, means the root screen appears at the bottom rightmost corner
root.geometry("240x200-50-100")

# to set a maximum size and a minimum size of the root screen
root.maxsize(width = 700, height = 700)
root.minsize(width = 150, height = 150)

# exercise from the powerpoint
second = Tk()
second.title("dalbah")
second.geometry("300x100+400+300")
second.maxsize(width = 400, height = 200)
second.mainloop()
# end of the exercise

# creating a label and button on the root screen
# way 1: pack method (stacks the objects on top of one another)

# parameters of Label and Button: the 'parent' of the label, text keyword argument to display the text
label1 = Label(root, text = "Welcome to the Jungle")
# parameters of pack method: keyword argument side takes one of four (top, bottom, right, left), keyword arguments padx and pady to move them away from the sides of the root screen, keyword argument fill to make the button as big as the screen
label1.pack(side = TOP, pady = 50)
button1 = Button(root, text = "Click this one")
button1.pack(side = LEFT, padx = 30, fill = X)
button2 = Button(root, text = "Don't click this one")
button2.pack(side = RIGHT, padx = 30)
label2 = Label(root, text = "Keep Yourself Alive")
label2.pack(side = BOTTOM, pady = 50)

# sub-way 1.2: using pack method without creating an object
Label(root, text = "Welcome to the Jungle").pack(side = TOP, pady = 50)
Button(root, text = "Click this one").pack(side = LEFT, padx = 30)
Button(root, text = "Don't click this one").pack(side = RIGHT, padx = 30)
Label(root, text = "Keep Yourself Alive").pack(side = BOTTOM, pady = 50)

Label(root, text = "Welcome to the Jungle").pack(pady = 50)
Button(root, text = "Click this one").pack()
Button(root, text = "Don't click this one").pack(pady = 50)
Label(root, text = "Keep Yourself Alive").pack()

# way 2: place method (sets the objects in a specific coordinate)
btn1 = Button(root, text = "First Button")
btn1.place(x = 50, y = 50)
btn2 = Button(root, text = "Second Button")
btn2.place(x = 150, y = 150)
btn3 = Button(root, text = "Third Button")
btn3.place(x = 250, y = 250)
extra = Button(root, text = "EXTRA")
extra.place(x = 500, y = 120, width = 100, height = 45)

# way 3: grid method
Label(root, text = "Username: ").grid(row = 0, pady = 5, padx = 10)
Label(root, text = "Password: ").grid(row = 1, pady = 5, padx = 10)

Entry(root).grid(row = 0, column = 1, pady = 5)
Entry(root).grid(row = 1, column = 1, pady = 5)

Button(root, text = "Cancel").grid(row = 2, column = 1, sticky = "e")
Button(root, text = "Login").grid(row = 2, column = 1, sticky = "w")

root.mainloop() # effectively runs the program and displays the screen