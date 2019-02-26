import ebay_api
import simplejson as json
import api_contract_accessor

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







# build_api_call populates a given templated api call with
#   specific call information (e.g. any uri parameters, request payload)
#   and data from Google Sheets (the getDataSet() function)
# Variables:
#   base_uri - string - https:\\api.ebay.com or https:\\api.sandbox.ebay.com
#   contract_identifier - string - name of api contract file used
#   current_api_call - string - name of api call
#   request_payload - json - request body template to be populated
#   uri_parameters - array - this contains the required values of the uri parameters
def build_api_call(base_uri, selected_api_contract_data, current_api_call, request_payload, uri_parameters):
    """
    Need to select correct(based on call name):
        1|request payload, from callSelector
        2|api contract, from contractSelector
        3|uri parameters, from <new function here>? <-- not sure how to handle uri params yet
        *may need to parse current_api_call based on delimiter*
    Result of this function:
        1| put together components of api call:
            a| URI - base_uri + api-specific uri parts + call-specific uri parts + uri params
            b| BODY - template of request payload
            c| HEADERS - header keys
    """
    # loads selected_api_contract_data into JSON-accessible format
    selected_api_contract_json = api_contract_accessor.load_selected_api_contract_data(selected_api_contract_data)

    api_contract_base_path = selected_api_contract_json['servers'][0]['variables']['basePath']['default']

    http_operation = "get"
    operation_id = "getInventoryLocation"
    print("selected_api_contract_json['paths']")
    # print number of objects in json object
    # print(len(selected_api_contract_json['paths']))
    current_path = "/location/{merchantLocationKey}"
    # print(selected_api_contract_json['paths'][current_path][http_operation]['operationId'])




    api_pieces1 = "111"
    api_pieces2 = "222"
    built_api_call = api_pieces1 + api_pieces2
    return built_api_call





















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
