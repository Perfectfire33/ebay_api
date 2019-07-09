import bll.ebay_api_connector
import simplejson as json
import bll.dal.api_contract_accessor
import bll.dal.api_local_file_accessor

"""
ebay object list
    inventory_item
    location
    offer
    inventory_item_group
    
    For request_payload file:
        Create a folder of files with each file being a specific request payload (set values to placeholders, and replace placeholders with variables)
"""
# inventory_createOrReplaceInventoryItem(token, uri_env, uri_param1, body)
def createInventoryObject(filepath_token, filepath_body):
    # Get token from local file
    # (could write script to generate token and put in gsheet api,
    # then pull it from gsheet api to use it here)
    token = open(filepath_token).read()

    # eBay API requires Bearer token
    tokenPrepared = "Bearer " + token

    # Get JSON body of inventory item from local file (put this on google sheet, get with gsheet api?)
    body = open(filepath_body).read()
    # ^^ could make this a file with list of ebay API objects to create ,
    # then get data from ebay_object_reciever.py
    #
    uri_env = "sandbox"
    # Get SKU from Google Sheet eBay Inventory File?
    sku = "testItem1"

    # Call inventory_createOrReplaceInventoryItem function in ebay_api_connector.py with parameters
    api_response = bll.ebay_api_connector.inventory_createOrReplaceInventoryItem(tokenPrepared, uri_env, sku, body)

    code = api_response.status_code
    print("code")
    print(code)

    test22 = api_response.raw
    print("test22")
    print(test22)
    test33 = api_response.url
    print("test33")
    print(test33)

    print("api_response")
    print(api_response)

    return api_response



def createInventoryObjectX(filepath_token, filepath_body, uri_env):
    # Get token from local file
    # (could write script to generate token and put in gsheet api,
    # then pull it from gsheet api to use it here)
    token = open(filepath_token).read()

    # eBay API requires Bearer token
    tokenPrepared = "Bearer " + token

    # Get JSON body of inventory item from local file (put this on google sheet, get with gsheet api?)
    body = open(filepath_body).read()
    # ^^ could make this a file with list of ebay API objects to create ,
    # then get data from ebay_object_reciever.py
    #

    # Get SKU from Google Sheet eBay Inventory File?
    sku = "testItem1"
    uri_param1 = sku

    # Call inventory_createOrReplaceInventoryItem function in ebay_api_connector.py with parameters
    api_response = bll.ebay_api_connector.inventory_createOrReplaceInventoryItem(tokenPrepared, uri_env, uri_param1, body)

    code = api_response.status_code
    print("code")
    print(code)

    print("api_response")
    print(api_response)

    return api_response









# This function matches the json keys with values which are variables from the incoming dataSet
def matchFieldsWithVariables(object_type):
    print("matchFieldsWithVariables")

    if object_type == "inventoryItem":
        print("inventoryItem is current Object Type")
        filepath_body = "get current file path"
        body = open(filepath_body).read()

   # if object type is a location
    if object_type == "location":
        print("object_type == location")
        # retrieve 'add location' API call from contract
        # api_data_array.append()

        # return api_data_array

    # if object type is an offer
    if object_type == "offer":
        print("object_type == offer")
        # retrieve 'add offer' API call from contract

        # return selected api call data
        # return api_data_array

    # if object type is an inventory_item_group
    if object_type == "inventory_item_group":
        print("object_type == inventory_item_group")
        # retrieve 'add inventory_item_group' API call from contract


# This function gets the file path for the correct json request body
def getCurrentFilePath():
    print("getCurrentFilePath")






def setContractIdentifer():
    contract_identifier = 'sell_inventory_v1_oas3.json'
    return contract_identifier

def setRepoPath():
    repo_path = r'C:\Users\dick\Documents\GitHub'
    return repo_path

def getSelectedApiContractData():

    repo_path = setRepoPath()
    contract_identifier = setContractIdentifer()

    # Set api contract file directory
    api_contract_dir = repo_path + r'\ebay_api\bll\dal\api_contracts'
    # Get list of api contract filenames within directory
    api_contract_filename_list = bll.dal.api_local_file_accessor.get_api_contract_filename_list(api_contract_dir)

    # contract_data_array is an array of all the JSON contract bodies (or data of the files in the api_contracts folder)
    contract_data_array = bll.dal.api_local_file_accessor.load_api_contracts(api_contract_dir, api_contract_filename_list)

    selected_contract_fileinfo = bll.dal.api_local_file_accessor.apiContractSelector(api_contract_filename_list,
                                                                             contract_identifier)

    # print("selected_contract_fileinfo")
    # print(selected_contract_fileinfo)
    # print("selected_contract_fileinfo")

    selected_api_contract_data = bll.dal.api_local_file_accessor.apiContractAccessor(selected_contract_fileinfo,
                                                                             contract_data_array)

    return selected_api_contract_data




# determine what inventory type this object will be
# object_type - one of the items in the object list:
    #     inventory_item
    #     location
    #     offer
    #     inventory_item_group
