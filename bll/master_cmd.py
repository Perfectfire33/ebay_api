from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import bll.gsheets_api_connector
import bll.ebay_api_connector
import bll.ebay_object_defs
import bll.dal.api_local_file_accessor
import bll.dal.api_sequencer
import os
import sys
import simplejson as json
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
configData = bll.gsheets_api_connector.readConfigFile()
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
# listOfAcceptableFields = gsheets_api_connector.getAcceptableFields(p3, p4, p5, p6, p7)

# Acquire Set of Google Sheet Data
# dataSet = gsheets_api_connector.getDataSet(p1, p2, listOfAcceptableFields)
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
#   This should eventually be set in config file
#   JOSEPH-PC:          api_calls_dir = r'C:\Users\Joseph\PycharmProjects\ebay_api\api_calls'
#   DICK-PC:            api_calls_dir = r'C:\Users\dick\Documents\GitHub\ebay_api\api_calls'
#   WIN-UJAOO6FHEGF:    api_calls_dir = r'C:\Users\Joseph\Documents\GitHub\ebay_api\api_calls'
# repo_path = r'C:\Users\Joseph\Documents\GitHub'
repo_path = r'C:\Users\dick\Documents\GitHub'


# api_calls_dir is the file path of the api_calls folder

# api_calls_dir = r'C:\Users\dick\Documents\GitHub\ebay_api\api_calls'
api_calls_dir = repo_path + r'\ebay_api\api_calls'
# api_call_filename_list is a list of JSON file names of the api calls in the api_calls folder
api_call_filename_list = bll.dal.api_local_file_accessor.get_api_call_filename_list(api_calls_dir)

# print("api_call_filename_list")
# print(api_call_filename_list)

# call_data_array is an array of all the JSON request payload bodies (or data of the files in the api_calls folder)
# call_data_array = ebay_api_connector.load_api_calls(api_calls_dir, api_call_filename_list)



# Set api contract file directory
api_contract_dir = repo_path + r'\ebay_api\api_contracts'
# Get list of api contract filenames within directory
api_contract_filename_list = bll.dal.api_local_file_accessor.get_api_contract_filename_list(api_contract_dir)
# contract_data_array is an array of all the JSON contract bodies (or data of the files in the api_contracts folder)
contract_data_array = bll.dal.api_local_file_accessor.load_api_contracts(api_contract_dir, api_contract_filename_list)
contract_identifier = 'sell_inventory_v1_oas3.json'
selected_contract_fileinfo = bll.dal.api_local_file_accessor.apiContractSelector(api_contract_filename_list, contract_identifier)
selected_api_contract_data = bll.dal.api_local_file_accessor.apiContractAccessor(selected_contract_fileinfo, contract_data_array)




# Identifies what api call to make
call_identifier = "createOrReplaceInventoryItem.json"
# currently selected call fileinfo (filename and index in its array)
selected_call_fileinfo = bll.dal.api_local_file_accessor.apiCallSelector(api_call_filename_list, call_identifier)
# File that contains filenames of api calls to cycle through, one per line
callSequenceFile = repo_path + r'\ebay_api\callSequenceFile.csf'

""" Data of call_sequence_with_dir:
#   # create array of filepaths and filedata
#   call_sequence_set = []
#   call_sequence_set.append(call_sequence_set_fileinfo)
#   call_sequence_set.append(call_sequence_set_filedata)
#   call_sequence_with_dir = {}
#
#   # add set of call sequence to list
#   call_sequence_with_dir['call_sequence_set'] = call_sequence_set
#   # add the api_calls_dir to the list as well
#   call_sequence_with_dir['api_calls_dir'] = api_calls_dir
"""
# Get the data of the call sequence
# (object includes:
#   current api_calls directory and
#   array of api calls that includes:
#       filename,
#       index of filename,
#       and data of file
# )
call_sequence_with_dir = bll.dal.api_sequencer.callSequence(callSequenceFile, api_call_filename_list, api_calls_dir)
# print(call_sequence_with_dir)

# Set filepath token for ebay api access
filepath_token = repo_path + r'\ebay_api\bll\token.txt'
# This is the file that includes the api call data
filepath_body = repo_path + r'\ebay_api\bll\dal\request_payload.json'


uri_env="sandbox"
base_uri = bll.dal.ebay_api_connector.getBaseUri(uri_env)
# print('base_uri')
# print(base_uri)

# For now, set index to one.
current_call_index = 0
# Set data of generic call
request_payload = call_sequence_with_dir['call_sequence_set'][0][current_call_index]
# Set name of generic call
current_api_call = call_sequence_with_dir['call_sequence_set'][1][current_call_index]
# Set uri_parameters of generic call
uri_parameters = ""
current_api_call_built = bll.dal.ebay_api_connector.build_api_call(base_uri, selected_api_contract_data, current_api_call, request_payload, uri_parameters)

print("current_api_call_built")
print(current_api_call_built)






"""
1| use master_cmd.py as executable script (need to maybe add menu options?)
2| gsheets_api_connector.py calls read/write to spreadsheet functions in gsheets_api.py
2| gsheets_api_connector.py reads in a config file to know what areas of what sheets to interface with
2| gsheets_api_connector.py can output a big data array of areas specified in the config profile
3| need a new file for taking data from the big data array and making various app-specific objects
4| this file initially is ebay-specific. Duplicate-style files can be made if interfacing with other APIs
5| this file will prepare data from the spreadsheet and apply it to an app-specific (e.g. ebay inventory) schema
6| a second new file will take objects with populated data and combine them as necessary
        e.g. an API needs data from profile1 (spreadsheet1,sheet1,YX-YX) AND profile2 (spreadsheet2,sheet1,YX-YX)
        e.g. an API need a new object11 from object1,object2,object7 in profile1 (spreadsheet1,sheet1,YX-YX)
        idea: create a deriveObjectsFromProfile(schema) where 'schema' is the set of column headers to identify data
7| then, the data is prepared so <insert function here> can use it to hit an API and return a result
8| <insert function here> returns a result and <insert other function here> processes it (based on an input schema?)
9| the data is then pushed to a database (e.g. Google Sheets using gsheets_api_connector.py)
10| should retrieve a result saying that data has been successfully written (or when any operation completes)

"""





























