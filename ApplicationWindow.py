from Tkinter import *
from ttk import *
import Database as db

class ApplicationWindow():
    def __init__(self, master):
        self.master = master
        self.master.resizable(FALSE, FALSE)
        self.frame = Frame(self.master)
        self.master.bind('<Button-1>', self.click_button)
        self.master.curIndex = None
        
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

        self.area = Listbox(self.frame, selectmode=SINGLE)
        self.area.grid(row=1, column=0, rowspan=10, columnspan=2, padx=5, pady=5)
        
        self.itemName = Entry(self.frame, width = 18)
        self.itemName.grid(row=1, column=3, padx=5, sticky = W)
        self.itemName_LABEL = Label(self.frame, text = "Item Name")
        self.itemName_LABEL.grid(row=0, column=3, pady=2, padx=5, sticky=W)

        self.itemLifespan_Before_LABEL = Label(self.frame, text = "Item Lifespan Before")
        self.itemLifespan_Before_LABEL.grid(row=3, column=3, pady=2, padx=5, sticky=W)
        self.itemLifespan_Before = Entry(self.frame, width = 8)
        self.itemLifespan_Before.grid(row=4, column=3, padx=5, sticky=W)

        self.itemLifespan_After = Entry(self.frame, width = 8)
        self.itemLifespan_After.grid(row=6, column=3, padx=5, sticky=W)
        self.itemLifespan_After_LABEL = Label(self.frame, text = "Item Lifespan After")
        self.itemLifespan_After_LABEL.grid(row=5, column=3, pady=2, padx=5, sticky=W)

        self.cbtn = Button(self.frame, text="Close", command = self.frame.quit)
        self.cbtn.grid(row=12, column=4, padx=5, pady = 5, sticky=E+S)
        
##        self.hbtn = Button(self.frame, text="Help", command = helpWindow)
##        self.hbtn.grid(row=5, column=0, padx=5)
##
##        self.obtn = Button(self.frame, text="OK", command = test)
##        self.obtn.grid(row=5, column=3)

    def InsertListItem(self, arg):
        self.area.insert(END, arg)

    def click_button(self, event):
        widgetSelected = event.widget
        if widgetSelected == self.area:
            self.itemName.delete(0, END)
            self.itemLifespan_After.delete(0, END)
            self.itemLifespan_Before.delete(0, END)
            listSelection = self.area.curselection()
            self.itemName.insert(0, foodInKitchen[listSelection[0]].itemName)
            self.itemLifespan_After.insert(0, foodInKitchen[listSelection[0]].itemTimeAfter)
            self.itemLifespan_Before.insert(0, foodInKitchen[listSelection[0]].itemTimeBefore)
            
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

def AccessDatabase():
    length = len(foodInKitchen)
    for i in xrange(0,length):
        ListItem(foodInKitchen[i].itemName)
        
def InsertListData(listIndex):
    print listIndex

index = Tk()
InitializeMainWindow(index)
foodInKitchen = db.ReadInDatabase()
index.after(1000, AccessDatabase)
index.mainloop()

