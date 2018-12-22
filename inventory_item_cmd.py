#!/usr/bin/python
"""
This script will pull inventory data from Google Sheets API and send it to eBay API.
Takes inventory items from the Google Spreadsheet and Adds or Replaces them to eBay's database.
"""
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

# ~~~~~~~~~~~~~~~~~~~~ Start Script ~~~~~~~~~~~~~~~~~~~~~ #

print("\n")

print("\n")

print("---------------------------- Start Script ---------------------------------")
print("-------------- Create or Replace Inventory Item  --------------------------")

print("\n")

filepath_token = r'\Users\dick\PycharmProjects\ebay_api\token.txt'
filepath_body = r'C:\Users\dick\PycharmProjects\ebay_api\request_payload.json'

token = open(filepath_token).read()
tokenPrepared = "Bearer " + token

body = open(filepath_body).read()
sku = "testItem1"

api_response = ebay_api_connector.inventory_createOrReplaceInventoryItem(body, tokenPrepared, sku)

print("aaa")
code = api_response.status_code
print("code")
print(code)

print("api_response")
print(api_response)


print("---------------------------- End Script ---------------------------------")










