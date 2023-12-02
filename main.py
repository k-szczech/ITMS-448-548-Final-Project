# Krystian Szczech, Na'im Muhammad, & Michael Yelich - Fall 2023
# Main file for GUI interface and data handling

from modules import geoip as geo
from modules import emailChecker as disposable
from modules import emailcheck as spam
from modules import file as file
import json
import PySimpleGUI as sg # GUI library

# Functions relating to data handling
# First position is data type (string), second position is a list of json strings
data=["",[]]
page = ""
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
                csvRow.append(str(jsonData[key]))
            else:
                csvRow.append("")
        output += ",".join(csvRow) + "\n"
    with open(fileName, "w") as outFile:
        outFile.write(output)
        outFile.close()

# Functions relating to GUI
    # Element layout
def makeWindow():
    layout = [[sg.Button("Spam Identifier"), sg.Button("Disposable"), sg.Button("File"), sg.Button("GeoIP")]]
    window = sg.Window('IP Address/Domain Name Lookup', layout)
    return window

window = makeWindow()
    # Event loop for window processing
while True:
    event, values = window.read()
    
    # Spam Identifier
    if event == "Spam Identifier":
        page="1"
        layout_spam = [[sg.Text("Spam Identifier")], [sg.Text("Enter an email content to check for spam: "), sg.InputText()], 
                       [sg.Button("submit email content"), sg.Button("New Request"), sg.Button("Cancel")]]
        window = sg.Window('Spam Identifier', layout_spam)

    # Disposable
    if event == "Disposable":
        layout = [  [sg.Text('Disposable'), sg.Text('Please Enter Email Address'), sg.InputText()],
                    [sg.Button("Submit Email Address"), sg.Button("New Request"), sg.Button("Cancel")]]
        window = sg.Window('Disposable', layout)
    
    # File
    if event == "File":
        layout = [  [sg.Text('File'), sg.Text(''), sg.InputText()], # ? File Path maybe
                    [sg.Button("Submit File"), sg.Button("New Request"), sg.Button("Cancel")]]
        window = sg.Window('File', layout)
    
    # Disposable
    if event == "GeoIP":
        layout = [  [sg.Text('Geo IP'), sg.Text('Please Enter IP adresss'), sg.InputText()],
                    [sg.Button("Submit IP address"), sg.Button("New Request"), sg.Button("Cancel")]]
        window = sg.Window('Geo IP', layout)
    
    
    if event == "New Request":
        window = makeWindow()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event =='submit email content':
        value1 = spam.detect_spam_email(values[0])
        layout = [  [sg.Text(value1)]]
        window = sg.Window('spam', layout)
    if event =='Submit Email Address':
        value2 = disposable.getResult(values[0])
        resetDataType(type(value2))
        addData(type(value2),value2)
        dumpCSV("emailOutput",getKeys())
    if event =='Submit File':
        value3 = file.upload_file(values[0])
        layout = [  [sg.Text(value3)]]
        window = sg.Window('File', layout)
    if event =='Submit IP address':
        value4 = geo.getResult(values[0])
        resetDataType(type(value4))
        addData(type(value4),value4)
        dumpCSV("ipOutput",getKeys())

        
        

        

window.close()
