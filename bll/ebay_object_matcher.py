import bll.dal.api_local_file_accessor
import bll.ebay_object_receiver
import json
import bll.ebay_api_connector

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




# get number of items in inventory from loadJsonData() and operation list from "Script Runtime"
#   (take data from each item and put into a request body)
# getObjectCount retrieves what operations and the number of operation executions
#   based on number of keys in the json variable in appDataSet , and
#   based on the Script Name where Property Value equals 1 in ebay-config-data from configDataSet
def getObjectCount(configDataSet, appDataSet):
    #print("begin getObjectCount")
    # Import JSON header-data matched object
    wjson = bll.ebay_object_receiver.loadJsonData(appDataSet)
    # Get list of object types to count
    script_execute_list = bll.ebay_object_matcher.getScriptExecutionList(configDataSet)
    #print("script_execute_list")
    #print(script_execute_list.__len__())
    # select statement on what scripts are flagged for execution
    i = 0
    objectCountAccumulator = []
    objectScriptTypeAccumulator = []
    while i < script_execute_list.__len__():
        if script_execute_list[i] == "create_item_inventory":
            #print("create_item_inventory")
            counter = 0
            #print("len(wjson)")
            #print(len(wjson))
            #print("range(len(wjson))")
            #print(range(len(wjson)))
            #print("begin for loop")
            #for each row in inventory, make an api request payload with the data
            for object in range(len(wjson[0])):
                #print("object" + str(j))
                #print(object)
                #print("wjson[0][0]")
                #print(wjson[0][1])
                #print("wjson[area0][counter]['item_id']")
                #print(wjson[0][counter]['item_id'])
                counter = counter + 1
            objectCountAccumulator.append(counter)
            objectScriptTypeAccumulator.append(script_execute_list[i])

        if script_execute_list[i] == "create_item_inventory_location":
            #print("create_item_inventory_location")
            counter = 0
            #this for loop in range(len(wjson[0])) might have to be different for inventory location
            #   if data is grabbed from different area of sheet
            for object in range(len(wjson[0])):
                counter = counter + 1
            objectCountAccumulator.append(counter)
            objectScriptTypeAccumulator.append(script_execute_list[i])

        if script_execute_list[i] == "create_item_offer":
            #print("create_item_offer")
            counter = 0
            for object in range(len(wjson[0])):
                counter = counter + 1
            objectCountAccumulator.append(counter)
            objectScriptTypeAccumulator.append(script_execute_list[i])

        if script_execute_list[i] == "publish_offer":
            #print("publish_offer")
            counter = 0
            for object in range(len(wjson[0])):
                counter = counter + 1
            objectCountAccumulator.append(counter)
            objectScriptTypeAccumulator.append(script_execute_list[i])
        i = i + 1
    objectCount = []
    objectCount.append(objectCountAccumulator)
    objectCount.append(objectScriptTypeAccumulator)
    return objectCount


def call_ebay_api(configDataSet, appDataSet, uri_env):
    # for each row in inventory, make an api request payload with the data
    object_count = bll.ebay_object_matcher.getObjectCount(configDataSet, appDataSet)
    #print("object_count")
    #print(object_count)
    # Import JSON header-data matched object
    wjson = bll.ebay_object_receiver.loadJsonData(appDataSet)
    # Set filepath token for ebay api access
    filepath_token = configDataSet[0][2][2] + configDataSet[0][2][1]
    # This is the file that includes the api call data
    filepath_body = configDataSet[0][6][2] + configDataSet[0][6][1]
    # This is the folder of the json request payload files
    api_payload_folder = configDataSet[0][7][2]
    payloadFilenameMap = bll.ebay_api_connector.getPayloadFilenameMap()
    """
    For each script:
        1| select each json payload and update it according to the endpoint
    """
    for script in object_count[1]:
        #array of API call responses
        api_array = []
        if script == "create_item_inventory":
            # open the right payload file with json data
            api_payload_filename = api_payload_folder + payloadFilenameMap['inventory_createOrReplaceInventoryItem']
            #api_payload_filename = api_payload_folder + payloadFilenameMap['inventory_createInventoryLocation']
            api_payload_file = open(api_payload_filename, "r")
            # replace values in json_payload_body with data from wjson variable
            json_payload_body = json.load(api_payload_file)
            api_payload_file.close()
            k = 0
            while k < object_count[0][0]:
                body_var1 = wjson[0][k]['item_title']
                body_var2 = wjson[1][k]['item_condition']
                body_var3 = wjson[1][k]['item_condition_description']
                body_var4 = wjson[1][k]['item_qty']
                body_var5 = wjson[2][k]['packed_item_weight_lb']
                body_var6 = wjson[2][k]['packed_item_weight_oz']
                body_var7 = wjson[2][k]['packed_item_height']
                body_var8 = wjson[2][k]['packed_item_length']
                body_var9 = wjson[2][k]['packed_item_depth']
                json_payload_body['product']['title'] = body_var1
                json_payload_body['condition'] = body_var2
                json_payload_body['conditionDescription'] = body_var3
                json_payload_body['availability']['shipToLocationAvailability']['quantity'] = body_var4
                #json_payload_body['availability']['pickupAtLocationAvailability']['quantity'] = body_var5
                # area3
                # packed_item_weight_lb
                # packed_item_weight_oz
                # packed_item_height
                # packed_item_length
                # packed_item_depth

                # assign second google sheet profile (vjson) (sheet2) in the inventory and grab sku
                #for now, set item_id to sku
                uri_param1 = wjson[0][k]['item_id']
                #open token file
                token_file = open(filepath_token).read()
                # eBay API requires Bearer token
                tokenPrepared = "Bearer " + token_file
                #read destination file
                # Get JSON body of inventory item from local file (put this on google sheet, get with gsheet api?)
                body_string = str(json_payload_body)
                body = body_string.replace("\'", "\"")
                api_response = bll.ebay_api_connector.inventory_createOrReplaceInventoryItem(tokenPrepared, uri_env, uri_param1, body)
                api_array.append(api_response)
                api_array.append(api_response.text)
                api_array.append(api_response.status_code)
                k = k + 1

            print("API_ARRAY")
            print(api_array)
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