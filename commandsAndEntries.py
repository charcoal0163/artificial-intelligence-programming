from tkinter import *
from tkinter.font import *
import tkinter.messagebox as ms

top = Tk()
top.title("Dialogue")
top.geometry("200x300")

def showMessage():
    ms.showinfo(title = "Information", message = "be informed bitches")
    
def showErrorMessage(title, message):
    ms.showerror(title, message)

def showWarningMessage():
    ms.showwarning("Warning", "EARLLLL")

def askQuestion():
    res = ms.askquestion("Question", "Change the label?")
    if res == "yes":
        label.configure(text = "ch-ch-ch-changes")
    
def askYNQuestion():
    res = ms.askyesno("Yes/No Question", "Change the label?")
    if res == YES:
        label.configure(text = "we can be heroes")
    else:
        res2 = ms.askokcancel("OK/Cancel", "Are you sure?")
        if res2 == True:
            label.configure(text = "yippie")
        else:
            label.configure(text = "okay :(")

title = "Error Message"
message = "girl you wrong"

label = Label(top, text = "Examples", font = ("courier", 9, "normal"))
label.grid(row = 0, column = 0)
button1 = Button(top, text = "Show Message", font = ("times", 9, "normal", "italic"), command = showMessage)
button1.grid(row = 1, column = 1)
button2 = Button(top, text = "Show Error", font = ("times", 9, "normal", "italic"), command = lambda: showErrorMessage(title, message))
button2.grid(row = 2, column = 1, pady = 10)
button3 = Button(top, text = "Show Warning", font = ("times", 9, "normal", "italic"), command = lambda: showWarningMessage())
button3.grid(row = 3, column = 1, pady = 5)
button4 = Button(top, text = "Ask Question", font = ("times", 9, "normal", "italic"), command = askQuestion)
button4.grid(row = 4, column = 1, pady = 5)
button5 = Button(top, text = "Yes/No Question", font = ("times", 9, "normal", "italic"), command = askYNQuestion)
button5.grid(row = 5, column = 1, pady = 5)
button0 = Button(top, text = "Quit", command = top.destroy, font = ("times", 9, "normal", "italic"))
button0.grid(row = 8, column = 1, pady = 5)

# exercise from powerpoint
root = Tk()
root.title("Dalbah")
root.geometry("300x100")

def okayCancel():
    response = ms.askokcancel("Okay/Cancel", "HELLO BITCHES")
    if response == True:
        ynRes = ms.askyesno("Yes/No Question", "you sure?")
        if ynRes == YES:
            ms.showinfo("Proceed Status", "Going Ahead...")
        else:
            ms.showinfo("Cancelling", "BYE BYE")
Label(root, text = "Exercise", font = ("times", 10), pady = 10).pack()
btn1 = Button(root, text = "Okay/Cancel", command = okayCancel)
btn1.pack()
# end of exercise

toot = Tk()
toot.title("Dialogue")
toot.geometry("200x150")

def getName():
    if ent1.get() and ent2.get():
        full = ent1.get() + " " + ent2.get()
        ms.showinfo("Full Name", full)
    else:
        ms.showerror("Error", "One or two entries are empty.")

lab1 = Label(toot, text = "First Name: ")
lab1.grid(row = 0)

lab2 = Label(toot, text = "Last Name: ")
lab2.grid(row = 1)

ent1 = Entry(toot)
ent1.grid(row = 0, column = 1)

ent2 = Entry(toot)
ent2.grid(row = 1, column = 1)

btn1 = Button(toot, text = "Get Name", command = getName)
btn1.grid(row = 2, column = 1, sticky = "w")

btn2 = Button(toot, text = "Quit", command = toot.destroy)
btn2.grid(row = 2, column = 1, sticky = "e")

topper = Tk()
topper.title("Dialogue")
topper.geometry("200x150")

def addNum():
    if entA.get() and entB.get():
        lblC.configure(text = int(entA.get()) + int(entB.get()))
        
lblA = Label(topper, text = "First Number")
lblA.grid(row = 0)

lblB = Label(topper, text = "Second Number")
lblB.grid(row = 1)

entA = Entry(topper)
entA.grid(row = 0, column = 1)

entB = Entry(topper)
entB.grid(row = 1, column = 1)

btnA = Button(topper, text = "+", command = addNum)
btnA.grid(row = 2)

lblC = Label(topper, text = "answer here")
lblC.grid(row = 3)

topper.mainloop()
toot.mainloop()
root.mainloop()
top.mainloop()