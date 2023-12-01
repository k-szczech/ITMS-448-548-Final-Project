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
    data[1].append(jsonData)
