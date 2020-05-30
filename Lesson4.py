from tkinter import *

root = Tk()
root.geometry('600x400+450+250')

l = Label(root, text='Текст в строке 1\n Строка 2\n Строка 3\n Строка 4\n Строка 5', bg='red', fg='#fff',
          font=('Comic Sans MS', 10, 'bold'), justify=LEFT, width=50, height=10, anchor=SW)
l.pack()

# img = PhotoImage(file='python-logo.png')
# l_logo = Label(root, image=img)
# l_logo.pack()
root.mainloop()
