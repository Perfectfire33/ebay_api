from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import gsheets_api_connector
import ebay_api_connector
import gsheets_api
import os
import sys

"""
This file:
>Calls Google Sheet APIs using Google Client Library in gsheets_api.py
>Contains functions that are used when executing gSheets_cmd.py

Variables Google Sheet APIs need:
    For getSheet():
        These variables must be set in a function that calls getSheet():
        If modifying these scopes, delete the file token.json.
        >   scopes = 'https://www.googleapis.com/auth/spreadsheets.readonly'
        >   tokenPath = 'token.json'

    For getSheetValues():
        These variables must be set in a function that calls getSheetValues()
        The ID and range of a sample spreadsheet.
        >   spreadsheet_id = '1Xqm9Mhe9-ADbDqo6l4oEPM1pygGof0YcUrHcpZM01vo'
        >   sheet_range = 'Class Data!A2:E'

    For updateSheetValues():
        These variables must be set in a function that calls updateSheetValues():
        >   spreadsheet_id = '1Xqm9Mhe9-ADbDqo6l4oEPM1pygGof0YcUrHcpZM01vo'
        >   sheet_range = 'mySheet!A2:E'
        >   valInputOpt = "USER_ENTERED"
        >   bodyData = []

"""

print("\n")
print("---------------------------- Start Script ---------------------------------")
print("-------------- Get Sheet Area Info  --------------------------")
print("\n")

"""
/////////////////////////// Environment Set Up /////////////////////////////////
"""

# Get accessible Google Sheet Areas
acceptableFieldsList = gsheets_api_connector.getAcceptableFields()

# These variables must be set in a function that calls getSheet()
# If modifying these scopes, delete the file token.json.
scopes = 'https://www.googleapis.com/auth/spreadsheets.readonly'
tokenPath = 'token.json'

# Get Sheet
sheet = gsheets_api.getSheet(scopes, tokenPath)


"""
//////////// Collect Acceptable Field Areas and put into usable array /////////////
"""

coordList = []
#   For each XY coordinate set in the (currently only) acceptable field profile (Profile1)
#   Save to an array (format is e.g. coordList = ["A1,B12","E1,G12","I1,K12"] )
listCount = acceptableFieldsList[0]['sheet_cell_xy_sets'].__len__()

print("begin.listCount")
print(listCount)
print("end.listCount")

counter = 0
counter2 = 1
while counter < listCount:
    coordList.append(acceptableFieldsList[0]["sheet_cell_xy_sets"][counter2 - 1])
    counter = counter + 1
    counter2 = counter2 + 1

print("begin.coordList")
print(coordList)
print("end.coordList")

#for listCount in acceptableFieldsList[0]['sheet_cell_xy_sets']:
    #print("begin.listCount")
    #print(listCount)
    #print("end.listCount")
    #coordinates = acceptableFieldsList[0]['sheet_cell_xy_sets'][listCount]
    #coordList.append(coordinates)

# A sheet's cell's selection
#   e.g. [start, end]
#   e.g. currentCoordSet = ["A1","B12"]
currentCoordSet = []
# List of all the selected areas (separated appropriated)
#   e.g. [Area1[start,end], Area2[start,end]]
#   e.g. currentCoordSetList = [["A1","B12"],["E1,G12"],["I1,K12"]]
currentCoordSetList = []
# Go through coordinates list and make into acceptable format for Google Sheets API
for item in coordList:
    #print("begin.item")
    #print(coordList.index(item))
    #print("end.item")
    currentCoord = coordList[coordList.index(item)]
    currentCoordSet = currentCoord.split(",")
    currentCoordSetList.append(currentCoordSet)



"""
//////////// Get Values from all accessible Google Sheet areas /////////////
//////////// and store into object  ////////////////////////////////////////
"""
# All data from all selected areas
dataSet = []

# Cycle Through each accessible area of Google Sheets and add into dataSet array
for area in currentCoordSetList:
    sheet_range = acceptableFieldsList[0]['sheet_name'] \
                  + "!" + currentCoordSetList[currentCoordSetList.index(area)][0] \
                  + ":" + currentCoordSetList[currentCoordSetList.index(area)][1]
    dataSet.append(gsheets_api.getSheetValues(acceptableFieldsList[0]['spreadsheet_id'], sheet_range))



"""
//////////// Process data from selected areas accordingly /////////////
//////////// Send to destination  ////////////////////////////////////////
"""

print("dataSet")
print(dataSet)

