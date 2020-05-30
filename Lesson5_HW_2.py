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

root = Tk()
root.title('Rainbow')


def get_color(text_color, hex_color):
    entry_color_number.delete(0, END)
    entry_color_number.insert(END, hex_color)
    label_color['text'] = text_color


label_color = Label(root)
label_color.pack()

entry_color_number = Entry(root, width=30, justify=CENTER)
entry_color_number.pack()

btn_red = Button(root, bg='#ff0000', command=lambda: get_color('Red', '#ff0000')).pack(fill=X)

btn_orange = Button(root, bg='#ff7d00', command=lambda: get_color('Orange', '#ff7d00')).pack(fill=X)

btn_yellow = Button(root, bg='#ffff00', command=lambda: get_color('Yellow', '#ffff00')).pack(fill=X)

btn_green = Button(root, bg='#00ff00', command=lambda: get_color('Green', '#00ff00')).pack(fill=X)

btn_lightblue = Button(root, bg='#007dff', command=lambda: get_color('Lightblue', '#007dff')).pack(fill=X)

btn_blue = Button(root, bg='#0000ff', command=lambda: get_color('Blue', '#0000ff')).pack(fill=X)

btn_purple = Button(root, bg='#7d00ff', command=lambda: get_color('Purple', '#7d00ff')).pack(fill=X)

root.mainloop()
