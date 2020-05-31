from tkinter import *

root = Tk()
root.title('Grid')
root.geometry('800x400+550+200')

main_menu = Menu(root)
root.config(menu=main_menu)


# main_menu.add_command(label='File')
# main_menu.add_command(label='About')

def about_program():
    pass


# File
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Open')
file_menu.add_command(label='Save')
file_menu.add_separator()
file_menu.add_command(label='Exit')
main_menu.add_cascade(label='File', menu=file_menu)

# About
help_menu = Menu(main_menu, tearoff=0)
help_menu_sub = Menu(help_menu, tearoff=0)
help_menu_sub.add_command(label='Online')
help_menu_sub.add_command(label='Offline')
help_menu.add_cascade(label='Help', menu=help_menu_sub)
main_menu.add_cascade(label='FAQ', menu=help_menu)
help_menu.add_command(label='About', command='about_program')

# f_menu = Frame(root, bg='#1f252a', height=40)
# f_menu.pack(fill=X)
f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

t = Text(f_text, bg='#343d46', fg='#c6dec1', padx=10, pady=10, wrap=WORD, font='Arial 14', insertbackground='#eda756',
         selectbackground='#4e5a65', spacing3=10, width=30)
t.pack(fill=BOTH, expand=1, side=LEFT)

scroll = Scrollbar(f_text, command=t.yview)
scroll.pack(fill=Y, side=LEFT)
t.config(yscrollcommand=scroll.set)

root.mainloop()
