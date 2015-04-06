from Tkinter import *
from ttk import *
import Database as db
import string
import os
from time import strftime
from PIL import Image, ImageTk

itemFilepath = "C:\\Projects\\Testing Location\\Smart Kitchen\\Product Image\\00000000.gif"
MainScreenBackGround = "C:\\Projects\\Testing Location\\Smart Kitchen\\Product Image\\MainScreenBackGround.png"
NewGroceriesBackGround = "C:\\Projects\\Testing Location\\Smart Kitchen\\Product Image\\GroceryShoppingBackGround.gif"

#############################  Main Application Window  ##################################
def InitializeMainWindowFeatures(root, mainSelf):
    
    mainSelf.lbl = Label(root, text="Foods")
    mainSelf.lbl.grid(row=0, column=0, sticky=W)
    mainSelf.area = Listbox(root, selectmode=SINGLE, height=17, width=18)
    mainSelf.area.grid(row=1, column=0, rowspan=10, columnspan=2, padx=5, sticky=W)
    
    mainSelf.itemName = Entry(root, width = 18)
    mainSelf.itemName.grid(row=1, column=3, padx=5, sticky = W)
    mainSelf.itemName_LABEL = Label(root, text = "Item Name")
    mainSelf.itemName_LABEL.grid(row=0, column=3, sticky=W)

    mainSelf.itemDatePurchased = Entry(root, width = 15)
    mainSelf.itemDatePurchased.grid(row=4, column=3, padx=5, sticky=W)
    mainSelf.itemDatePurchased_LABEL = Label(root, text = "Date Purchased")
    mainSelf.itemDatePurchased_LABEL.grid(row=3, column=3, sticky=W)

    mainSelf.itemSelfLifeTime = Entry(root, width = 15)
    mainSelf.itemSelfLifeTime.grid(row=4, column=4, padx=5, sticky=W)
    mainSelf.itemSelfLifeTime_LABEL = Label(root, text = "Expire Time")
    mainSelf.itemSelfLifeTime_LABEL.grid(row=3, column=4, sticky=W)

    mainSelf.itemQuantity = Entry(root, width = 5)
    mainSelf.itemQuantity.grid(row=1, column=4, padx=5, sticky=W)
    mainSelf.itemQuantity_LABEL = Label(root, text = "Qantity")
    mainSelf.itemQuantity_LABEL.grid(row=0, column=4, sticky=W)

    itemFilepath = "C:\\Projects\\Testing Location\\Smart Kitchen\\Product Image\\NoPictureAvailable.gif"
    photo = PhotoImage(file = itemFilepath)
    mainSelf.imageCanvas = Canvas(root, width=50, height=180)
    mainSelf.imageCanvas.grid(row=5, column=3, rowspan=5, columnspan=2, padx=5, pady=5, sticky=W+E+N+S)
    mainSelf.imageCanvas.create_image(0,0, image = photo)

    mainSelf.CloseButton = Button(root, text="Close", command = root.quit)
    mainSelf.CloseButton.grid(row=12, column=4, padx=5, pady = 5, sticky=E+S)
    
##        self.hbtn = Button(self.frame, text="Help", command = helpWindow)
##        self.hbtn.grid(row=5, column=0, padx=5)

    mainSelf.obtn = Button(root, text="Went Shopping!", command = MainWindow.InsertNewItems)
    mainSelf.obtn.grid(row=0, column=5, sticky=N+S)

    mainSelf.ListButton = Button(root, text="List", command = MainWindow.ShowList)
    mainSelf.ListButton.grid(row=12, column=0, padx=5, pady = 5, sticky=W+S)



class ApplicationWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
##        self.master.resizable(FALSE, FALSE)
        self.master.bind('<Button-1>', self.click_button)
        self.initUI()        
        
    def initUI(self):
        self.master.title("Smart Kitchen 1.00")
        self.grid(sticky = N+S+E+W)

    def GetSelfMaster(self):
        return self

