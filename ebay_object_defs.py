import ebay_api_connector
import simplejson as json


"""
ebay object list
    inventory_item
    location
    offer
    inventory_item_group
    
    For request_payload file:
        Create a folder of files with each file being a specific request payload (set values to placeholders, and replace placeholders with variables)
"""
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

    selected_api_contract_json = json.loads(selected_api_contract_data)

    api_contract_base_path = selected_api_contract_json['servers'][0]['variables']['basePath']['default']
    http_operation = "get"
    operation_id = "getInventoryLocation"

    for path in selected_api_contract_json['paths']:
        if path[http_operation]['operationId'] == operation_id:
            api_contract_path = selected_api_contract_json['paths'][path]
            # api_ = selected_api_contract_json['paths'][path]




def createInventoryObject(filepath_token, filepath_body):
    # Get token from local file
    # (could write script to generate token and put in gsheet api,
    # then pull it from gsheet api to use it here)
    token = open(filepath_token).read()

    # eBay API requires Bearer token
    tokenPrepared = "Bearer " + token

    # Get JSON body of inventory item from local file (put this on google sheet, get with gsheet api?)
    body = open(filepath_body).read()

    # Get SKU from Google Sheet eBay Inventory File?
    sku = "testItem1"

    # Call inventory_createOrReplaceInventoryItem function in ebay_api_connector.py with parameters
    api_response = ebay_api_connector.inventory_createOrReplaceInventoryItem(body, tokenPrepared, sku)

    code = api_response.status_code
    print("code")
    print(code)

    print("api_response")
    print(api_response)

    return api_response
