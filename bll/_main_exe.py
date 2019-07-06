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

# This definition builds the call sequence file based on needed API body response payloads
# current_api_call_body ~ a list of api call response filenames
#   (each api call with a body is associated with a filename in mapPayloadBodyToFilename in ebay_api_connector)
def writeCallSequenceFile(current_api_call_body):
    print("writeCallSequenceFile")
    configFileName = "callSequenceFile.csf"
    file = open(configFileName, 'w')
    for call_body in current_api_call_body:
        file.write(current_api_call_body)

    file.close()




repo_path = r'C:\Users\dick\Documents\GitHub'
# api_calls_dir is the file path of the api_calls folder
api_calls_dir = repo_path + r'\ebay_api\bll\dal\api_calls'
# api_call_filename_list is a list of JSON file names of the api calls in the api_calls folder
api_call_filename_list = bll.dal.api_local_file_accessor.get_api_call_filename_list(api_calls_dir)



# Identifies what api call to make
call_identifier = "createOrReplaceInventoryItem.json"
# currently selected call fileinfo (filename and index in its array)
selected_call_fileinfo = bll.dal.api_local_file_accessor.apiCallSelector(api_call_filename_list, call_identifier)
# File that contains filenames of api calls to cycle through, one per line
callSequenceFile = repo_path + r'\ebay_api\bll\callSequenceFile.csf'

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
print(call_sequence_with_dir)