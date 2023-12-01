from modules import geoip
import json


# Functions relating to data handling
# First position is data type (string), second position is a list of json strings
data=["",[]]

def resetDataType(newType):
    data[0]=newType
    data[1]=[]

def getDataType():
    return data[0]

def getKeys():
    keyList = []
    for entry in data[1]:
        entry_keys = list(json.loads(entry).keys())
        for key in entry_keys:
            if(not(key in keyList)):
                keyList.append(key)
    return keyList

def addData(dataType, jsonData):
    if(dataType != getDataType()):
        raise TypeError("Data type mismatch")
    #removing problematic characters
    processedData = jsonData.replace("\n","")
    data[1].append(processedData)

def dumpCSV(fileName, keyList):
    output = ""
    output += ",".join(keyList)
    output += "\n"
    for row in data[1]:
        csvRow = []
        jsonData = json.loads(row)
        for key in keyList:
            if key in jsonData:
                csvRow.append(jsonData[key])
            else:
                csvRow.append("")
        output += ",".join(csvRow) + "\n"
    with open(fileName, "w") as outFile:
        outFile.write(output)
        outFile.close()