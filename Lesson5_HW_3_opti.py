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

colors = {
    '#ff0000': 'Красный',
    '#ff7d00': 'Оранжевый',
    '#ffff00': 'Желтый',
    '#00ff00': 'Зеленый',
    '#007dff': 'Голубой',
    '#0000ff': 'Синий',
    '#7d00ff': 'Фиолетовый',
}
for k, v in colors.items():
    Button(root, bg=k, command=lambda text=v, hex=k: get_color(text, hex)).pack(fill=X)

root.mainloop()
