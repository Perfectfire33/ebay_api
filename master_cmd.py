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


scopes = 'https://www.googleapis.com/auth/spreadsheets.readonly'
tokenPath = 'token.json'

acceptableFields_profileName = "Profile1"
spreadsheet_name = "eBay_API_Dashboard"
spreadsheet_id = "1Xqm9Mhe9-ADbDqo6l4oEPM1pygGof0YcUrHcpZM01vo"
sheet_name = "stage3"
sheet_cell_xy_sets = []
# Create list of xy sets (e.g. read in from file list of coordinates to select):
sheet_cell_xy_sets.append("A8,B16")
sheet_cell_xy_sets.append("D8,G16")
sheet_cell_xy_sets.append("I8,P16")

# Set current Acceptable Fields
p1=acceptableFields_profileName
p2=spreadsheet_name
p3=spreadsheet_id
p4=sheet_name
p5=sheet_cell_xy_sets

# Acquire List of Acceptable Fields (Areas in Google Sheets to grab data from)
listOfAcceptableFields = gsheets_api_connector.getAcceptableFields(p1,p2,p3,p4,p5)


dataSet = gsheets_api_connector.getDataSet(scopes, tokenPath, listOfAcceptableFields)

print(dataSet)









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














