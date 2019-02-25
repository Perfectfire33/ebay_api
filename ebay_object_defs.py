import ebay_api_connector
import simplejson as json
import api_contract_accessor
"""
Structure of Inventory API OpenAPI JSON Contract:
    { 
        openapi:"openapi version",
        info:{ title, description, contact:{ name:"" }, license, version},
        servers:[ url, description, variables:{ basePath:{ default:"" } } ],
        paths:{ "path_name":{ "http_type":{ 
            tags:[], 
            description:"", 
            operationId:"", 
            parameters:[ name:"", in:"", description:"", required:"", schema:{ type:"" } ], 
            responses:{ response_code:{ description:"", content:{ content_type:{ schema:{ $ref:"" } } } } } 
        }, 
        components:{ schemas:{ schema_name:{ }, securitySchemas: { api_auth: { type:"", description:"", flows:{ authorizationCode:{ authorizationUrl:"", tokenUrl:"", scopes:{ scope_list:"" } } } } } }
    }
    where
        path_name is <create function to return list of paths>
        http_type is "get", "put", "post", "delete"
        response_code is "200", "400", "404", "500"
        content_type is "application/json"
        schema_name is <create function to return list of schemas>
        scope_name is <create function to return list of scopes>
        
"""


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

    # retrieve list of currently selected API contract paths
    path_list = api_contract_accessor.getContractPaths(selected_api_contract_json)


    for path in selected_api_contract_json['paths']:
        # print("path")
        # print(path)
        if path[current_path]['get']['operationId'] == operation_id:
            #        api_contract_path = selected_api_contract_json['paths'][path]
            #        api_ = selected_api_contract_json['paths'][path]
            print("aa")
    api_pieces1 = "111"
    api_pieces2 = "222"
    built_api_call = api_pieces1 + api_pieces2
    return built_api_call























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
