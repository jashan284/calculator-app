from tkinter import *

root = Tk()
root.title("My Calculator")
root.geometry("320x450")
root.configure(bg="black")

entry = Entry(root, width=18, font=("Arial", 22), bd=8, justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10)

def click(num):
    entry.insert(END, num)

def clear():
    entry.delete(0, END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, result)
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

# Button style
btn_style = {"width":5, "height":2, "font":("Arial", 16)}

buttons = [
    ('7',1,0),('8',1,1),('9',1,2),('/',1,3),
    ('4',2,0),('5',2,1),('6',2,2),('*',2,3),
    ('1',3,0),('2',3,1),('3',3,2),('-',3,3),
    ('0',4,0),('C',4,1),('=',4,2),('+',4,3)
]

for (text,row,col) in buttons:
    if text == "=":
        Button(root, text=text, command=calculate, bg="orange", **btn_style).grid(row=row, column=col, padx=5, pady=5)
    elif text == "C":
        Button(root, text=text, command=clear, bg="red", **btn_style).grid(row=row, column=col, padx=5, pady=5)
    else:
        Button(root, text=text, command=lambda t=text: click(t), bg="gray", **btn_style).grid(row=row, column=col, padx=5, pady=5)

root.mainloop()