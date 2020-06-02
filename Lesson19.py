from tkinter import ttk
from ttkthemes import ThemedTk

# root = ThemedTk(theme='arc')
# root = ThemedTk(theme='clearlooks')
# root = ThemedTk(theme='plastic')
root = ThemedTk(theme='radiance')
root.title('ThemedTk')
root.geometry('300x250+550+300')

ttk.Button(root, text='Button').pack(pady=10)
ttk.Entry(root).pack()

root.mainloop()
