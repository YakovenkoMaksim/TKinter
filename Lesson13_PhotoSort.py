from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import os
from datetime import datetime

root = Tk()
root.title('PhotoSort')
root.geometry('500x100+300+300')

s = ttk.Style()
s.configure('my.TButton', font=('Helvetica', 20))


def choose_dir():
    dir_path = filedialog.askdirectory()
    e_path.delete(0, END)
    e_path.insert(0, dir_path)


def f_start():
    cur_path = e_path.get()
    if cur_path:
        for folder, subfolders, files in os.walk(cur_path):
            for file in files:
                path = os.path.join(folder, file)
                mtime = os.path.getmtime(path)
                date = datetime.fromtimestamp(mtime)
                date = date.strftime("%Y%m%d")
                date_folder = os.path.join(cur_path, date)
                if not os.path.exists(date_folder):
                    os.mkdir(date_folder)
                os.rename(path, os.path.join(date_folder, file))
        messagebox.showinfo('Выполнено!', 'Сортировка выполнена успешно')
        e_path.delete(0, END)
    else:
        messagebox.showwarning('Ошибка!', 'Выберите папку с фотографиями')


frame = Frame(root)
frame.pack(padx=10, pady=15, fill=X)

e_path = Entry(frame)
e_path.pack(side=LEFT, ipady=2, expand=True, fill=X)

btn_dialog = ttk.Button(frame, text='Выбрать папку', command=choose_dir)
btn_dialog.pack(side=LEFT, padx=10)

btn_start = ttk.Button(root, text='Начать', style='my.TButton', command=f_start)
btn_start.pack(fill=X, padx=10)

root.mainloop()
