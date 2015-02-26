import os
import ConfigParser
import re

kitchenDatabaseFilename = "\\Kitchen Database\\KitchenDatabase.ini"

class DatabaseContents:
    def __init__(self, VIN, data):
        self.itemVIN = VIN
        self.itemName = data[0][1]
        self.itemTimeBefore = data[1][1]
        self.itemTimeAfter = data[2][1]

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
        
