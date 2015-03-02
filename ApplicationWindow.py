from Tkinter import *
from ttk import *
import Database as db
import string
from time import strftime
from PIL import Image, ImageTk

itemFilepath = "C:\\Projects\\Testing Location\\Smart Kitchen\\Product Image\\00000000.gif"


#############################  Main Application Window  ##################################
class ApplicationWindow():
    def __init__(self, master):
        self.master = master
##        self.master.resizable(FALSE, FALSE)
        self.frame = Frame(self.master)
        self.master.bind('<Button-1>', self.click_button)
##        self.master.curIndex = None
        
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

        self.area = Listbox(self.frame, selectmode=SINGLE, height=17, width=25)
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
        self.itemSelfLifeTime.grid(row=4, column=4, padx=5, sticky=W)
        self.itemSelfLifeTime_LABEL = Label(self.frame, text = "Expire Time")
        self.itemSelfLifeTime_LABEL.grid(row=3, column=4, pady=2, padx=5, sticky=W)

        itemFilepath = "C:\\Projects\\Testing Location\\Smart Kitchen\\Product Image\\NoPictureAvailable.gif"
        self.photo = PhotoImage(file = itemFilepath)
        self.imageCanvas = Canvas(self.frame, width=200, height=200)
        self.imageCanvas.grid(row=5, column=3, rowspan=6, columnspan=3, padx=5, pady=5)
        self.imageCanvas.create_image(100,100, image = self.photo)

##        self.photo = PhotoImage(Image.open(itemFilepath))
##        self.label = Label(image=self.photo)
##        self.label.image = photo # keep a reference!
##        label.pack()

##        itemImage = Image.open(itemFilepath)
##        self.itemPicture = PhotoImage(image=itemImage)
##        self.itemPicture.grid(row=3, column=3, rowspan=7, columnspan=4, padx=5, pady=5)

        self.CloseButton = Button(self.frame, text="Close", command = self.frame.quit)
        self.CloseButton.grid(row=12, column=4, padx=5, pady = 5, sticky=E+S)
        
##        self.hbtn = Button(self.frame, text="Help", command = helpWindow)
##        self.hbtn.grid(row=5, column=0, padx=5)
##
##        self.obtn = Button(self.frame, text="OK", command = test)
##        self.obtn.grid(row=5, column=3)

        self.ListButton = Button(self.frame, text="List", command = self.ShowList)
        self.ListButton.grid(row=12, column=0, padx=5, pady = 5, sticky=W+S)

#############################  Functions for Main Window  ##################################

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

            itemFilepath = "C:\\Projects\\Testing Location\\Smart Kitchen\\Product Image\\"+foodInKitchen[listSelection[0]].itemVIN+".gif"
            self.photo = PhotoImage(file = itemFilepath)
            self.imageCanvas.create_image(100,100, image = self.photo)
            
        elif widgetSelected == self.CloseButton:
            self.frame.quit

    def ShowList(self):
        FoodStructure = [[] for i in range(3)]
        global ListIndex
        global listWindowIndex
        listWindowIndex = Tk()
        ListIndex = ListWindow(listWindowIndex)
        InsertItems()
        
