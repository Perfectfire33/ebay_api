import bll.dal.ebay_api
import simplejson as json
import bll.dal.api_contract_accessor
import bll.dal.api_contract_access_tests
"""
EBAY_API_CONNECTOR.PY ~ CONNECT EBAY API 
TO OUR APP
"""

"""
This file:
>retrieves eBay API OwaAuth credentials in format of token.txt (if need new token: https://developer.ebay.com/my/auth?env=sandbox&index=0&auth_type=oauth )
>authenticates with eBay API using token.txt
>contains functions for specific eBay operations
    >each function:
        >prepares HTTP call (combine url, body, headers)
        >calls function in ebay_api.py (e.g. myData = ebay_api.myFunction(param1, param2) )
        >ebay_api.py returns JSON body from the eBay API
        >returns the api response (should contain http code, body converted to json, or any error message)
>To be referenced in inventory_item_cmd.py and master_cmd.py
"""

# get_api_headers presets the api_headers variable and requires the token
def get_api_headers(token):
    api_headers = {'Authorization': '%s' % token,
                   'content-type': 'application/json',
                   'Accept': 'application/json',
                   'content-language': 'en-US'}

    return api_headers

# getBaseUri retrieves and prepares the generic uri that is necessary in the http call
# Variables requires:
#   uri_env ~ sandbox or production environment
# Call Example:
#   base_uri = ebay_api_connector.getBaseUri(uri_env="sandbox")
# Used in:
#   ebay_object_defs.build_api_call()
#   this file -- ebay_api_connector
def getBaseUri(uri_env):
    if uri_env == 'sandbox':
        base_uri = 'https://api.sandbox.ebay.com'

    if uri_env == 'production':
        base_uri = 'https://api.ebay.com'

    return base_uri


""" <><><><><><><><><> BEGIN InventoryItem Object <><><><><><><><><><><> """
# uri_param1 ~~ {sku}
def inventory_createOrReplaceInventoryItem(token, uri_env, uri_param1, body):
    """Create the Inventory Item"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/inventory/v1/inventory_item/' + str(uri_param1) + '/'
    # Method Headers
    api_headers = get_api_headers(token)
    # Call the API Endpoint
    api_response = bll.dal.ebay_api.getInventoryItem(api_url, body, api_headers)
    # Return the API Response
    return api_response

# uri_param1 ~~ {sku}
def inventory_getInventoryItem(token, uri_param1, uri_env):
    """Get an Inventory Item"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/inventory/v1/inventory_item/' + str(uri_param1) + '/'
    # Method Headers
    api_headers = get_api_headers(token)
    # Call the API Endpoint
    api_response = bll.dal.ebay_api.getInventoryItem(api_url, api_headers)
    # Return the API Response
    return api_response

# uri_param1 ~~ limit
# uri_param2 ~~ offset
def inventory_getInventoryItems(token, uri_env, uri_param1, uri_param2):
    """Get Inventory Items"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get a inventory items
    api_url = base_uri + '/sell/inventory/v1/inventory_item/' + '?limit=' + uri_param1 + '&offset=' + uri_param2
    # Method Headers
    api_headers = get_api_headers(token)
    # Specify request body json data and headers
    api_response = bll.dal.ebay_api.getInventoryItem(api_url, api_headers)
    # Return the API Response
    return api_response

# uri_param1 ~~ {sku}
def inventory_deleteInventoryItem(token, uri_env, uri_param1):
    """Delete an Inventory Item"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/inventory/v1/inventory_item/' + str(uri_param1) + '/'
    # Method Headers
    api_headers = get_api_headers(token)
    # Specify request body json data and headers
    api_response = bll.dal.ebay_api.deleteInventoryItem(api_url, api_headers)
    # Return the API Response
    return api_response

def inventory_bulkUpdatePriceQuantity(token, uri_env):
    """Update Price and Quantity for bulk Inventory Items"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/inventory/v1/bulk_update_price_quantity/'
    # Method Headers
    api_headers = get_api_headers(token)
    # Specify request body json data and headers
    api_response = bll.dal.ebay_api.bulkUpdatePriceQuantity(api_url, api_headers)
    # Return the API Response
    return api_response

def inventory_bulkCreateOrReplaceInventoryItem(token, uri_env):
    """Bulk Create or Update Inventory Item"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/inventory/v1/bulk_create_or_replace_inventory_item/'
    # Method Headers
    api_headers = get_api_headers(token)
    # Specify request body json data and headers
    api_response = bll.dal.ebay_api.bulkCreateOrReplaceInventoryItem(api_url, api_headers)
    # Return the API Response
    return api_response

def inventory_bulkGetInventoryItem(token, uri_env):
    """Get a Inventory Items in Bulk"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/inventory/v1/bulk_create_or_replace_inventory_item/'
    # Method Headers
    api_headers = get_api_headers(token)
    # Specify request body json data and headers
    api_response = bll.dal.ebay_api.bulkCreateOrReplaceInventoryItem(api_url, api_headers)
    # Return the API Response
    return api_response

""" <><><><><><><><><> END InventoryItem Object <><><><><><><><><><><> """

""" <><><><><><><><><> BEGIN InventoryLocation Object <><><><><><><><><><><> """

# uri_param1 ~~ {merchantLocationKey}
def inventory_getInventoryLocation(token, uri_env, uri_param1):
    """Get an Inventory Item"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/inventory/v1/location/' + str(uri_param1) + '/'
    # Method Headers
    api_headers = get_api_headers(token)
    # Call the API Endpoint
    api_response = bll.dal.ebay_api.getInventoryItem(api_url, api_headers)
    # Return the API Response
    return api_response

# uri_param1 ~~ offset
# uri_param2 ~~ limit
def inventory_getInventoryLocations(token, uri_env, uri_param1, uri_param2):
    """Get an Inventory Item"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/inventory/v1/location/' + '?offset=' + uri_param1 + '&limit=' + uri_param2
    # Method Headers
    api_headers = get_api_headers(token)
    # Call the API Endpoint
    api_response = bll.dal.ebay_api.getInventoryItem(api_url, api_headers)
    # Return the API Response
    return api_response