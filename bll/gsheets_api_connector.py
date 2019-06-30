from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import bll.dal.gsheets_api
import os
import sys

"""
GSHEETS_API_CONNECTOR.PY ~ CONNECT GOOGLE SHEETS API 
TO OUR APP
"""

"""
This file:
>Calls Google Sheet APIs using Google Client Library in gsheets_api.py
>Contains functions that are used when executing gSheets_cmd.py
>To be referenced in gSheets_cmd.py and master_cmd.py

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
def readConfigFile():
    configArray = []
    xyCoordArray = []
    configFileName = "master_cmd.setdata"
    lines = tuple(open(configFileName, 'r'))
    for line in lines:
        lineA = line.split('\n')
        if lines.index(line) >= 9:
            configArray.append(lineA)

        if lines.index(line) >= 15:
            xyCoordArray.append(lineA)

    # print("###### BEGIN read master_cmd.setdata ##############")
    # print("---- settings lines in file ----")
    # print("scopes =" + configArray[0][0])
    # print("tokenPath =" + configArray[1][0])
    # print("acceptableFields_profileName =" + configArray[2][0])
    # print("spreadsheet_name =" + configArray[3][0])
    # print("spreadsheet_id =" + configArray[4][0])
    # print("sheet_name =" + configArray[5][0])
    # print("---- settings lines in file ----")
    # print("---- xy coord lines in file ----")
    # print("xyCoordArray = {")
    # for coordX in xyCoordArray:
    #     print(xyCoordArray[xyCoordArray.index(coordX)][0])
    # print("}")
    # print("---- xy coord lines in file ----")
    # print("###### END read master_cmd.setdata ##############")

    scopes = configArray[0][0]
    tokenPath = configArray[1][0]
    acceptableFields_profileName = configArray[2][0]
    spreadsheet_name = configArray[3][0]
    spreadsheet_id = configArray[4][0]
    sheet_name = configArray[5][0]
    sheet_cell_xy_sets = []
    # Create list of xy sets (e.g. read in from file list of coordinates to select):
    for itemX in xyCoordArray:
        sheet_cell_xy_sets.append(xyCoordArray[xyCoordArray.index(itemX)][0])

    # configDataSet = []

    # for profile in configProfileCount:
    configData = []
    configData.append(scopes)
    configData.append(tokenPath)
    configData.append(acceptableFields_profileName)
    configData.append(spreadsheet_name)
    configData.append(spreadsheet_id)
    configData.append(sheet_name)
    configData.append(sheet_cell_xy_sets)
    # configDataSet.append(configData)

    # print(configData)
    """
    configData[0] = scopes
    configData[1] = tokenPath
    configData[2] = acceptableFields_profileName
    configData[3] = spreadsheet_name
    configData[4] = spreadsheet_id
    configData[5] = sheet_name
    configData[6] = sheet_cell_xy_sets
    """
    return configData


# This function allows for loading a 'profile' of what Google Sheet(s)
#   and cells within those sheets are accessible
# Collect info about what fields need to be accessed based on a defined structure
def getAcceptableFields(p1, p2, p3, p4, p5):

    acceptableFields_profileName = p1
    spreadsheet_name = p2
    spreadsheet_id = p3
    sheet_name = p4
    sheet_cell_xy_sets = p5

    # Read in local file, hard-code, or accept user input within executable script

    # Must create for loop to add multiple 'acceptableFields' to the list of acceptable fields
    # For now, only one is necessary
    acceptableFields = {}
    acceptableFields['acceptableFields_profileName'] = acceptableFields_profileName
    acceptableFields['spreadsheet_name'] = spreadsheet_name
    acceptableFields['spreadsheet_id'] = spreadsheet_id
    acceptableFields['sheet_name'] = sheet_name
    acceptableFields['sheet_cell_xy_sets'] = sheet_cell_xy_sets
    # acceptableFields.append(acceptableFields_profileName)
    # acceptableFields.append(spreadsheet_name)
    # acceptableFields.append(spreadsheet_id)
    # acceptableFields.append(sheet_name)
    # acceptableFields.append(sheet_cell_xy_sets)

    listOfAcceptableFields = []
    listOfAcceptableFields.append(acceptableFields)
    # print(listOfAcceptableFields)

    # This is accessed as e.g. listOfAcceptableFields[0].sheet_cell_xy_sets[0]
    return listOfAcceptableFields


# getDataSet retrieves the data from the selected Google Sheet area(s)
def getDataSet(scopes, tokenPath, listOfAcceptableFields):
    # These variables must be set in a function that calls getSheet()
    # If modifying these scopes, delete the file token.json.
    # scopes = 'https://www.googleapis.com/auth/spreadsheets.readonly'
    # tokenPath = 'token.json'

    # Get Sheet
    # sheet = gsheets_api.getSheet(scopes, tokenPath)

    """
    //////////// Collect Acceptable Field Areas and put into usable array /////////////
    """
    coordList = []
    #   For each XY coordinate set in the (currently only) acceptable field profile (Profile1)
    #   Save to an array (format is e.g. coordList = ["A1,B12","E1,G12","I1,K12"] )
    listCount = listOfAcceptableFields[0]['sheet_cell_xy_sets'].__len__()

    # print("begin.listCount")
    # print(listCount)
    # print("end.listCount")

    counter = 0
    counter2 = 1
    while counter < listCount:
        coordList.append(listOfAcceptableFields[0]["sheet_cell_xy_sets"][counter2 - 1])
        counter = counter + 1
        counter2 = counter2 + 1

    # print("begin.coordList")
    # print(coordList)
    # print("end.coordList")

    # for listCount in listOfAcceptableFields[0]['sheet_cell_xy_sets']:
    # print("begin.listCount")
    # print(listCount)
    # print("end.listCount")
    # coordinates = listOfAcceptableFields[0]['sheet_cell_xy_sets'][listCount]
    # coordList.append(coordinates)

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
        # print("begin.item")
        # print(coordList.index(item))
        # print("end.item")
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
        sheet_range = listOfAcceptableFields[0]['sheet_name'] \
                      + "!" + currentCoordSetList[currentCoordSetList.index(area)][0] \
                      + ":" + currentCoordSetList[currentCoordSetList.index(area)][1]
        dataSet.append(bll.dal.gsheets_api.getSheetValues(scopes, tokenPath, listOfAcceptableFields[0]['spreadsheet_id'], sheet_range))

    # Format of dataSet:
    """
    [
      todo: add profile1 here in hierarchy once finish adding support for multi profile in this file
        area1[
            row1[ column1, column2 ], 
            row2[ column1, column2 ]
        ], 
        area2[
            row1[ column1, column2 ],
            row2[ column1, column2 ]
        ]
    ]
    print("dataSet")
    print(dataSet)
    """
    return dataSet