#############################  Functions for Main Window  ##################################

    def InsertListItem(self, arg):
        self.area.insert(END, arg)

    def click_button(self, event):
        widgetSelected = event.widget
        if widgetSelected == self.area:
            self.itemName.delete(0, END)
            self.itemDatePurchased.delete(0, END)
            self.itemSelfLifeTime.delete(0, END)
            self.itemQuantity.delete(0, END)
            listSelection = self.area.curselection()
            self.itemName.insert(0, foodInKitchen[listSelection[0]].itemName)
            self.itemDatePurchased.insert(0, foodInKitchen[listSelection[0]].datePurchased)
            self.itemSelfLifeTime.insert(0, foodInKitchen[listSelection[0]].itemShelfLife)
            self.itemQuantity.insert(0, foodInKitchen[listSelection[0]].itemQuantity)

            itemFilepath = "C:\\Projects\\Testing Location\\Smart Kitchen\\Product Image\\"+foodInKitchen[listSelection[0]].itemVIN+".gif"
            if not os.path.isfile(itemFilepath):
                itemFilepath = "C:\\Projects\\Testing Location\\Smart Kitchen\\Product Image\\NoPictureAvailable.gif"
            self.photo = PhotoImage(file = itemFilepath)
            self.imageCanvas.create_image(100, 80, image = self.photo)
            
        elif widgetSelected == self.CloseButton:
            self.quit

    def ShowList(self):
        FoodStructure = [[] for i in range(3)]
        global ListIndex
        global listWindowIndex
        listWindowIndex = Tk()
        ListIndex = ListWindow(listWindowIndex)
        InsertItems()

    def InsertNewItems(self):
        global NewItemsIndex
        global NewItemsWindowIndex
        NewItemsWindowIndex = Tk()
        NewItemsIndex = NewItemsWindow(NewItemsWindowIndex)
        PopulateExpireTimesWindow()
        
        
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

#############################  Insert New Items  #################################
class NewItemsWindow():
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.master.bind('<Button-1>', self.click_button)
        self.initUI()

    def initUI(self):
        self.master.title("New Groceries!")
        self.style = Style()
        self.style.theme_use("default")
        self.frame.grid(row = 0, column = 0, sticky=N+E+S+W)

        self.itemName = Entry(self.frame, width = 18)
        self.itemName.grid(row=1, column=1, padx=5, sticky = W)
        self.itemName_LABEL = Label(self.frame, text = "Item Name")
        self.itemName_LABEL.grid(row=0, column=1, pady=2, padx=5, sticky=W)

        self.itemQuantity = Entry(self.frame, width = 15)
        self.itemQuantity.grid(row=1, column=3, padx=5, sticky=W)
        self.itemQuantity_LABEL = Label(self.frame, text = "Quantity")
        self.itemQuantity_LABEL.grid(row=0, column=3, pady=2, padx=5, sticky=W)

        self.ExpireTimeFrame = Frame(self.master)
        self.ExpireTimeFrame.grid(row=3, column=0, rowspan=10, columnspan=3, sticky=N+S+E+W)
        self.ExpireTimeFrame.grid_rowconfigure(0, weight=1)
        self.ExpireTimeFrame.grid_columnconfigure(0, weight=1)
        self.ExpireTimeLabel = Label(self.ExpireTimeFrame, text="Expire Time")
        self.ExpireTimeLabel.grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.ExpireTimeScrollbar = Scrollbar(self.ExpireTimeFrame, orient=VERTICAL)
        self.ExpireTimeList = Listbox(self.ExpireTimeFrame, selectmode=SINGLE, yscrollcommand=self.ExpireTimeScrollbar, height=10, width=20)
        self.ExpireTimeList.grid(row=1, column=0, rowspan=5, columnspan=5, padx=5, sticky=W+N)
        self.ExpireTimeScrollbar.config(command=self.ExpireTimeyview)
        self.ExpireTimeScrollbar.grid(row=1, column=1, rowspan=5, sticky=N+S) 
 
        self.CloseButton = Button(self.ExpireTimeFrame, text="Close")
        self.CloseButton.grid(row=6, column=7, padx=5, pady=5, sticky=W+S)

        self.InsertButton = Button(self.ExpireTimeFrame, text="Insert", )
        self.InsertButton.grid(row=6, column=0, padx=5, pady=5, sticky=E+S)
        self.InsertButton.grid_remove()
        
