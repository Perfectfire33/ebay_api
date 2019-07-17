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


#api_response = bll.ebay_object_matcher.write_to_sheet()
#print("api_response")
#print(api_response)


#api_array = bll.ebay_object_matcher.get_authorize_code(uri_env="production")
#api_array = bll.ebay_object_matcher.get_user_access_token(configDataSet,
#                                                          uri_env="sandbox",
#                                                          auth_code="v%5E1.1%23i%5E1%23I%5E3%23r%5E1%23p%5E3%23f%5E0%23t%5EUl41XzQ6OEMwQkRDNzFDMjA2QzVDQjUxQ0M5NDBFODAxRDdDN0JfMF8xI0VeMTI4NA%3D%3D")

#print("api_array")
#print(api_array)

# variable1 = "get_all_inventory_items"
#if variable1 == "get_all_inventory_items":


# app data set is all the xy cells from the app's config data set (Google Sheets Data I)
appDataSet = bll._setup_config.getGoogleSheetDataSet(data_set_type="app", data_set_data=configDataSet)
# app data set is all the xy cells from the app's config data set (Google Sheets Data II)
appDataSet2 = bll._setup_config.getGoogleSheetDataSet(data_set_type="app2", data_set_data=configDataSet)
# app data set is all the xy cells from the app's config data set (Google Sheets Data III)
#appDataSet3 = bll._setup_config.getGoogleSheetDataSet(data_set_type="app3", data_set_data=configDataSet)

# now use the appDataSet and configDataSet to bind eBay data to the eBay API call

""" PHOTOS """
#api_array = bll.ebay_object_matcher.createPictureFolders(configDataSet, appDataSet2)

#api_array = bll.ebay_object_matcher.create_url(configDataSet)

# get index of the entry


#print("current_item_index")
#print(current_item_index)


""" INVENTORY ITEMS """
#api_array = bll.ebay_object_matcher.create_item_inventory(configDataSet, appDataSet, appDataSet2, uri_env="production")
#api_array = bll.ebay_object_matcher.get_all_inventory_items(configDataSet, uri_env="production")
api_array = bll.ebay_object_matcher.write_get_all_inventory_items_to_sheet(configDataSet, uri_env="production")
#api_array = bll.ebay_object_matcher.delete_list_of_inventory_items(configDataSet, appDataSet, uri_env="production")
#api_array = bll.ebay_object_matcher.delete_item_inventory(configDataSet, uri_env="sandbox", sku="00001")

""" LOCATIONS """
#api_array = bll.ebay_object_matcher.create_inventory_location(configDataSet, appDataSet3, uri_env="production")
#api_array = bll.ebay_object_matcher.get_all_inventory_locations(configDataSet, uri_env="production")




""" OFFERS """
#api_array = bll.ebay_object_matcher.delete_list_of_inventory_offers(configDataSet, appDataSet, uri_env="production")
#api_array = bll.ebay_object_matcher.get_list_of_item_offers_for_list_of_items(configDataSet, appDataSet, uri_env="production")
#api_array = bll.ebay_object_matcher.write_get_all_offers_to_sheet(configDataSet, appDataSet, uri_env="production")
#api_array = bll.ebay_object_matcher.create_item_offer(configDataSet, appDataSet, appDataSet2, uri_env="production")
#api_array = bll.ebay_object_matcher.publish_item_offer(configDataSet, uri_env="production", offer_id="29508536014")
#api_array = bll.ebay_object_matcher.withdraw_item_offer(configDataSet, uri_env="production", offer_id="29508535014")

""" POLICIES """
#api_array = bll.ebay_object_matcher.get_all_fulfillment_policies(configDataSet, uri_env="sandbox")
#api_array = bll.ebay_object_matcher.get_all_payment_policies(configDataSet, uri_env="sandbox")

#api_array = bll.ebay_object_matcher.getListOfPaymentPolicyNames(configDataSet, uri_env="production")
#api_array = bll.ebay_object_matcher.getListOfFulfillmentPolicyNames(configDataSet, uri_env="production")
#api_array = bll.ebay_object_matcher.getListOfReturnPolicyNames(configDataSet, uri_env="production")

#api_array = bll.ebay_object_matcher.get_all_fulfillment_policies(configDataSet, uri_env="sandbox")
#api_array = bll.ebay_object_matcher.get_all_return_policies(configDataSet, uri_env="production")

#api_array = bll.ebay_object_matcher.create_fulfillment_policy(configDataSet, uri_env="sandbox")
#api_array = bll.ebay_object_matcher.create_return_policy(configDataSet, uri_env="sandbox")
#api_array = bll.ebay_object_matcher.create_payment_policy(configDataSet, uri_env="sandbox")

#api_array = bll.ebay_object_matcher.get_fulfillment_policy_id_list_via_name(configDataSet, appDataSet, uri_env="sandbox")
#api_array = bll.ebay_object_matcher.get_return_policy_id_list_via_name(configDataSet, appDataSet, uri_env="sandbox")
#api_array = bll.ebay_object_matcher.get_payment_policy_id_list_via_name(configDataSet, appDataSet, uri_env="sandbox")


""" CATEGORIES """
#api_array = bll.ebay_object_matcher.get_default_category_tree(configDataSet, uri_env="sandbox")
#api_array = bll.ebay_object_matcher.get_category_suggestions(configDataSet, uri_env="production")

print("api_array")
print(api_array)