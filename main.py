# from tkinter import *
# from tkinter import ttk
# root = Tk()
# root.geometry("800x800")
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# btn = ttk.Button(frm, text="Quit", command=root.destroy, width=15, )
# btn.pack()
# root.mainloop()

import tkinter as tk

def vict():
    lable.config(text='ПОБЕДА')
    btn_yes.config(text='ZOV')
    btn_no.config(text='ЗОВ', bg='Green', width=30, height=10, fg='White')


def bomb():
    lable.config(text='Вы захватили Зеленского?')
    btn_yes.config(text='Убить', command=vict)
    btn_no.config(text='Дать кокаина', width=15, height=1, bg='Red')

def begin_svo():
    lable.config(text='Что разбомбить?')
    btn_yes.config(text='Детский дом', command=bomb)
    btn_no.config(text='Больница для детей', bg='Green', width=30, height=10, fg='White', command=bomb)

# Create the main window
root = tk.Tk()
root.title("Симулятор ПУТИНА")
root.geometry("800x400")

image = tk.PhotoImage(file='777.png')
bg_lable = tk.Label(root, image=image)
bg_lable.place(x=0, y=0, relwidth=1, relheight=1)
lable = tk.Label(root, bg='Gray', text='Начать СВО?', fg='White')
lable.place(x=300, y=250, width=150, height=75)

# Create buttons with different sizes
btn_yes = tk.Button(root, text="Начать СВО", width=30, height=10, bg='Green', fg='White', activebackground='Green', command=begin_svo)
btn_yes.pack(side='right')


btn_no = tk.Button(root, text="НЕ начинать СВО", width=15, height=1, bg='Red')
btn_no.pack(side='left')


# Run the main event loop
root.mainloop()
