from Tkinter import *
from ttk import *
import Database as db
from time import strftime

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

        self.itemDatePurchased = Entry(self.frame, width = 15)
        self.itemDatePurchased.grid(row=4, column=3, padx=5, sticky=W)
        self.itemDatePurchased_LABEL = Label(self.frame, text = "Date Purchased")
        self.itemDatePurchased_LABEL.grid(row=3, column=3, pady=2, padx=5, sticky=W)

        self.itemSelfLifeTime = Entry(self.frame, width = 15)
        self.itemSelfLifeTime.grid(row=6, column=3, padx=5, sticky=W)
        self.itemSelfLifeTime_LABEL = Label(self.frame, text = "Date Expires")
        self.itemSelfLifeTime_LABEL.grid(row=5, column=3, pady=2, padx=5, sticky=W)

        self.CloseButton = Button(self.frame, text="Close", command = self.frame.quit)
        self.CloseButton.grid(row=12, column=4, padx=5, pady = 5, sticky=E+S)
        
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
            self.itemDatePurchased.delete(0, END)
            self.itemSelfLifeTime.delete(0, END)
            listSelection = self.area.curselection()
            self.itemName.insert(0, foodInKitchen[listSelection[0]].itemName)
            self.itemDatePurchased.insert(0, foodInKitchen[listSelection[0]].datePurchased)
            self.itemSelfLifeTime.insert(0, foodInKitchen[listSelection[0]].itemShelfLife)
        elif widgetSelected == self.CloseButton:
            self.frame.quit
            

            
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

def CalculateSpoilTimes():
    print "You are not calculating the times."

    timeString = strftime('%X %x %Z')
    foundTimeNow = re.search("(.*?):(.*?):[0-9][0-9] (.*?)/(.*?)/(.*?) .*", timeString)    
    if foundTimeNow:
        hourNow = foundTimeNow.group(1)
        minuteNow = foundTimeNow.group(2)
        monthNow = foundTimeNow.group(3)
        dayNow = foundTimeNow.group(4)
        yearNow = int(foundTimeNow.group(5)) + 2000
        
##    length = len(foodInKitchen)
##    for i in range(0, length):
##        foundTimeExpired = re.search("(.*?):(.*?) (.*?)\.(.*?)\.(.*?)$", foodInKitchen[i].itemTimeExpires)
##        if foundTimeExpired:
##            hourExpired = foundTimeExpired.group(1)
##            minuteExpired = foundTimeExpired.group(2)
##            monthExpired = foundTimeExpired.group(3)
##            dayExpired = foundTimeExpired.group(4)
##            yearExpired = foundTimeExpired.group(5)
##            
##            TimeNow = db.TimeClass(hourNow, minuteNow, monthNow, dayNow, yearNow)
##            TimeItem = db.TimeClass(hourExpired, minuteExpired, monthExpired, dayExpired, yearExpired)
##            db.CheckIfItemsAreExpired(TimeNow, TimeItem)
            
def InsertListData(listIndex):
    print listIndex

index = Tk()
InitializeMainWindow(index)
foodInKitchen = db.ReadInDatabase()
AccessDatabase()
index.after(10, CalculateSpoilTimes)
index.mainloop()

