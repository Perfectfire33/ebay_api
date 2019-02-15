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
>
>
>
"""

# To be referenced in:
#   gSheets_cmd.py
def gSheets_inventory_createOrReplaceInventoryItem(body, token, sku):

    # Get values given coordinates
    values = getSheetValues(SAMPLE_SPREADSHEET_ID, SAMPLE_RANGE_NAME)
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
