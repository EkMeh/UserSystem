import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
#Create form LOGIN UP window / form LOGIN UP
def formLoginUp():
    global li_label
    global li
    global lg
    global lanMet
    global ok_b
    global bk_i
    global un_i
    global ps_i
    global users_field
    global password_field
    global submitOne
    global result_label
    formL = tk.Toplevel()
    # Set title
    formL.title("LOG IN FORM")
    # Set background
    formL.configure(background='light green')
    # Set logo
    formL.tk.call('wm', 'iconphoto', formL._w, tk.PhotoImage(file='src\\logoicon.png'))
    # Set size window
    formL.geometry("480x420+400+40")
    # Set max-size window
    formL.maxsize(480, 600)
    # Create langue icon
    li = tk.PhotoImage(file="src\\language.png")
    li_label = tk.Label(formL, image=li).place(x=367, y=5)
    # Defination combobox values name
    lg = tk.StringVar()
    # Create combobox / lanMet
    lanMet = ttk.Combobox(formL, height=5, width=3, textvariable=lg, font="Arial 11")
    lanMet['values'] = ('BG', 'EN')
    lanMet.place(x=390, y=4)
    lanMet.current(0)
    # Create combobox button / ok_b
    ok_b = tk.Button(formL, text="OK", bg="gray", font="Verdana 8 bold", activebackground="green")
    ok_b.place(x=440, y=5)
    # Set User Icon
    bk_i = tk.PhotoImage(file="src\\users.png")
    bk_i_l = tk.Label(formL, image=bk_i).place(x=175, y=30)
    un_i = tk.PhotoImage(file="src\\username.png")
    un_i_l = tk.Label(formL, image=un_i).place(x=50, y=200)
    ps_i = tk.PhotoImage(file="src\\password.png")
    ps_i_l = tk.Label(formL, image=ps_i).place(x=50, y=270)
    # Set User Label
    username_label33 = tk.Label(formL, text="Username", bg="light green", font="bold 14").place(x=100, y=205)
    password_label44 = tk.Label(formL, text="Password", bg="light green", font="bold 14").place(x=100, y=275)
    # Set User Entry
    users_field = Entry(formL, font="bold 14")
    password_field = Entry(formL, font="bold 14", show="*")
    users_field.place(x=200, y=205)
    password_field.place(x=200, y=275)
    # Set User Button
    submitOne = Button(formL, text="LOG IN", fg="Black", bg="Red", font="Verdana 14 bold ", width="18")
    submitOne.place(x=125, y=340)
    # Set Info Label
    result_label = tk.Label(formL, font="Verdana 9 bold ", bg="light green", fg="red")
    result_label.config(text="")
    result_label.place(x=120, y=310)