'''
Напишите программу, состоящую из семи кнопок, цвета которых соответствуют цветам радуги.
При нажатии на ту или иную кнопку в текстовое поле должен вставляться код цвета,
а в метку – название цвета.
#ff0000: Красный
#ff7d00: Оранжевый
#ffff00: Желтый
#00ff00: Зеленый
#007dff: Голубой
#0000ff: Синий
#7d00ff: Фиолетовый
'''

from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Rainbow')


def red():
    pass


label_color = Label(root)
label_color.pack()

entry_color_number = Entry(root, width=30, justify=CENTER)
entry_color_number.pack()

ttk.Style().configure('btn_red', bg='#ff0000')

btn_red = ttk.Button(root)
btn_red.pack(fill=X)

btn_orange = Button(root, bg='orange')
btn_orange.pack(fill=X)

btn_yellow = Button(root, bg='yellow')
btn_yellow.pack(fill=X)

btn_green = Button(root, bg='green')
btn_green.pack(fill=X)

btn_lightblue = Button(root, bg='lightblue')
btn_lightblue.pack(fill=X)

btn_blue = Button(root, bg='blue')
btn_blue.pack(fill=X)

btn_purple = Button(root, bg='purple')
btn_purple.pack(fill=X)

root.mainloop()
