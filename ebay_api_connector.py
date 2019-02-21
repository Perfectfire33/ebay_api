import ebay_api
from os import listdir
from os.path import isfile, join
import ebay_api_connector
import simplejson as json
"""
EBAY_API_CONNECTOR.PY ~ CONNECT EBAY API 
TO OUR APP
"""

"""
This file:
>retrieves eBay API OAuth credentials in format of token.txt (if need new token: https://developer.ebay.com/my/auth?env=sandbox&index=0&auth_type=oauth )
>authenticates with eBay API using token.txt
>contains functions for specific eBay operations
    >each function:
        >prepares HTTP call (combine url, body, headers)
        >calls function in ebay_api.py (e.g. myData = ebay_api.myFunction(param1, param2) )
        >ebay_api.py returns JSON body from the eBay API
        >returns the api response (should contain http code, body converted to json, or any error message)
>To be referenced in inventory_item_cmd.py and master_cmd.py
"""
# get_api_contract_filename_list retrieves filename list of api contracts
def get_api_contract_filename_list(api_contract_dir):
    api_contract_filename_list = [f for f in listdir(api_contract_dir) if isfile(join(api_contract_dir, f))]
    return api_contract_filename_list

# load_api_contracts retrieves the data content of the contracts specified in api_contract_filename_list
#   example: contract_data_array = load_api_contracts(api_contract_dir, api_contract_filename_list)
def load_api_contracts(api_contract_dir, api_contract_filename_list):
    contract_data_array = []
    for api_contract_file in api_contract_filename_list:
        currentPath = api_contract_dir + "\\" + api_contract_file
        # print(currentPath)
        contract_data_array.append(open(currentPath).read())

    return contract_data_array



# apiContractSelector selects an api contract to employ based on caller function
#   returns a filename and data of file from bigger array based on matching contract_identifier
# Variables:
#   contract_data_array is the data of the file
#   api_contract_filename_list is the file name (1:1 ratio with call_data_array)
#   contract_identifier is the api contract identifier (should be almost same as file name)
#   example: selected_contract_fileinfo = apiContractSelector(api_contract_filename_list, contract_identifier)
def apiContractSelector(api_contract_filename_list, contract_identifier):
    selected_contract_fileinfo = {}
    for api_contract_filename in api_contract_filename_list:
        if contract_identifier == api_contract_filename:
            selected_contract_fileinfo['filename'] = api_contract_filename
            selected_contract_fileinfo['index'] = api_contract_filename_list.index(api_contract_filename)

    return selected_contract_fileinfo

# apiContractAccessor retrieves critical data from the selected contract and returns it in a prepared format
# example: selected_api_contract_data = apiContractAccessor(selected_contract_fileinfo, contract_data_array)
def apiContractAccessor(selected_contract_fileinfo, contract_data_array):
    # get data from the api contract file
    selected_api_contract_data = contract_data_array[selected_contract_fileinfo['index']]

    return selected_api_contract_data








# load_api_calls ~ reads in folder of request body .json files and returns array of filenames and filecontent
# filepath_token = r'\Users\Joseph\PycharmProjects\ebay_api\token.txt'
# filepath_body = r'C:\Users\Joseph\PycharmProjects\ebay_api\request_payload.json'
# api_calls_dir = r'C:\Users\Joseph\PycharmProjects\ebay_api\'
def get_api_call_filename_list(api_calls_dir):
    api_call_filename_list = [f for f in listdir(api_calls_dir) if isfile(join(api_calls_dir, f))]
    # Get JSON body of inventory item from local file (put this on google sheet, get with gsheet api?)

    return api_call_filename_list


# load_api_calls retrieves the data content of the api calls specified in api_call_filename_list
def load_api_calls(api_calls_dir, api_call_filename_list):
    call_data_array = []
    for api_call_file in api_call_filename_list:
        currentPath = api_calls_dir + "\\" + api_call_file
        # print(currentPath)
        call_data_array.append(open(currentPath).read())

    return call_data_array



# apiCallSelector selects an api call to prepare based on caller function
#   returns a filename and data of file from bigger array based on matching call_identifier
# Variables:
#   call_data_array is the data of the file
#   api_call_filename_list is the file name (1:1 ratio with call_data_array)
#   call_identifier is the api call identifier (should be almost same as file name)
def apiCallSelector(api_call_filename_list, call_identifier):
    selected_call_fileinfo = {}
    for api_call_filename in api_call_filename_list:
        if call_identifier == api_call_filename:
            selected_call_fileinfo['filename'] = api_call_filename
            selected_call_fileinfo['index'] = api_call_filename_list.index(api_call_filename)

    return selected_call_fileinfo




