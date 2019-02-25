# Import all necessary modules.
# import xlrd

from collections import OrderedDict
import simplejson as json
import shutil

# from openpyxl import load_workbook
# import bll

import os
import sys

import ebay_api_connector


"""
INVENTORY_ITEM_CMD.PY ~ EXECUTABLE COMMAND FILE
READ/WRITE TO/FROM
GOOGLE SHEET API <-> EBAY API
"""

"""
This script will pull inventory data from Google Sheets API and send it to eBay API.
Takes inventory items from the Google Spreadsheet and Adds or Replaces them to eBay's database.
"""


# ~~~~~~~~~~~~~~~~~~~~ Start Script ~~~~~~~~~~~~~~~~~~~~~ #

print("\n")

print("\n")

print("---------------------------- Start Script ---------------------------------")
print("-------------- Create or Replace Inventory Item  --------------------------")

print("\n")

filepath_token = r'\Users\Joseph\PycharmProjects\ebay_api\token.txt'
filepath_body = r'C:\Users\Joseph\PycharmProjects\ebay_api\request_payload.json'

# Get token from local file
# (could write script to generate token and put in gsheet api,
# then pull it from gsheet api to use it here)
token = open(filepath_token).read()

# eBay API requires Bearer token
tokenPrepared = "Bearer " + token

# Get JSON body of inventory item from local file (put this on google sheet, get with gsheet api?)
body = open(filepath_body).read()

# Get SKU from Google Sheet eBay Inventory File?
sku = "testItem1"

# Call inventory_createOrReplaceInventoryItem function in ebay_api_connector.py with parameters
api_response = ebay_api_connector.inventory_createOrReplaceInventoryItem(body, tokenPrepared, sku)

code = api_response.status_code
print("code")
print(code)

print("api_response")
print(api_response)


print("---------------------------- End Script ---------------------------------")










