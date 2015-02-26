from Tkinter import *
from ttk import *
import ApplicationWindow as app
import Database as db

def AccessDatabase():
    length = len(foodInKitchen)
    for i in xrange(0,length):
        app.ListItem(foodInKitchen[i].itemName)
        
def InsertListData(listIndex):
    print listIndex

index = Tk()
app.InitializeMainWindow(index)
foodInKitchen = db.ReadInDatabase()
index.after(1000, AccessDatabase)
index.mainloop()