def determineInventoryObject(object_type, crud_operation):
    print("determineInventoryObject")
    print("determine what inventory type this object will be")

    # initialize api_data_array to store selected components of the api call
    api_data_array = []

    # retrieve selected api contract data
    api_data = getSelectedApiContractData()

    # retrieve 'add inventory_item' API call from contract
    api_data_json = bll.dal.api_contract_accessor.load_selected_api_contract_data(api_data)
    api_contract_base_path = api_data_json['servers'][0]['variables']['basePath']['default']
    # retrieve list of currently selected API contract paths
    path_list = bll.dal.api_contract_accessor.get_contract_path_list(api_data_json)
    print("path_list")
    print(path_list)
    myEndpointList = {}
    for path in path_list:
        myEndpointList[path_list.index(path)] = path

    print("myEndpointList")
    print(myEndpointList)

    """if PATH is /inventory_item/{SKU}"""
    if object_type == "inventory_item":
        print("object_type == inventory_item")
        myEndpoint = myEndpointList[5]
        http_operation_list = bll.dal.api_contract_accessor.get_path_http_operation_list(myEndpoint,
                                                                                         api_data_json)
        print("http_operation_list")
        print(http_operation_list)

        """
        This API ENDPOINT will PUT an inventory_item object with 
        #   a given SKU in URI 
        #   and given DESCRIPTION in REQUEST_BODY
        """
        if crud_operation is 'create':
            print("crud_operation == create")
            # index 1 is 'put'
            myOperation = http_operation_list[1]

            endpoint_parameter_list = bll.dal.api_contract_accessor.get_endpoint_parameter_list(myEndpoint,
                                                                                                myOperation,
                                                                                                api_data_json)
            print("endpoint_parameter_list")
            print(endpoint_parameter_list)
            endpoint_request_body = bll.dal.api_contract_accessor.get_endpoint_request_body(myEndpoint,
                                                                                            myOperation,
                                                                                            api_data_json)
            print("endpoint_request_body")
            print(endpoint_request_body)


        """
        This API ENDPOINT will GET an inventory_item object and it's DESCRIPTION with 
        #   a given SKU in URI
        """
        if crud_operation is 'read':
            print("crud_operation == read")
            # index 0 is 'get'
            myOperation = http_operation_list[0]

        """ This API ENDPOINT will DELETE an inventory_item object with a given SKU in URI """
        if crud_operation is 'delete':
            print("crud_operation == delete")
            # index 2 is 'delete'
            myOperation = http_operation_list[2]







        # return selected api call data
        return api_data_array





    # if object type is a location
    if object_type == "location":
        print("object_type == location")
        # retrieve 'add location' API call from contract
        api_data_array.append()

        return api_data_array

    # if object type is an offer
    if object_type == "offer":
        print("object_type == offer")
        # retrieve 'add offer' API call from contract

        # return selected api call data
        return api_data_array

    # if object type is an inventory_item_group
    if object_type == "inventory_item_group":
        print("object_type == inventory_item_group")
        # retrieve 'add inventory_item_group' API call from contract

        # return selected api call data
        return api_data_array





# aaa
def createNewInventoryObject(filepath_token, filepath_body):
    print("createNewInventoryObject")
    # call determineInventoryObject
    newInventoryObject = determineInventoryObject()


object_type = "inventory_item"
crud_operation = "create"
tempVar = determineInventoryObject(object_type, crud_operation)
print("tempVar")
print(tempVar)




def call_ebay_api_old(configDataSet, appDataSet, uri_env):
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
    current_object_position = 0
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
            k = 2
            while k < object_count[0][0]:
                body_var1 = wjson[0][k]['item_title']
                body_var2 = wjson[1][k]['item_condition']
                body_var3 = wjson[1][k]['item_condition_description']
                body_var4 = wjson[1][k]['item_qty']
                json_payload_body['product']['title'] = body_var1
                json_payload_body['condition'] = body_var2
                json_payload_body['conditionDescription'] = body_var3
                json_payload_body['availability']['shipToLocationAvailability']['quantity'] = body_var4
                # assign second google sheet profile (vjson) (sheet2) in the inventory and grab sku
                #for now, set item_id to sku
                #uri_param1 = wjson[0][k]['item_id']
                uri_param1 = "testTTT"
                #uri_param1 = "TestDDD"
                uri_param2 = "0"

                #open, write, and close destination file
                destination_file = open(filepath_body, "w")
                destination_file.write(str(json_payload_body))
                destination_file.close()
                #open token file
                token_file = open(filepath_token).read()
                # eBay API requires Bearer token
                tokenPrepared = "Bearer " + token_file
                #read destination file
                # Get JSON body of inventory item from local file (put this on google sheet, get with gsheet api?)
                bodyX = open(filepath_body).read()
                body = bodyX.replace("\'", "\"")

                print("tokenPrepared")
                print(tokenPrepared)
                print("body")
                print(body)
                print("uri_param1")
                print(uri_param1)
                #inventory_createOrReplaceInventoryItem(token, uri_env, uri_param1, body)
                #api_response = bll.ebay_api_connector.inventory_getInventoryItem(tokenPrepared, uri_env, uri_param1)
                api_response = bll.ebay_api_connector.inventory_createOrReplaceInventoryItem(tokenPrepared, uri_env, uri_param1, body)
                #api_response = bll.ebay_api_connector.inventory_createInventoryLocation(tokenPrepared, uri_env, uri_param1, body)
                api_array.append(api_response)
                api_array.append(api_response.text)
                api_array.append(api_response.status_code)
                k = k + 1

            print("API_ARRAY")
            print(api_array)
            #area3
            # packed_item_weight_lb
            # packed_item_weight_oz
            # packed_item_height
            # packed_item_length
            # packed_item_depth
        current_object_position = current_object_position + 1
    # return api_response_set