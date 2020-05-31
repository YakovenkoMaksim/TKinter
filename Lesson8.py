from tkinter import *

root = Tk()
root.title('Place')
root.geometry('400x400+550+200')

# l1 = Label(root, text='Hello world', bg='#3498db', fg='#fff', font='16', padx=20, pady=8)
# l1.place(x=0, y=0)
# l2 = Label(root, text='Hello world', bg='#3498db', fg='#fff', font='16', padx=20, pady=8)
# l2.place(relx=0.5, rely=0.5, anchor=CENTER)

# btn1 = Button(text='Button1', bg='#3498db', fg='#000', font='16', padx=20, pady=8)
# btn1.place(x=0, y=0)
# btn2 = Button(text='Button2', bg='#3498db', fg='#000', font='16', padx=20, pady=8)
# btn2.place(relx=0.5, rely=0.5, anchor=CENTER)
# btn3 = Button(text='Button3', bg='#3498db', fg='#000', font='16', padx=20, pady=8)
# btn3.place(relx=1, rely=1, anchor='se')

l = Label(bg='#000').place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)

root.mainloop()
