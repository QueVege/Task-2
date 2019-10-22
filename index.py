from tkinter import *
from tkinter import messagebox
from turtle import Screen, Turtle
from curves import *

def show_message():
    messagebox.showinfo("TypeError", "Please enter a valid iteration number")

def curve_type():
    
    draw.reset()
    draw.speed('fastest')
    R = Entry.get()
    
    try:
        R = int(R)

        if var.get() == 0: 
            peano_curve(draw, True, R)
            
        elif var.get() == 1:
            hilbert_curve(draw, True, R)

        elif var.get() == 2:
            gosper_curve(draw, True, R)

    except ValueError:
        show_message()

root = Tk()
root.title('Space filling curves')

screen = Screen()

draw = Turtle()

Label(root, text='Type:').grid(row=0 ,column=0, padx=5, pady=5, sticky="w")

var = IntVar()
var.set(0)
rad0 = Radiobutton(root, text="Peano curve", variable=var, value=0)
rad1 = Radiobutton(root, text="Hilbert curve", variable=var, value=1)
rad2 = Radiobutton(root, text="Gosper curve", variable=var, value=2)

rad0.grid(row=1, column=0, padx=5, sticky="w")
rad1.grid(row=2, column=0, padx=5, sticky="w")
rad2.grid(row=3, column=0, padx=5, sticky="w")

Label(root,text='Iteration\nnumber:').grid(row=0,column=1, padx=5, pady=5,sticky="e")

Entry= Entry(root, width=5, font='Arial 10')
Entry.grid(row=1, column=1, padx=10, pady=5, sticky="e")

but = Button(root, width=5, text='Go', command=curve_type)
but.grid(row=3, column=1, padx=10, pady=5, sticky="e")

screen.exitonclick()
root.mainloop()
