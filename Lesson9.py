from tkinter import *

root = Tk()
root.title('Grid')
root.geometry('800x400+550+200')

f_menu = Frame(root, bg='#1f252a', height=40)
f_text = Frame(root)
f_menu.pack(fill=X)
f_text.pack(fill=BOTH, expand=1)

l_menu = Label(f_menu, text='Menu', bg='#2b3239', fg='#c6dec1', font='Arial 10')
l_menu.place(x=10, y=10)


def add_str():
    t.insert('2.4', 'Hello ')


def del_str():
    # t.delete('2.4', '2.10')
    t.delete('1.0', END)


def get_str():
    print(t.get('1.0', END))


btn_add = Button(root, text='Add', command=add_str).place(x=50, y=10)
btn_del = Button(root, text='Delete', command=del_str).place(x=90, y=10)
btn_get = Button(root, text='Get', command=get_str).place(x=140, y=10)


t = Text(f_text, bg='#343d46', fg='#c6dec1', padx=10, pady=10, wrap=WORD, font='Arial 14', insertbackground='#eda756',
         selectbackground='#4e5a65', spacing3=10, width=30)
t.pack(fill=BOTH, expand=1, side=LEFT)

scroll = Scrollbar(f_text, command=t.yview)
scroll.pack(fill=Y, side=LEFT)
t.config(yscrollcommand=scroll.set)

root.mainloop()
