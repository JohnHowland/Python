import os
import ConfigParser
import re
import time

kitchenDatabaseFilename = "\\Kitchen Database\\KitchenDatabase.ini"

ExpireTimeStringList = []
ExpireTimeStringList = ['1 day','2 days','3 days',
                        '4 days','5 days','6 days',
                        '7 days','8 days','9 days',
                        '10 days','11 days','12 days',
                        '13 days','14 days','15 days',
                        '16 days','17 days','18 days',
                        '19 days','20 days','21 days',
                        '22 days','23 days','24 days',
                        '25 days','26 days','27 days',
                        '28 days','29 days','30 days']

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
            elif data[i][0] == "quantity":
                self.itemQuantity = data[i][1]
            else:
                print "The data not found: "+data[i][0]

def ReadInDatabase():
    currentDirectory = os.getcwd()
    kitchenDatabaseFilepath = currentDirectory + kitchenDatabaseFilename
    KitchenStructure = []
    kitchenDatabaseIndex = ConfigParser.ConfigParser()
    kitchenDatabaseIndex.read(kitchenDatabaseFilepath)

    kitchenSections = kitchenDatabaseIndex.sections()
    for section in kitchenSections:
        options = kitchenDatabaseIndex.items(section)
        KitchenStructure.append(DatabaseContents(section, options))
    
    return KitchenStructure

def CheckIfItemsAreExpired(Current, foodStructure):
    goodCounter = 0
    badCounter = 0
    outSoonCounter = 0
    errorCounter = 0
    
    timeStamp = Current.hour+":"+Current.minute+" "+Current.month+"."+Current.day+"."+str(Current.year)

    FoodListIndex = ConfigParser.ConfigParser()
    FoodListIndex.add_section("TimeStamp")
    FoodListIndex.add_section("Good Food")
    FoodListIndex.add_section("Out Soon Food")
    FoodListIndex.add_section("Spoiled Food")
    FoodListIndex.add_section("Error")
    FoodListIndex.set("TimeStamp", "TimeAdded", timeStamp)

##    FoodListIndex.add_section("Good Food")
##    for i in range(0, 10):
##        string1 = "GoodFood"+str(i)
##        FoodListIndex.set("Good Food", string1, string1)
##        
##    FoodListIndex.add_section("Out Soon Food")
##    for i in range(0, 10):
##        string2 = "OutSoonFood"+str(i)
##        FoodListIndex.set("Out Soon Food", string2, string2)
##        
##    FoodListIndex.add_section("Spoiled Food")
##    for i in range(0, 10):
##        string3 = "SpoiledFood"+str(i)
##        FoodListIndex.set("Spoiled Food", string3, string3)

    length = len(foodStructure)
    for i in range(0, length):
        timeTilExpiresString = foodStructure[i].itemShelfLife
        if "day" in timeTilExpiresString or "d" in timeTilExpiresString:
            found = re.findall('\d+', timeTilExpiresString)
            number = int(found[0])*24
        elif "hour" in timeTilExpiresString or "hr" in timeTilExpiresString or "h" in timeTilExpiresString:
            found = re.findall('\d+', timeTilExpiresString)
            number = int(found[0])
        elif "year" in timeTilExpiresString or "yr" in timeTilExpiresString or "y" in timeTilExpiresString:
            found = re.findall('\d+', timeTilExpiresString)
            number = int(found[0])*24*365
        else:
            number = 0

        foodDecision = Result(Current, foodStructure[i].datePurchased, number)

        if foodDecision == 1:
            print "You are in number 1"
            goodStringIndex = "GoodString" + str(goodCounter)
            FoodListIndex.set("Good Food", goodStringIndex, foodStructure[i].itemName)
            goodCounter = goodCounter + 1
        elif foodDecision == 2:
            outSoonStringIndex = "OutSoonString" + str(outSoonCounter)
            FoodListIndex.set("Out Soon Food", outSoonStringIndex, foodStructure[i].itemName)
            outSoonCounter = outSoonCounter + 1 
        elif foodDecision == 3:
            badStringIndex = "BadString" + str(badCounter)
            FoodListIndex.set("Spoiled Food", badStringIndex, foodStructure[i].itemName)
            badCounter = badCounter + 1
        else:
            print "There was an error"
            errorStringIndex = "ErrorString" + str(errorCounter)
            FoodListIndex.set("Error", errorStringIndex, foodStructure[i].itemName)
            errorCounter = errorCounter + 1
            
            

    FoodList = open("Kitchen Database\\FoodList.ini", "w+")
    FoodListIndex.write(FoodList)
    FoodList.close()
    time.sleep(2)

def Result(Time, purchaseDate, timeTilExpires):
    foodDecision = 1
##    ThirtyOneDays = [01, 03, 05, 07, 08, 10, 12]
    exception = 0
    print "You made it inside the results function"
    
    print purchaseDate
##    foundTimeNow = re.search("(.*?):(.*?) (.*?)\.(.*?)\.(.*?)$", purchaseDate)    
##    if foundTimeNow:
##        hour = int(foundTimeNow.group(1))
##        minute = int(foundTimeNow.group(2))
##        month = int(foundTimeNow.group(3))
##        day = int(foundTimeNow.group(4))
##        year = int(foundTimeNow.group(5))
##
####        print "hour "+str(hour)
####        print "minute "+str(minute)
####        print "month "+str(month)
####        print "day "+str(day)
####        print "year "+str(year)
##
##        if Time.yearNow > year:
##            elapsedYears = Time.yearNow - year
##            if elapsedYears > 1:
##                if Time.monthNow < month:
##                    elapsedMonths = (Time.monthNow + 12) - month
##                else:
##                    elapsedMonths = (Time.monthNow) - month
##                    elapsedMonths = elapsedMonths + (elapsedYears * 12)
##                
##        
##
##
##        elapsedHours = Time.hourNow - hour
##        elapsedMinutes = Time.minuteNow - minute
##        elapsedMonths = Time.monthNow - month
##        elapsedDays = (Time.dayNow + exception) - day
##        elapsedYears = Time.yearNow - year
        

    
    





    return foodDecision 


def LoadFoodList():
    currentDirectory = os.getcwd()
    FoodFilepath = currentDirectory+"\\Kitchen Database\\FoodList.ini"
    FoodListIndex = ConfigParser.ConfigParser()
    FoodListIndex.read(FoodFilepath)
    
    FoodListStructure = [[] for i in range(3)]
    FoodSections = FoodListIndex.sections()
    
    for section in FoodSections:
        if section != "TimeStamp" and section != "Error":
            print "You made after the section check"
            options = FoodListIndex.items(section)
            if section == "Good Food":
                listNumber = 0
            elif section == "Out Soon Food":
                listNumber = 1
            elif section == "Spoiled Food":
                listNumber = 2
            else:
                print "Error!!"

            for option in options:
##                print option[1]
                FoodListStructure[listNumber].append(option[1])
##                print FoodListStructure[listNumber]
    return FoodListStructure

def InsertNewGroceryItem(name, quantity, expireTime):
    err = 0
    print "You made it into insert function in database file!"

    return err
                
            
