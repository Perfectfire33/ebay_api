from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import ebay_api

"""
GSHEETS_API_CONNECTOR.PY ~ CONNECT GOOGLE SHEETS API 
TO OUR APP
"""

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

# This function allows for loading a 'profile' of what Google Sheet(s)
#   and cells within those sheets are accessible
# Collect info about what fields need to be accessed based on a defined structure
def getAcceptableFields():

    acceptableFields_profileName = "Profile1"
    spreadsheet_name = "eBay_API_Dashboard"
    spreadsheet_id = "1Xqm9Mhe9-ADbDqo6l4oEPM1pygGof0YcUrHcpZM01vo"
    sheet_name = "stage3"
    sheet_cell_xy_sets = []
    # Create list of xy sets (e.g. read in from file list of coordinates to select):
    sheet_cell_xy_sets.append("A8,B16")
    sheet_cell_xy_sets.append("D8,G16")
    sheet_cell_xy_sets.append("I8,P16")

    # Read in local file, hard-code, or accept user input within executable script
    acceptableFields = {}
    acceptableFields.append(acceptableFields_profileName)
    acceptableFields.append(spreadsheet_name)
    acceptableFields.append(spreadsheet_id)
    acceptableFields.append(sheet_name)
    acceptableFields.append(sheet_cell_xy_sets)

    return acceptableFields


# Pulls inventory data from Google Sheets
# Requires a range of fields
def gSheets_inventory_retrieveInventoryData():




# To be referenced in:
#   gSheets_cmd.py
def gSheets_inventory_createOrReplaceInventoryItem(body, token, sku):

    # Get values given coordinates
    values = getSheetValues(spreadsheet_id, sheet_range)
    # Scroll through the array
    for row in values:
        # Print columns A and E, which correspond to indices 0 and 4.
        print('%s, %s' % (row[0], row[4]))


    # This is the ebay URL used to add or update an inventory item                      *****IMPORTANT*****
    api_url = 'https://api.sandbox.ebay.com/sell/inventory/v1/inventory_item/' + str(sku) + '/' # <--- Use this test env url first then Prod
                                                            # Prod env url: https://api.ebay.com


    # Method body
    api_payload = body

    # Method Headers
    api_headers = {'Authorization': '%s' % token,
                            'content-type': 'application/json',
                            'Accept': 'application/json',
                            'content-language': 'en-US'}

    # Specify request body json data and headers
    api_response = ebay_api.createOrReplaceInventoryItem(api_url, api_payload, api_headers)


    """Store the addTestCase response"""

    # Use the .json function() to get the data in json format and then we store it in api_response variable
    # api_response = api_response.json()
    return api_response



def Xinventory_createOrReplaceInventoryItem(body, token, sku):

    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    sheet = service.spreadsheets()

    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    aa = sheet.values().get()

    if not values:
        print('No data found.')
    else:
        print('Name, Major:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s, %s' % (row[0], row[4]))


    # This is the ebay URL used to add or update an inventory item                      *****IMPORTANT*****
    api_url = 'https://api.sandbox.ebay.com/sell/inventory/v1/inventory_item/' + str(sku) + '/' # <--- Use this test env url first then Prod
                                                            # Prod env url: https://api.ebay.com


    # Method body
    api_payload = body

    # Method Headers
    api_headers = {'Authorization': '%s' % token,
                            'content-type': 'application/json',
                            'Accept': 'application/json',
                            'content-language': 'en-US'}

    # Specify request body json data and headers
    api_response = ebay_api.createOrReplaceInventoryItem(api_url, api_payload, api_headers)


    """Store the addTestCase response"""

    # Use the .json function() to get the data in json format and then we store it in api_response variable
    # api_response = api_response.json()
    return api_response
