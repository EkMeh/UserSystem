import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
import formLogIn
import formSignUp

#Create MAIN WINDOW
def form_Si_Lo():
    global loginUp
    global singUp
    global lg
    global lanMet
    global form_S_L
    form_S_L=tk.Tk()
    #Set main window name
    form_S_L.title("MAIN WINDOW")
    #Set main window size
    form_S_L.geometry("360x260+520+250")
    #Set main window maxsize
    form_S_L.maxsize(360, 230)
    #Set software icon
    form_S_L.tk.call('wm', 'iconphoto', form_S_L._w, tk.PhotoImage(file='src\\logoicon.png'))
    #Set background
    form_S_L.configure(background='light green')
    #Create langue icon
    li = tk.PhotoImage(file="src\\language.png")
    li_label = tk.Label(form_S_L, image=li).place(x=240, y=5)
    #Defination combobox values name
    lg = tk.StringVar()
    #Create combobox / lanMet
    lanMet = ttk.Combobox(form_S_L, height=5, width=3, textvariable=lg, font="Arial 11")
    lanMet['values'] = ('BG','EN')
    lanMet.current(0)
    lanMet.place(x=265, y=4)
    #Create combobox button / ok_b
    ok_b = tk.Button(form_S_L, text="OK", bg="gray", font="Verdana 8 bold", activebackground="green")
    ok_b.place(x=317, y=5)
    #Create button login up / loginUp
    loginUp=tk.Button(form_S_L, text="LOG IN", bg="orange", font="Verdana 14 bold", width="18" , activebackground="green",command=formLogIn.formLoginUp)
    loginUp.place(x=60, y=80)
    #Create button sing up / signUp
    singUp=tk.Button(form_S_L, text="SIGN IN", bg="orange", font="Verdana 14 bold", width="18" , activebackground="green", command=formSignUp.formSingUP)
    singUp.place(x=60, y=130)
    form_S_L.mainloop()


form_Si_Lo()
