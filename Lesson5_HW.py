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


def color_red():
    entry_color_number.delete(0, END)
    entry_color_number.insert(END, '#ff0000')
    label_color['text'] = 'RED'


def color_orange():
    entry_color_number.delete(0, END)
    entry_color_number.insert(END, '#ff7d00')
    label_color['text'] = 'ORANGE'


def color_yellow():
    entry_color_number.delete(0, END)
    entry_color_number.insert(END, '#ffff00')
    label_color['text'] = 'YELLOW'


def color_green():
    entry_color_number.delete(0, END)
    entry_color_number.insert(END, '#00ff00')
    label_color['text'] = 'GREEN'


def color_lightblue():
    entry_color_number.delete(0, END)
    entry_color_number.insert(END, '#007dff')
    label_color['text'] = 'LIGHTBLUE'


def color_blue():
    entry_color_number.delete(0, END)
    entry_color_number.insert(END, '#0000ff')
    label_color['text'] = 'BLUE'


def color_purple():
    entry_color_number.delete(0, END)
    entry_color_number.insert(END, '#7d00ff')
    label_color['text'] = 'PURPLE'


label_color = Label(root)
label_color.pack()

entry_color_number = Entry(root, width=30, justify=CENTER)
entry_color_number.pack()

btn_red = Button(root, bg='#ff0000', command=color_red).pack(fill=X)

btn_orange = Button(root, bg='#ff7d00', command=color_orange).pack(fill=X)

btn_yellow = Button(root, bg='#ffff00', command=color_yellow).pack(fill=X)

btn_green = Button(root, bg='#00ff00', command=color_green).pack(fill=X)

btn_lightblue = Button(root, bg='#007dff', command=color_lightblue).pack(fill=X)

btn_blue = Button(root, bg='#0000ff', command=color_blue).pack(fill=X)

btn_purple = Button(root, bg='#7d00ff', command=color_purple).pack(fill=X)

root.mainloop()
