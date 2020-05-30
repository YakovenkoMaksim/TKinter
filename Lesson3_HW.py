from tkinter import *

root = Tk()
root.title('Mini calculator')
root.geometry('600x400+450+250')

a = 10
b = 5


def add():
    global a
    global b
    print(a + b)


def sub():
    global a
    global b
    print(a - b)


def mult():
    global a
    global b
    print(a * b)


def dev():
    global a
    global b
    print(a / b)


btn_add = Button(root, text='Add', width=10, pady=5, command=add)
btn_add.pack()
btn_sub = Button(root, text='Subtract', width=10, pady=5, command=sub)
btn_sub.pack()
btn_mult = Button(root, text='Multiply', width=10, pady=5, command=mult)
btn_mult.pack()
btn_dev = Button(root, text='Divide', width=10, pady=5, command=dev)
btn_dev.pack()

root.mainloop()
