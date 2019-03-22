import gsheets_api_connector

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

# need to define headers
headers = []
headers.append('item_id')
headers.append('item_title')
headers.append('item_category')
headers.append('item_condition')
headers.append('item_condition_description')
headers.append('item_price')
headers.append('item_qty')
headers.append('packed_item_weight_lb')
headers.append('packed_item_weight_oz')
headers.append('packed_item_height')
headers.append('packed_item_length')
headers.append('packed_item_depth')

# ebay incoming object row
inventory_row = {}

# need to define column groups


# set to first group of columns
column_group = 0

# get number of rows to get this header
rows = len(dataSet[column_group])

# select first column
column = 0

# get number of columns in this group of columns
# columns = len(dataSet[column_group])

for row in rows:
        for header in headers:
            inventory_row[header] = dataSet[column_group][row][column]


"""
{
 column_group1 : {
    
 
 }
}

"""

print(dataSet)

print("dataSet Details:")
print(dataSet[1][0][0])

"""

set header row in config file and read in headers
maybe convert to lower case and add _ in place of spaces
for generic google sheet scripts:
    make header a yes/no optional
    allow for multiple header rows (or areas within same row)

"""