# callSequence reads in a sequence file and returns an array of call names and call data
def callSequence(callSequenceFile, api_call_filename_list, api_calls_dir):
    # get list of call names from file
    call_sequence = tuple(open(callSequenceFile, 'r'))
    # get all call data at once
    call_data_array = load_api_calls(api_calls_dir, api_call_filename_list)
    # create array for fileinfo
    call_sequence_set_fileinfo = []
    # create array for data of files in sequence set
    call_sequence_set_filedata = []

    # loop for each api call in the api call sequence
    for call_identifier in call_sequence:
        # select the index from the file name array and match it to the index of the data array
        s_call_identifer = call_identifier.split("\n")
        # select what call from pool of calls that match the current call in the sequence
        selected_call_fileinfo = ebay_api_connector.apiCallSelector(api_call_filename_list, s_call_identifer[0])
        # add the filename and index of current selected call to filename array
        call_sequence_set_fileinfo.append(selected_call_fileinfo)
        call_sequence_set_filedata.append(call_data_array[selected_call_fileinfo['index']])

    # create array of filepaths and filedata
    call_sequence_set = []
    call_sequence_set.append(call_sequence_set_fileinfo)
    call_sequence_set.append(call_sequence_set_filedata)
    call_sequence_with_dir = {}
    call_sequence_with_dir['call_sequence_set'] = call_sequence_set
    call_sequence_with_dir['api_calls_dir'] = api_calls_dir

    return call_sequence_with_dir


# executeCallSequenceFile takes the prepared call_sequence_with_dir and executes each call against the API and
#   returns an array of api responses
def executeCallSequenceFile(call_sequence_with_dir):
    print('test')
    # For each call in call sequence,
    # identify appropriate function based on call name,
    #   (potentially need to build a table that maps the file call name to API call name if they are to differ)
    # execute the function to get that api's response,
    # and add the whole response to an array of responses
    #   (will need to then parse the response in another function and use that data based on call success or error)
    print('test')



# parseExecutedCallSequence takes the executed_call_sequence and takes action based on each call's response
def parseExecutedCallSequence(executed_call_sequence):
    print('test')
    # AA
    # AA
    print('test')

# getBaseUri retrieves and prepares the generic uri that is necessary in the http call
# Variables requires:
#   uri_env ~ sandbox or production environment
# Call Example:
#   base_uri = ebay_api_connector.getBaseUri(uri_env="sandbox")
# Used in:
#   ebay_object_defs.build_api_call()
def getBaseUri(uri_env):
    if uri_env == 'sandbox':
        base_uri = 'https://api.sandbox.ebay.com'

    if uri_env == 'production':
        base_uri = 'https://api.ebay.com'

    # selected_api_contract_data = ebay_api_connector.apiContractAccessor(selected_contract_fileinfo, contract_data_array)
    # selected_api_contract_json = json.loads(selected_api_contract_data)
    # selected_api_contract_json = json.loads(selected_api_contract_data)
    # print("selected_api_contract_data.info")
    # print(selected_api_contract_json['info']['title'])

    # print('base_uri')
    # print(base_uri)
    return base_uri


def inventory_createOrReplaceInventoryItem(body, token, sku):

    """Create the Inventory Item"""

    # This is the ebay URL used to add or update an inventory item                      *****IMPORTANT*****
    api_url = 'https://api.sandbox.ebay.com/sell/inventory/v1/inventory_item/' + str(sku) + '/' # <--- Use this test env url first then Prod
                                                            # Prod env url: https://api.ebay.com

    # Method body
    api_payload = body

    # Method Headers
    api_headers = {'Authorization': '%s' % token,
                            'content-type': 'application/json',
                            'Accept': 'application/json',
                            'content-language': 'en-US'}

    # Specify request body json data and headers
    api_response = ebay_api.createOrReplaceInventoryItem(api_url, api_payload, api_headers)

    """ Store the addTestCase response """
    """Create the Test Case"""
    # Use the .json function() to get the data in json format and then we store it in api_response variable
    # api_response = api_response.json()
    return api_response







def inventory_createOrReplaceInventoryItem(body, token, sku):

    """Create the Inventory Item"""

    # This is the ebay URL used to add or update an inventory item                      *****IMPORTANT*****
    api_url = 'https://api.sandbox.ebay.com/sell/inventory/v1/inventory_item/' + str(sku) + '/' # <--- Use this test env url first then Prod
                                                            # Prod env url: https://api.ebay.com

    # Method body
    api_payload = body

    # Method Headers
    api_headers = {'Authorization': '%s' % token,
                            'content-type': 'application/json',
                            'Accept': 'application/json',
                            'content-language': 'en-US'}

    # Specify request body json data and headers
    api_response = ebay_api.createOrReplaceInventoryItem(api_url, api_payload, api_headers)

    """ Store the addTestCase response """
    """Create the Test Case"""
    # Use the .json function() to get the data in json format and then we store it in api_response variable
    # api_response = api_response.json()
    return api_response
