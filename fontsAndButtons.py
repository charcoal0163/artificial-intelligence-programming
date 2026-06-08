from tkinter import *
from tkinter.font import *

# top = Tk()
# top.title("First Example")
# top.geometry("320x320+400+400")

# # # to create objets of Font to use in a label
# # font1 = Font(family = "times", size = 20, weight = "bold", slant = "italic")
# # font2 = Font(family = "arial", size = 12, slant = "italic", underline = 5)

# # # to create a label and change the colour of the text (background and foreground), and specify the font
# # label1 = Label(top, text = "Willkommen", bg = "light blue", fg = "dark blue", font = font1)
# # label1.pack()

# # label2 = Label(top, text = "Bienvenue", fg = "indigo", font = font2)
# # label2.pack(pady = 10)

# # button1 = Button(top, text = "Au revoir", bg = "pink", fg = "#5D3A00", font = font1)
# # button1.pack()

# # button2 = Button(top, text = "Aufwidersehen", font = ("times", 8, "italic"), bg = "#6DAEDB", fg = "#173753")
# # button2.pack()

# # label3 = Label(top, text = "Willkommen", bg = "light blue", fg = "dark blue", width = 30, height = 5)
# # label3.pack()

# # button3 = Button(top, text = "Aufwidersehen", font = ("times", 8, "italic"), bg = "#6DAEDB", width = 20, height = 2)
# # button3.pack()

# # # to edit the details of a label or button
# # label2.configure(fg = "black", relief = GROOVE)

# # # exercise from powerpoint
# # new = Tk()
# # new.title("Dalbah")
# # new.geometry("300x100")

# # lbl1 = Label(new, text = "First", font = ("times"), bg = "#6DAEDB", relief = GROOVE)
# # lbl1.pack()
# # lbl2 = Label(new, text = "Second", font = ("courier"), bg = "#A1CCA5", relief = SUNKEN)
# # lbl2.pack()
# # # end of exercise

# # def changeLabel():
# #     label4.configure(text = "sinnerman")

# # def changeLabelTo(text):
# #     label4.configure(text = text)

# # label4 = Label(top, text = "i wish i knew how it would feel to be free")
# # label4.pack()
# # button4 = Button(top, text = "ch-ch-ch-changes", command = changeLabel)
# # button4.pack()
# # button5 = Button(top, text = "no woman, no cry", command = top.destroy)
# # button5.pack()
# # button6 = Button(top, text = "turn your lights down low", command = lambda: changeLabelTo("stand down margaret"))
# # button6.pack()

# exercise 2
another = Tk()
another.title("Dalbah 2.0")
another.geometry("220x220")

def change():
    label5.configure(text = "the button was clicked")
    
label5 = Label(another, text = "when the chips are down")
label5.pack()
button7 = Button(another, text = "click here", command = change)
button7.pack()
Button(another, text = "bye bye", command = another.destroy).pack()
# end of exercise 2

top.mainloop()