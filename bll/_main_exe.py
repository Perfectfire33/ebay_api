import bll._setup_config
import bll.ebay_object_receiver
import bll.ebay_object_matcher
import json
import bll.old.ebay_object_defs
import time

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
#app data set is all the xy cells from the app's config data set (Google Sheets Data I)
#appDataSet = bll._setup_config.getGoogleSheetDataSet(data_set_type="app", data_set_data=configDataSet)
#app data set is all the xy cells from the app's config data set (Google Sheets Data II)
appDataSet2 = bll._setup_config.getGoogleSheetDataSet(data_set_type="app2", data_set_data=configDataSet)
print("appDataSet2")
print(appDataSet2)
#app data set is all the xy cells from the app's config data set (Google Sheets Data III)
appDataSet3 = bll._setup_config.getGoogleSheetDataSet(data_set_type="app3", data_set_data=configDataSet)

#api_array = bll.ebay_object_matcher.get_all_inventory_items(configDataSet, uri_env="sandbox")
#print("api_array")
#print(api_array)

# now use the appDataSet and configDataSet to bind eBay data to the eBay API call
#api_array = bll.ebay_object_matcher.create_item_inventory(configDataSet, appDataSet, appDataSet2, uri_env="sandbox")
#print("api_array")
#print(api_array)

#api_array = bll.ebay_object_matcher.create_inventory_location(configDataSet, appDataSet3, uri_env="sandbox")
#print("api_array")
#print(api_array)

#print("sleeping 8s")
#time.sleep(8)


#api_array = bll.ebay_object_matcher.get_all_inventory_locations(configDataSet, uri_env="sandbox")
#print("api_array")
#print(api_array)

# refer to https://developer.ebay.com/api-docs/static/oauth-scopes.html for production commerence scope
#api_array = bll.ebay_object_matcher.get_all_fulfillment_policies(configDataSet, uri_env="sandbox")
api_array = bll.ebay_object_matcher.get_all_payment_policies(configDataSet, uri_env="sandbox")
print("api_array")
print(api_array)
api_array2 = bll.ebay_object_matcher.get_all_fulfillment_policies(configDataSet, uri_env="sandbox")
api_array3 = bll.ebay_object_matcher.get_all_return_policies(configDataSet, uri_env="sandbox")
print("api_array2")
print(api_array2)
print("api_array3")
print(api_array3)

#api_array = bll.ebay_object_matcher.get_default_category_tree(configDataSet, uri_env="sandbox")
#print("api_array")
#print(api_array)

#api_array2 = bll.ebay_object_matcher.get_category_suggestions(configDataSet, uri_env="sandbox")
#print("api_array2")
#print(api_array2)

#repo_path = r'C:\Users\dick\Documents\GitHub'
# Set filepath token for ebay api access
#filepath_token = repo_path + r'\ebay_api\bll\token.txt'
# This is the file that includes the api call data
#filepath_body = repo_path + r'\ebay_api\bll\dal\request_payload.json'

#api_x2_response = bll.old.ebay_object_defs.createInventoryObject(filepath_token, filepath_body)
#print("api_x2_response")
#print(api_x2_response)
