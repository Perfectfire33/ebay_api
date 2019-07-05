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

    # Get SKU from Google Sheet eBay Inventory File?
    sku = "testItem1"

    # Call inventory_createOrReplaceInventoryItem function in ebay_api_connector.py with parameters
    api_response = bll.ebay_api_connector.inventory_createOrReplaceInventoryItem(body, tokenPrepared, sku)

    code = api_response.status_code
    print("code")
    print(code)

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