from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
print("\n")
print("---------------------------- Start Script ---------------------------------")
print("-------------- Get Sheet Info  --------------------------")
print("\n")

# If modifying these scopes, delete the file token.json.
# SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '1Xqm9Mhe9-ADbDqo6l4oEPM1pygGof0YcUrHcpZM01vo'
SHEET_RANGE = 'incoming_data!A1:D5'

#filepath_body = r'C:\Users\dick\PycharmProjects\ebay_api\gSheet_update_body.json'
#PAYLOAD = open(filepath_body).read()

#print("PAYLOAD")
#print(PAYLOAD)

#
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
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=SHEET_RANGE).execute()
values = result.get('values', [])

print("values")
print(values)


BFRange = 'incoming_data!A1:D5'

myBF="ZZZ"
BFData = {}

arrayData = []
arrayData.append("AAA")
arrayData.append("BBB")
arrayData.append("CCC")
arrayData.append("DDD")

#BFData['values']= [[myBF],[myBF],[myBF],[myBF],[myBF]]
BFData['values']= [arrayData,arrayData,arrayData,arrayData,arrayData]
BFData['majorDimension']="ROWS"
BFData['range']= BFRange


print("BFData")
print(BFData)


result2 = sheet.values().update(spreadsheetId=SPREADSHEET_ID, range=SHEET_RANGE, valueInputOption="USER_ENTERED", body=BFData).execute()
print("result2")
print(result2)


values2 = result2.get('updatedRange')
print("values2")
print(values2)




#filepath_token = r'\Users\dick\PycharmProjects\ebay_api\token.json'

#token = open(filepath_token).read()
#tokenPrepared = "Bearer " + token

#body = open(filepath_body).read()
#sku = "testItem1"

#api_response = gsheets_api_connector.getSheetData(body, tokenPrepared, sku)

#code = api_response.status_code
#print("code")
#print(code)

#print("api_response")
#print(api_response)


print("---------------------------- End Script ---------------------------------")