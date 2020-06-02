from tkinter import *
from tkinter import ttk

root = Tk()
root.title('ttk')
root.geometry('300x250+550+300')

s = ttk.Style()
s.theme_use('clam')


# s.configure('TButton', padding=6)
#
# Button(root, text='Button1', padx=40, pady=5).pack(pady=10)
# ttk.Button(root, text='Button2', width=11).pack()
# ttk.Button(root, text='Button2', width=11).pack(pady=10)
#
# Entry(root).pack(pady=10)
# ttk.Entry(root).pack()

def choose(event):
    print(select.current(), select.get())


select = ttk.Combobox(root, values=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
select.place(relx=0.5, rely=0.5, anchor=CENTER)
select.current(0)
select.bind('<<ComboboxSelected>>', choose)

root.mainloop()
