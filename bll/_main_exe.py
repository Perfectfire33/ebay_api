import bll._setup_config
import bll.ebay_object_receiver
import bll.ebay_object_matcher
import json
import bll.old.ebay_object_defs

"""
This script is designed to be run directly
00 Execute This Python File Directly 00
"""
configDataSet = bll._setup_config.getGoogleSheetDataSet(data_set_type="config", data_set_data="")

#print("configDataSet")
#print(configDataSet)
# use appConfigDataSet whenever need a piece of the config data throughout the app
# below, we define the appConfigDataSet
"""
appConfigDataSet Fields
XY Set Fields:
0 area1 ~ "File Output Locations"
1 area2 ~ "Script Runtime"
2 area3 ~ "Google Sheets Data 1 - Properties"
3 area4 ~ "Google Sheets Data 1 - XY Coord Sets"
4 area5 ~ "Google Sheets Data 2 - Properties"
5 area6 ~ "Google Sheets Data 2 - XY Coord Sets"
"""
#app data set is all the xy cells from the app's config data set
appDataSet = bll._setup_config.getGoogleSheetDataSet(data_set_type="app", data_set_data=configDataSet)

#print("appDataSet")
#print(appDataSet)







# def mergeJsonRows():


# now use the appDataSet and configDataSet to bind eBay data to the eBay API call
ebay_api_response = bll.ebay_object_matcher.call_ebay_api(configDataSet, appDataSet, uri_env="sandbox")
print("ebay_api_response")
print(ebay_api_response)

#repo_path = r'C:\Users\dick\Documents\GitHub'
# Set filepath token for ebay api access
#filepath_token = repo_path + r'\ebay_api\bll\token.txt'
# This is the file that includes the api call data
#filepath_body = repo_path + r'\ebay_api\bll\dal\request_payload.json'

#api_x2_response = bll.old.ebay_object_defs.createInventoryObject(filepath_token, filepath_body)
#print("api_x2_response")
#print(api_x2_response)