#############################  Functions for Insert New Items  ##################################
    def click_button(self, event):
        widgetSelected = event.widget
        if widgetSelected == self.CloseButton:
            NewItemsWindowIndex.destroy()
        if widgetSelected == self.InsertButton:
            print "You have inserted this item!"
            self.InsertEnteredNewGrocery()
        if widgetSelected == self.ExpireTimeList:
            self.InsertButton.grid()

    def InsertEnteredNewGrocery(self):
        err = 0
        itemNameString = self.itemName.get()
        itemQuantityString = self.itemQuantity.get()
        sel = self.ExpireTimeList.curselection()
        itemExpireTimeString = db.ExpireTimeStringList[sel[0]]
        if len(itemNameString) < 1 or len(itemQuantityString) < 1:
            print "Error!!"
        else:
            err = db.InsertNewGroceryItem(itemNameString, itemQuantityString, itemExpireTimeString)
            if err:
                if err == -1:
                    print "An error occured while inserting grocery"
            else:
                print "Item was inserted successfully"
            

    def ExpireTimeyview(self, *args):
        apply(self.ExpireTimeList.yview, args)

    def InsertExpireTimes(self, args):
        self.ExpireTimeList.insert(END, args)
        
#############################  Error Message Window  #################################
##class ErrorMessageWindow():
##    def __init__(self, master):
##        self.master = master
##        self.frame = Frame(self.master)
##        self.master.bind('<Button-1>', self.click_button)
##        self.initUI()
##
##    def initUI(self):
##        self.master.title("ERROR")
##        self.style = Style()
##        self.style.theme_use("default")
##        self.frame.grid(row = 0, column = 0, sticky=N+E+S+W)


#############################  Other Functions  ##################################
##def InsertItems():
##    FoodStructure = db.LoadFoodList()
##    WhichList = 0
##    for cols in FoodStructure:
##        for FoodString in cols:
##            ListIndex.InsertFoodItem(FoodString, WhichList)
##        WhichList = WhichList + 1
##
##def PopulateExpireTimesWindow():
##    for dayString in db.ExpireTimeStringList:
##        NewItemsIndex.InsertExpireTimes(dayString)
##            
##def ListItem(PutMessageString):
##    windowVariable.InsertListItem(PutMessageString) 
##        
##def CloseListWindow():
##    ListWindow.quit()
##
##def InitializeMainWindow(windowIndex):
##    global windowVariable
####    windowIndex.geometry('368x355+50+50')
##    windowVariable = ApplicationWindow(windowIndex)
##
def PrintAvailableFoods(root, mainSelf):
    length = len(foodInKitchen)
    for i in xrange(0,length):
        String = foodInKitchen[i].itemName
        mainSelf.area.insert(END, String)

##def CalculateSpoilTimes():
##    print "You are now calculating the times."
##
##    timeString = strftime('%X %x %Z')
##    foundTimeNow = re.search("(.*?):(.*?):[0-9][0-9] (.*?)/(.*?)/(.*?) .*", timeString)    
##    if foundTimeNow:
##        hourNow = foundTimeNow.group(1)
##        minuteNow = foundTimeNow.group(2)
##        monthNow = foundTimeNow.group(3)
##        dayNow = foundTimeNow.group(4)
##        yearNow = int(foundTimeNow.group(5)) + 2000
##           
##        TimeNow = db.TimeClass(hourNow, minuteNow, monthNow, dayNow, yearNow)
##        length = len(foodInKitchen)
##        db.CheckIfItemsAreExpired(TimeNow, foodInKitchen)
##        
##def InsertListData(listIndex):
##    print listIndex


root = Tk()
root.geometry("500x350+300+300")
global MainWindow
MainWindow = ApplicationWindow(root)

im = Image.open(MainScreenBackGround)
tkimage = ImageTk.PhotoImage(im)
myvar=Label(root, image = tkimage)
myvar.place(x=0, y=0, relwidth=1, relheight=1)
mainSelf = MainWindow.GetSelfMaster()
print mainSelf
InitializeMainWindowFeatures(root, mainSelf)

foodInKitchen = db.ReadInDatabase()
PrintAvailableFoods(root, mainSelf)
##index.after(10, CalculateSpoilTimes)
root.mainloop()

