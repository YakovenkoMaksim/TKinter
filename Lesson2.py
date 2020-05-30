from tkinter import *

root = Tk()

root.title('Button lesson')
root.geometry('600x400+450+250')


def clicked():
    print('Clicked')


# btn = Button(root, text='Button', command=clicked, font='Arial 16 italic')
btn = Button(root, text='Button')
btn.configure(width=10)
btn['font'] = 'Arial 15'
btn.pack()

root.mainloop()