#############################  Food List Window  ##################################            
class ListWindow():
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.master.bind('<Button-1>', self.click_button)
        self.initUI()

    def initUI(self):
        self.master.title("List")
        self.style = Style()
        self.style.theme_use("default")
        self.frame.grid(row = 0, column = 0, sticky=N+E+S+W)

        self.GoodFrame = Frame(self.master)
        self.GoodFrame.grid(row=0, column=0, rowspan=10, columnspan=6)
        self.GoodFrame.grid_rowconfigure(0, weight=1)
        self.GoodFrame.grid_columnconfigure(0, weight=1)
        self.GoodScrollbar = Scrollbar(self.GoodFrame, orient=VERTICAL)
        self.GoodLabel = Label(self.GoodFrame, text="Good")
        self.GoodLabel.grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.GoodList = Listbox(self.GoodFrame, selectmode=SINGLE, yscrollcommand=self.GoodScrollbar, height=10, width=20)      
        self.GoodList.grid(row=1, column=0, rowspan=10, columnspan=5, padx=5, pady=5)
        self.GoodScrollbar.config(command=self.Goodyview)
        self.GoodScrollbar.grid(row=1, column=6, rowspan=10, sticky=N+S)
        
        self.OutSoonFrame = Frame(self.master)
        self.OutSoonFrame.grid(row=0, column=6, rowspan=10, columnspan=6)
        self.OutSoonFrame.grid_rowconfigure(0, weight=1)
        self.OutSoonFrame.grid_columnconfigure(0, weight=1)
        self.OutSoonScrollbar = Scrollbar(self.OutSoonFrame, orient=VERTICAL)
        self.OutSoonLabel = Label(self.OutSoonFrame, text="Out Soon")
        self.OutSoonLabel.grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.OutSoonList = Listbox(self.OutSoonFrame, selectmode=SINGLE, yscrollcommand=self.OutSoonScrollbar, height=10, width=20)
        self.OutSoonList.grid(row=1, column=0, rowspan=10, columnspan=5, padx=5, pady=5)
        self.OutSoonScrollbar.config(command=self.OutSoonyview)
        self.OutSoonScrollbar.grid(row=1, column=6, rowspan=10, sticky=N+S)
        
        self.BadFrame = Frame(self.master)
        self.BadFrame.grid(row=0, column=12, rowspan=10, columnspan=6)
        self.BadFrame.grid_rowconfigure(0, weight=1)
        self.BadFrame.grid_columnconfigure(0, weight=1) 
        self.BadScrollbar = Scrollbar(self.BadFrame, orient=VERTICAL)        
        self.BadLabel = Label(self.BadFrame, text="Spoiled")
        self.BadLabel.grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.BadList = Listbox(self.BadFrame, selectmode=SINGLE, yscrollcommand=self.BadScrollbar, height=10, width=20)
        self.BadList.grid(row=1, column=0, rowspan=10, columnspan=5, padx=5, pady=5)
        self.BadScrollbar.config(command=self.Badyview)
        self.BadScrollbar.grid(row=1, column=6, rowspan=10, sticky=N+S)

        self.CloseFrame = Frame(self.master)
        self.CloseFrame.grid(row=11, column=0, columnspan=20) 
        self.CloseButton = Button(self.CloseFrame, text="Close")
        self.CloseButton.grid(row=0, column=20, padx=5, pady=5, sticky=W+S)

#############################  Functions for Food List Window  ##################################
    def Goodyview(self, *args):
        apply(self.GoodList.yview, args)
    def OutSoonyview(self, *args):
        apply(self.OutSoonList.yview, args)
    def Badyview(self, *args):
        apply(self.BadList.yview, args)

    def InsertFoodItem(self, arg, listNumber):
        if listNumber == 0:
            self.GoodList.insert(END, arg)
        elif listNumber == 1:
            self.OutSoonList.insert(END, arg)
        elif listNumber == 2:
            self.BadList.insert(END, arg)
        else:
            print str(listNumber)+" <-- Not found"
            
    def click_button(self, event):
        widgetSelected = event.widget
        if widgetSelected == self.CloseButton:
            print "you are here"
            listWindowIndex.destroy()

#############################  Other Functions  ##################################            

def InsertItems():
    FoodStructure = db.LoadFoodList()
    WhichList = 0
    for cols in FoodStructure:
        for FoodString in cols:
            ListIndex.InsertFoodItem(FoodString, WhichList)
        WhichList = WhichList + 1
            
def ListItem(PutMessageString):
    windowVariable.InsertListItem(PutMessageString) 
        
def CloseListWindow():
    ListWindow.quit()

def InitializeMainWindow(windowIndex):
    global windowVariable
##    windowIndex.geometry('368x355+50+50')
    windowVariable = ApplicationWindow(windowIndex)

def PrintAvailableFoods():
    length = len(foodInKitchen)
    for i in xrange(0,length):
        if len(foodInKitchen[i].itemName) < 30:
            StringTemp = '{:<30}'.format(foodInKitchen[i].itemName)
            String = StringTemp + " (" + foodInKitchen[i].itemQuantity + ")"
        else:
            String = foodInKitchen[i].itemName + "       (" + foodInKitchen[i].itemQuantity + ")"
            
        ListItem(String)

def CalculateSpoilTimes():
    print "You are now calculating the times."

    timeString = strftime('%X %x %Z')
    foundTimeNow = re.search("(.*?):(.*?):[0-9][0-9] (.*?)/(.*?)/(.*?) .*", timeString)    
    if foundTimeNow:
        hourNow = foundTimeNow.group(1)
        minuteNow = foundTimeNow.group(2)
        monthNow = foundTimeNow.group(3)
        dayNow = foundTimeNow.group(4)
        yearNow = int(foundTimeNow.group(5)) + 2000
           
        TimeNow = db.TimeClass(hourNow, minuteNow, monthNow, dayNow, yearNow)
        length = len(foodInKitchen)
        db.CheckIfItemsAreExpired(TimeNow, foodInKitchen)
        
def InsertListData(listIndex):
    print listIndex

index = Tk()
InitializeMainWindow(index)
foodInKitchen = db.ReadInDatabase()
PrintAvailableFoods()
index.after(10, CalculateSpoilTimes)
index.mainloop()

