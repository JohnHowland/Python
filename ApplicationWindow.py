from Tkinter import *
from ttk import *

class ApplicationWindow():
    def __init__(self, master):
        self.master = master
        self.master.resizable(FALSE, FALSE)
        self.frame = Frame(self.master)
        
##        self.textFrame = Frame(self.master)
        self.initUI()
        
    def initUI(self):
        self.master.title("Windows")
        self.style = Style()
        self.style.theme_use("default")
        self.frame.grid(row = 0, column = 0, sticky=N+E+S+W)
            
##        Button(master, text="Button {0}".format(c)).grid(row=6,column=c,sticky=E+W)
##        self.frame.columnconfigure(1, pad=5, weight=10)
##        self.frame.columnconfigure(8, pad=7)
##        self.frame.rowconfigure(1, pad=5, weight=10)
##        self.frame.rowconfigure(12, pad=7)
        
        self.lbl = Label(self.frame, text="Windows")
        self.lbl.grid(row=0, column=0, sticky=W, padx=5, pady=5)

        self.area = Listbox(self.frame)
        self.area.grid(row=1, column=0, rowspan=10, columnspan=2, padx=5, pady=5)
        
        self.itemName = Entry(self.frame, width = 18)
        self.itemName.grid(row=1, column=3, padx=5, sticky = W)
        self.itemLabel = Label(self.frame, text = "Item Name")
        self.itemLabel.grid(row=0, column=3, pady=2, padx=5, sticky=W)

        self.itemLifespan_Before = Label(self.frame, text = "Item Lifespan Before")
        self.itemLifespan_Before.grid(row=3, column=3, pady=2, padx=5, sticky=W)
        self.itemLifespan_Before = Entry(self.frame, width = 8)
        self.itemLifespan_Before.grid(row=4, column=3, padx=5, sticky=W)

        self.itemLifespan_After = Entry(self.frame, width = 8)
        self.itemLifespan_After.grid(row=6, column=3, padx=5, sticky=W)
        self.itemLifespan_After = Label(self.frame, text = "Item Lifespan After")
        self.itemLifespan_After.grid(row=5, column=3, pady=2, padx=5, sticky=W)

        self.cbtn = Button(self.frame, text="Close", command = self.frame.quit)
        self.cbtn.grid(row=12, column=4, padx=5, pady = 5, sticky=E+S)
        
##        self.hbtn = Button(self.frame, text="Help", command = helpWindow)
##        self.hbtn.grid(row=5, column=0, padx=5)
##
##        self.obtn = Button(self.frame, text="OK", command = test)
##        self.obtn.grid(row=5, column=3)

    def InsertListItem(self, arg):
        self.area.insert(END, arg)
        
def ListItem(PutMessageString):
    windowVariable.InsertListItem(PutMessageString) 
        
def helpWindow():
    print "You made it to the Help Window"

def activate():
    print "You are now activated"

def InitializeMainWindow(windowIndex):
    global windowVariable
    windowIndex.geometry('330x240+50+50')
    windowVariable = ApplicationWindow(windowIndex)
##    root.mainloop()
