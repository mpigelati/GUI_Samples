import tkinter as tk
import tkinter as ttk




root = tk.Tk()
root.title("Label Button")
alabel= ttk.Label(root,text="hellow worls")
alabel.grid(column =50,row=60 )

#def click_Me ():
    #print("hellow click me ")
    #action.configure(text="** I have been checked **" )
    #alabel.configure(foreground='red')

#action =tkk.Button(root,text="Click me!=",command= click_Me())
#action.grid(column=10,row= "20")
root.mainloop()
