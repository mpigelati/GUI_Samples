import Tkinter as tk
class Application(tk.Frame):
    def __init__(self,master=None):
        tk.frame.__init__(self,master)
        self.grid()
        self.creatWidget()
    def createWidget(self):
        self.quit_Button= tk.Button(self,text= "Quit",command=self.quit)
        self.quit_Button.grid()

app= Application()
app.master.title="sample Application"
app.mainloop()
