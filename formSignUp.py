import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *


#Create form SIGN UP window / form SING UP
def formSingUP():
    global li_label
    global li
    global lg
    global lanMet
    global ok_b
    global bk_i
    global fn_i
    global ln_i
    global un_i
    global ps_i
    global first_name_field
    global last_name_field
    global users_field
    global password_field
    global submit
    global result_label
    formS=tk.Toplevel()
    #Set title
    formS.title("SING UP FORM")
    #Set background
    formS.configure(background='light green')
    #Set logo
    formS.tk.call('wm', 'iconphoto', formS._w, tk.PhotoImage(file='src\logoicon.png'))
    #Set size window
    formS.geometry("480x600+400+40")
    #Set max-size window
    formS.maxsize(480,600)
    #Create langue icon
    li = tk.PhotoImage(file="src\\language.png")
    li_label = tk.Label(formS, image=li).place(x=367, y=5)
    #Defination combobox values name
    lg = tk.StringVar()
    #Create combobox / lanMet
    lanMet = ttk.Combobox(formS, height=5, width=3, textvariable=lg, font="Arial 11")
    lanMet['values'] = ('BG','EN')
    lanMet.place(x=390, y=4)
    #Create combobox button / ok_b
    ok_b = tk.Button(formS, text="OK", bg="gray", font="Verdana 8 bold", activebackground="green")
    ok_b.place(x=440, y=5)
    lanMet.current(0)
    #Set User Icon
    bk_i = tk.PhotoImage(file="src\\users.png")
    bk_i_l = tk.Label(formS, image=bk_i).place(x=175, y=30)
    fn_i = tk.PhotoImage(file="src\\firstname.png")
    fn_i_l = tk.Label(formS, image=fn_i).place(x=50, y=200)
    ln_i = tk.PhotoImage(file="src\\lastname.png")
    ln_i_l = tk.Label(formS, image=ln_i).place(x=50, y=270)
    un_i = tk.PhotoImage(file="src\\username.png")
    un_i_l = tk.Label(formS, image=un_i).place(x=50, y=340)
    ps_i = tk.PhotoImage(file="src\\password.png")
    ps_i_l = tk.Label(formS, image=ps_i).place(x=50, y=410)
    #Set User Label
    firstname_label11 = tk.Label(formS, text="Firstname", bg="light green", font="bold 14").place(x=100, y=205)

    lastname_label22 = tk.Label(formS, text="Lastname", bg="light green", font="bold 14").place(x=100, y=275)

    username_label33 = tk.Label(formS, text="Username", bg="light green", font="bold 14").place(x=100, y=345)

    password_label44 = tk.Label(formS, text="Password", bg="light green", font="bold 14").place(x=100, y=415)
    #Set User Entry
    first_name_field = Entry(formS,font="bold 14")
    last_name_field = Entry(formS,font="bold 14")
    users_field = Entry(formS,font="bold 14")
    password_field = Entry(formS,font="bold 14", show="*")
    first_name_field.place(x=200,y=205)
    last_name_field.place(x=200,y=275)
    users_field.place(x=200,y=345)
    password_field.place(x=200, y=415)
    #Set User Button
    submit = Button(formS, text="SIGN UP", fg="Black",bg="Red", font="Verdana 14 bold ",width="18")
    submit.place(x=125, y=480)
    #Set Info Label
    result_label = tk.Label(formS, font="Verdana 9 bold ", bg="light green", fg="red")
    result_label.config(text="")
    result_label.place(x=120, y=450)