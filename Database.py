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
            elif data[i][0] == "datepurchased":
                self.datePurchased = data[i][1]
            elif data[i][0] == "itemshelflife":
                self.itemShelfLife = data[i][1]
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

def CheckIfItemsAreExpired(Current, foodStructure):
    timeStamp = Current.hour+":"+Current.minute+" "+Current.month+"."+Current.day+"."+str(Current.year)

    FoodListIndex = ConfigParser.ConfigParser()
    FoodListIndex.add_section("TimeStamp")
    FoodListIndex.set("TimeStamp", "TimeAdded", timeStamp)

    length = len(foodStructure)
    for i in range(0, length):
        timeTilExpiresString = foodStructure[i].itemShelfLife
        if "day" in timeTilExpiresString or "d" in timeTilExpiresString:
            print "Found days"
            found = re.findall('\d+', timeTilExpiresString)
            number = int(found[0])*24
        elif "hour" in timeTilExpiresString or "hr" in timeTilExpiresString or "h" in timeTilExpiresString:
            print "Found hours"
            found = re.findall('\d+', timeTilExpiresString)
            number = int(found[0])
        elif "year" in timeTilExpiresString or "yr" in timeTilExpiresString or "y" in timeTilExpiresString:
            print "Found years"
            found = re.findall('\d+', timeTilExpiresString)
            number = int(found[0])*24*365
        else:
            number = 0
        print "The number is: "+str(number)

        

    FoodList = open("FoodList.ini", "w+")
    FoodListIndex.write(FoodList)
    FoodList.close()
    
