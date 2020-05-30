from tkinter import *

root = Tk()
root.title('Grid')
root.geometry('600x400+450+250')

f = Frame(root)
f.pack(pady=10)

btn_list = [
    ' 7', '8', '9',
    ' 4', '5', '6',
    ' 1', '2', '3',
    ' 0',
]

row = 0
column = 0

for i in btn_list:
    if i == '0':
        Button(f, text=i, padx=10, pady=5).grid(row=row, columnspan=3)
    else:
        Button(f, text=i, padx=10, pady=5).grid(row=row, column=column)
    column += 1
    if column == 3:
        column = 0
        row += 1

# btn7 = Button(f, text='7', padx=10, pady=5).grid(row=0, column=0)
# btn8 = Button(f, text='8', padx=10, pady=5).grid(row=0, column=1)
# btn9 = Button(f, text='9', padx=10, pady=5).grid(row=0, column=2)
# btn4 = Button(f, text='4', padx=10, pady=5).grid(row=1, column=0)
# btn5 = Button(f, text='5', padx=10, pady=5).grid(row=1, column=1)
# btn6 = Button(f, text='6', padx=10, pady=5).grid(row=1, column=2)
# btn1 = Button(f, text='1', padx=10, pady=5).grid(row=2, column=0)
# btn2 = Button(f, text='2', padx=10, pady=5).grid(row=2, column=1)
# btn3 = Button(f, text='3', padx=10, pady=5).grid(row=2, column=2)
# btn0 = Button(f, text='0', padx=10, pady=5).grid(row=3, columnspan=3)

root.mainloop()