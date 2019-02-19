from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import gsheets_api_connector
import ebay_api_connector
import gsheets_api
import os
import sys
# import master_cmd.setdata
# Reading a File Line By Line (see for removing \n, removing whitespaces):
# https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list

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
# Get Config Data
configData = gsheets_api_connector.readConfigFile()
# print(configData)

# Set current Config Data Params
p1=configData[0]
p2=configData[1]
p3=configData[2]
p4=configData[3]
p5=configData[4]
p6=configData[5]
p7=configData[6]

# Acquire List of Acceptable Fields (Areas in Google Sheets to grab data from)
listOfAcceptableFields = gsheets_api_connector.getAcceptableFields(p3, p4, p5, p6, p7)

# Acquire Set of Google Sheet Data
dataSet = gsheets_api_connector.getDataSet(p1, p2, listOfAcceptableFields)
# print(dataSet)

"""
//////////// Process data from selected areas accordingly /////////////
//////////// Send to destination  ////////////////////////////////////////
"""

# Need to format dataSet so it may fit into eBay's objects
# Then send to eBay API in proper eBay format

# eBay Object Design Notes
"""
inventory_item - add sku to inventory (any other fields?)


 
policy - shipping
policy - payment
policy - return


"""














