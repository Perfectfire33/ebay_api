import bll._setup_config
import bll.ebay_object_receiver

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


# Put appDataSet values inside of ebay objects and print API calls (use configDataSet values for config settings)
all_header_groups = bll.ebay_object_receiver.createObjectsFromDataSet(appDataSet)
print("all_header_groups")
print(all_header_groups)


# Execute API calls per configDataSet values ("Script Runtime" area2), returning api response data into proper file

# once this file (_main_exe.py) has ran, write back current time in
#   "ebay-config-data"."config_data"."Script Runtime"."Script Last Executed"


