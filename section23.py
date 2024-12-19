# Clase 215: Creating a GUI Window and Adding Widgets
from tkinter import *

'''
window = Tk()

def km_to_miles():
    miles = float(e1_value.get())*1.6
    t1.insert(END, miles)

b1 = Button(window, text="Execute", command=km_to_miles)
b1.grid(row=0, column=0 )

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)

window.mainloop()
'''

window= Tk()

def kg_convert():
    grams = float(e1_value.get())*1000
    t1.insert(END, grams)
    
    pounds = float(e1_value.get())*2.20462
    t2.insert(END, pounds)

    ounces = float(e1_value.get())*35.274
    t3.insert(END, ounces)

label=Label(window,text="Kg")
label.grid(row=0,column=1)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=2)

b1 = Button(window, text="Convert", command=kg_convert)
b1.grid(row=0, column=3)

t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=1)
t2 = Text(window, height=1, width=20)
t2.grid(row=1, column=2)
t3 = Text(window, height=1, width=20)
t3.grid(row=1, column=3)

window.mainloop()