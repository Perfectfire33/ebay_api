import ebay_api
from os import listdir
from os.path import isfile, join

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


# load_api_calls ~ reads in folder of request body .json files and returns array of filenames and filecontent
# filepath_token = r'\Users\Joseph\PycharmProjects\ebay_api\token.txt'
# filepath_body = r'C:\Users\Joseph\PycharmProjects\ebay_api\request_payload.json'
# api_calls_dir = r'C:\Users\Joseph\PycharmProjects\ebay_api\'
def get_api_call_filename_list(api_calls_dir):

    api_call_filename_list = [f for f in listdir(api_calls_dir) if isfile(join(api_calls_dir, f))]

    # Get JSON body of inventory item from local file (put this on google sheet, get with gsheet api?)
    #

    return api_call_filename_list

def load_api_calls(api_calls_dir, api_call_filename_list):
    call_data_array = []
    for api_call_file in api_call_filename_list:
        currentPath = api_calls_dir + "\\" + api_call_file
        # print(currentPath)
        call_data_array.append(open(currentPath).read())

    return call_data_array






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
