from Tkinter import *
from ttk import *
import ApplicationWindow as app
import Database as db

def AccessDatabase():
    length = len(foodInKitchen)
    for i in xrange(0,length):
        app.ListItem(foodInKitchen[i].itemName)
        print foodInKitchen[i].itemVIN
        print "\t" + foodInKitchen[i].itemName
        print "\t" + foodInKitchen[i].itemTimeBefore
        print "\t" + foodInKitchen[i].itemTimeAfter
        
index = Tk()
app.InitializeMainWindow(index)
print "You are now here!"
foodInKitchen = db.ReadInDatabase()
print foodInKitchen[0].itemName
index.after(1000, AccessDatabase)
index.mainloop()
