from tkinter import *

root = Tk()
root.title('TopLevel')
root.geometry('300x200+550+300')


def open_win():
    win = Toplevel()
    win.geometry('200x100+600+350')
    l = Label(win, text='Hello from TopLevel', bg='#000', fg='#fff').pack(expand=1, fill=BOTH)


Button(root, text='Open', command=open_win, padx=40, pady=5).place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
