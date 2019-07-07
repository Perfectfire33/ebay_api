import bll.dal.api_local_file_accessor

# this file matches ebay data to ebay objects
# sends objects out to api_call_sequencer file

# call_ebay_api gets api data, finds the appropriate api call set based on "script runtime" config area
# and will apply the "script runtime" to each row in the selected Google Sheet Area
# and will return an api response
def getScriptExecutionList(configDataSet):
    # Get data from "Script Runtime" Area
    scriptRuntimeData = []
    scriptRuntimeData.append(configDataSet[1][0][1])
    scriptRuntimeData.append(configDataSet[1][1][1])
    scriptRuntimeData.append(configDataSet[1][2][1])
    scriptRuntimeData.append(configDataSet[1][3][1])
    #print("scriptRuntimeData")
    #print(scriptRuntimeData)
    i = 0
    scriptExecuteList = []
    while i < scriptRuntimeData.__len__():
        if scriptRuntimeData[i] == "1":
            #print("Row = 1")
            scriptExecuteList.append(configDataSet[1][i][0])
        i = i + 1
    return scriptExecuteList


def call_ebay_api(configDataSet, appDataSet):
    # Get list of objects to create
    script_execute_list = bll.ebay_object_matcher.getScriptExecutionList(configDataSet)
    # select statement on what scripts are flagged for execution
    i = 0
    while i < script_execute_list.__len__():
        if script_execute_list[i] == "create_item_inventory":
            print("create_item_inventory")
            #for each row in inventory, make an api request payload with the data

            # Put appDataSet values inside of ebay objects and print API calls (use configDataSet values for config settings)
            all_header_groups = bll.ebay_object_receiver.createObjectsFromDataSet(appDataSet)
            #print("all_header_groups")
            #print(all_header_groups)
            #then, call the api and send body data to it
            j = 0
            itemObject = {}
            curItemData = []
            itemData = []
            # appDataSet len is
            print("len(appDataSet)")
            print(len(appDataSet))
            # BEGIN count Area (length of appDataSet)
            while j < len(appDataSet):
                for area in appDataSet[j]:
                    k = 0
                    while k < len(area):
                        itemObject[all_header_groups[j][k]] = area[k]
                        k = k + 1
                    curItemData.append(itemObject)
                    print("curItemData")
                    print(curItemData)
                # END count Area (length of appDataSet)
                j = j + 1

                itemData.append(curItemData)
                print("itemData")
                print(itemData)
            #returning the api call


        if script_execute_list[i] == "create_item_inventory_location":
            print("create_item_inventory_location")

        if script_execute_list[i] == "create_item_offer":
            print("create_item_offer")

        if script_execute_list[i] == "publish_offer":
            print("publish_offer")
        i = i + 1
    # return api_response_set



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
        file.write(call_body)

    file.close()





def tempStuff():
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