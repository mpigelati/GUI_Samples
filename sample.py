import  tkinter as tk
import tkinter as ttk
win=tk.Tk()
win.title("Label Button")
aLabel = ttk.Label(win, text="A Label")
aLabel.grid(column=0, row=0) # 1


def clickMe():
 print("click me")
 action.configure(text="** I have been Clicked! **")
 aLabel.configure(foreground='red') # 5

action = ttk.Button(win, text="Click Me!", command=clickMe)
action.grid(column=1, row=0)
win.mainloop()