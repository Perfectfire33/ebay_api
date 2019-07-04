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
    selected_api_contract_json = bll.dal.api_contract_accessor.load_selected_api_contract_data(selected_api_contract_data)

    api_contract_base_path = selected_api_contract_json['servers'][0]['variables']['basePath']['default']

    http_operation = "get"
    operation_id = "getInventoryLocation"
    print("selected_api_contract_json['paths']")
    # print number of objects in json object
    # print(len(selected_api_contract_json['paths']))
    current_path = "/location/{merchantLocationKey}"
    # print(selected_api_contract_json['paths'][current_path][http_operation]['operationId'])

    built_api_call = bll.dal.api_contract_access_tests.api_contract_access_tests(selected_api_contract_data)




    # api_pieces1 = "111"
    # api_pieces2 = "222"
    # built_api_call = api_pieces1 + api_pieces2
    return built_api_call


# once call is determined, find call among contracts,
# then build call template from selected contract:
#   request payload template
#   uri template
#   uri parameters template
#       notes:
#           build function to 'find' an api in a contract... example unique api name:
#               'ebay_api.commerce_api.assignCategoryToOffer'
#
#           could also use this in other way to pass parameters with an api call:
#               'ebay_api.commerce_api.assignCategoryToOffer(category, offer)'
#               this string would be manually parsed by scripts to know what to do
#
#           this string would then be a line in a sequence file
#           the api_templator (not api_sequencer) would create four files in
#           four directory folders: call, uri, params, headers
#           with proper template for the supplied api call



# once call template from selected contract is built,
# then populate template with call data from google sheets data object:
#   request payload data
#   uri data
#   uri parameter data
#
# data may also be taken from other sources, as necessary, to make a complete api call
# (e.g. uri params for searching may be in a txt file)

# once call is built with data, send to proper API



# api_finder locates an api call within a contract or set of contracts
def api_finder(operationId):
    abc = ""

    return abc


"""
legend:
    api_finder      ....    function that locates an api call within a contract or set of contracts
    api_templator   ....    function that builds template files from a located api
    api_populator   ....    function that grabs data from google sheets object and inserts it into api template files

overview of process:
    1|  command script sends what api call is necessary to api_finder 
    2|  api_finder locates the call and sends location data to api_templator
    3|  api_templator creates files for one api call at a time from contract data
    4|  api_populator takes data from identified google sheet object and 
            fills in the template, building a complete api call
    4|  api_sequencer then takes in the populated files (needs to be improved to handle uris, params, and headers)
            and creates data structure for app to access



gsheets_data_identifier ....    function that takes data from google sheets object based on api_populator info
                                and returns the data in a usable object (object schema determined by api_populator)
                                to api_populator

object_schema_selector  ....    selects the object schema 


function workflow:
    a. api_finder
    b. api_templator
    c. api_populator
        i. gsheets_data_identifier
    d. api_sequencer

"""

"""
big overview (all workflow) summary:

    A. 
    B. api_sequencer
        a. api_finder
        b. api_templator
        c. api_populator
            i. gsheets_data_identifier
    C. 
    D. 
    E. 
    F. 
    G. 
    H. 
    I. 




"""


def originalInventory_createOrReplaceInventoryItem(body, token, sku):

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
    api_response = bll.dal.ebay_api.createOrReplaceInventoryItem(api_url, api_payload, api_headers)

    """ Store the addTestCase response """
    """Create the Test Case"""
    # Use the .json function() to get the data in json format and then we store it in api_response variable
    # api_response = api_response.json()
    return api_response