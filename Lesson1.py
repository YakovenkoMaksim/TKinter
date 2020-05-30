from tkinter import *

root = Tk()

root.title('My first GUI app')
# root.iconbitmap('python.ico')
root.geometry('600x400+450+250') # w*h+x+y
root.resizable(False, False)
# root.config(bg='grey')
root['bg'] = 'grey'

root.mainloop()
