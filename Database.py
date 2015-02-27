import os
import ConfigParser
import re

kitchenDatabaseFilename = "\\Kitchen Database\\KitchenDatabase.ini"

class TimeClass:    
    def __init__(self, currentHour, currentMinute, currentMonth, currentDay, currentYear):
        self.hour = currentHour
        self.minute = currentMinute
        self.month = currentMonth
        self.day = currentDay
        self.year = currentYear

class DatabaseContents:
    def __init__(self, VIN, data):
        self.itemVIN = VIN
        length = len(data)
        
        for i in range(0, length):
            if data[i][0] == "itemname":
                self.itemName = data[i][1]
            elif data[i][0] == "itemlifespanbefore":
                self.itemTimeBefore = data[i][1]
            elif data[i][0] == "itemlifespanafter":
                self.itemTimeAfter = data[i][1]
            elif data[i][0] == "itemtimeexpires":
                self.itemTimeExpires = data[3][1]
            else:
                print "The data not found: "+data[i][0]

def ReadInDatabase():
    currentDirectory = os.getcwd()
    kitchenDatabaseFilepath = currentDirectory + kitchenDatabaseFilename
    KitchenStructure = []
    kitchenDatabaseIndex = ConfigParser.ConfigParser()
    kitchenDatabaseIndex.read(kitchenDatabaseFilepath)

    kitchenSections = kitchenDatabaseIndex.sections()
    i = 0
    for section in kitchenSections:
        options = kitchenDatabaseIndex.items(section)
        KitchenStructure.append(DatabaseContents(section, options))
    
    return KitchenStructure

def CheckIfItemsAreExpired(Current, Item):
    FoodList = open("FoodList.ini", "w")
    FoodList.close()

    FoodIndex = ConfigParser.ConfigParser()
    
