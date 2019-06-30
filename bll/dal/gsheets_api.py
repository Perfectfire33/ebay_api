from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import os
import sys

"""
GSHEETS_API.PY ~ CALL GOOGLE SHEETS API 
WITH GOOGLE CLIENT LIBRARY
AND RETRIEVE RESPONSE
"""

"""
This file:
>retrieves Google Sheets credentials in format of credentials.json
>authenticates with Google Sheets API
>contains functions for specific sheet operations
"""

# Add functions to interface with Google Sheets API

# These variables must be set in a function that calls getSheet()
# If modifying these scopes, delete the file token.json.
# scopes = 'https://www.googleapis.com/auth/spreadsheets.readonly'
# tokenPath = 'token.json'

# These variables must be set in a function that calls getSheetValues()
# The ID and range of a sample spreadsheet.
# SAMPLE_SPREADSHEET_ID = '1Xqm9Mhe9-ADbDqo6l4oEPM1pygGof0YcUrHcpZM01vo'
# SAMPLE_RANGE_NAME = 'Class Data!A2:E'


# SHEET_GID = '1040224557'


# getSheet()
#   This function requires a scopes URL (see Google Sheet API docs)
#       and tokenPath (location of token.json)
#   This function returns the authenticated sheet object
# Currently referenced in:
#   gsheets_api_connector.py/gSheets_inventory_createOrReplaceInventoryItem
def getSheet(scopes, tokenPath):
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    store = file.Storage(tokenPath)
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', scopes)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))
    # Call the Sheets API
    sheet = service.spreadsheets()
    return sheet


# getSheetValues()
#   This function requires a spreadsheet id and a sheet range
#   The sheet range is made up of a named sheet and cell coordinates (e.g. <sheet_name>!<column><row>:<column><row>)
def getSheetValues(scopes, tokenPath, spreadsheet_id, sheet_range):
    sheet = getSheet(scopes, tokenPath)
    result = sheet.values().get(spreadsheetId=spreadsheet_id,
                                range=sheet_range).execute()
    values = result.get('values', [])
    if not values:
        print('No data found.')
    else:
        return values


# updateSheetValues()
# These variables must be set in a function that calls updateSheetValues():
#   valInputOpt = "USER_ENTERED"
#   bodyData = []
def updateSheetValues(scopes, tokenPath, spreadsheet_id, sheet_range, valInputOpt, bodyData):
    sheet = getSheet(scopes, tokenPath)
    result = sheet.values().update(spreadsheetId=spreadsheet_id,
                                   range=sheet_range,
                                   valueInputOption=valInputOpt,
                                   body=bodyData).execute()
    values = result.get('values', [])
    if not values:
        print('No data found.')
    else:
        return values
