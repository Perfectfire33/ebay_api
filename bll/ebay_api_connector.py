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

# inventory_createOrReplaceInventoryItem request body uses /api_calls/createOrReplaceIventoryItem.json
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

# inventory_bulkUpdatePriceQuantity request body uses /api_calls/bulkUpdatePriceQuantity.json
def inventory_bulkUpdatePriceQuantity(token, uri_env, body):
    """Update Price and Quantity for bulk Inventory Items"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/inventory/v1/bulk_update_price_quantity/'
    # Method Headers
    api_headers = get_api_headers(token)
    # Specify request body json data and headers
    api_response = bll.dal.ebay_api.bulkUpdatePriceQuantity(api_url, api_headers, body)
    # Return the API Response
    return api_response

# inventory_bulkCreateOrReplaceInventoryItem request body uses /api_calls/bulkCreateOrReplaceInventoryItem.json
def inventory_bulkCreateOrReplaceInventoryItem(token, uri_env, body):
    """Bulk Create or Update Inventory Item"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/inventory/v1/bulk_create_or_replace_inventory_item/'
    # Method Headers
    api_headers = get_api_headers(token)
    # Specify request body json data and headers
    api_response = bll.dal.ebay_api.bulkCreateOrReplaceInventoryItem(api_url, body, api_headers)
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
    api_response = bll.dal.ebay_api.bulkGetInventoryItem(api_url, api_headers)
    # Return the API Response
    return api_response

""" <><><><><><><><><> END InventoryItem Object <><><><><><><><><><><> """

""" <><><><><><><><><> BEGIN InventoryLocation Object <><><><><><><><><><><> """

# uri_param1 ~~ {merchantLocationKey}
def inventory_getInventoryLocation(token, uri_env, uri_param1):
    """Get an Inventory Location"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/inventory/v1/location/' + str(uri_param1) + '/'
    # Method Headers
    api_headers = get_api_headers(token)
    # Call the API Endpoint
    api_response = bll.dal.ebay_api.getInventoryLocation(api_url, api_headers)
    # Return the API Response
    return api_response

# uri_param1 ~~ offset
# uri_param2 ~~ limit
def inventory_getInventoryLocations(token, uri_env, uri_param1, uri_param2):
    """Get Inventory Locations"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/inventory/v1/location/' + '?offset=' + uri_param1 + '&limit=' + uri_param2
    # Method Headers
    api_headers = get_api_headers(token)
    # Call the API Endpoint
    api_response = bll.dal.ebay_api.getInventoryLocations(api_url, api_headers)
    # Return the API Response
    return api_response

# inventory_createInventoryLocation request body uses /api_calls/createInventoryLocation.json
# uri_param1 ~~ {merchantLocationKey}
def inventory_createInventoryLocation(token, uri_env, uri_param1, body):
    """Create the Inventory Location"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/inventory/v1/location/' + str(uri_param1) + '/'
    # Method Headers
    api_headers = get_api_headers(token)
    # Call the API Endpoint
    api_response = bll.dal.ebay_api.createInventoryLocation(api_url, body, api_headers)
    # Return the API Response
    return api_response


# uri_param1 ~~ {merchantLocationKey}
def inventory_disableInventoryLocation(token, uri_env, uri_param1):
    """Disable the Inventory Location"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/inventory/v1/location/' + str(uri_param1) + '/disable'
    # Method Headers
    api_headers = get_api_headers(token)
    # Call the API Endpoint
    api_response = bll.dal.ebay_api.disableInventoryLocation(api_url, api_headers)
    # Return the API Response
    return api_response

# uri_param1 ~~ {merchantLocationKey}
def inventory_enableInventoryLocation(token, uri_env, uri_param1):
    """Enable the Inventory Location"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/inventory/v1/location/' + str(uri_param1) + '/enable'
    # Method Headers
    api_headers = get_api_headers(token)
    # Call the API Endpoint
    api_response = bll.dal.ebay_api.enableInventoryLocation(api_url, api_headers)
    # Return the API Response
    return api_response

# uri_param1 ~~ {merchantLocationKey}
def inventory_deleteInventoryLocation(token, uri_env, uri_param1):
    """Delete the Inventory Location"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/inventory/v1/location/' + str(uri_param1) + '/'
    # Method Headers
    api_headers = get_api_headers(token)
    # Call the API Endpoint
    api_response = bll.dal.ebay_api.deleteInventoryLocation(api_url, api_headers)
    # Return the API Response
    return api_response


# uri_param1 ~~ {merchantLocationKey}
def inventory_updateInventoryLocation(token, uri_env, uri_param1, body):
    """Update the Inventory Location"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/inventory/v1/location/' + str(uri_param1) + '/'
    # Method Headers
    api_headers = get_api_headers(token)
    # Call the API Endpoint
    api_response = bll.dal.ebay_api.updateInventoryLocation(api_url, body, api_headers)
    # Return the API Response
    return api_response


""" <><><><><><><><><> END InventoryLocation Object <><><><><><><><><><><> """

""" <><><><><><><><><> BEGIN Offer Object <><><><><><><><><><><> """
# inventory_createOffer request body uses /api_calls/createOffer.json
def inventory_createOffer(token, uri_env, body):
    """Create the Inventory Offer"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/inventory/v1/offer/'
    # Method Headers
    api_headers = get_api_headers(token)
    # Call the API Endpoint
    api_response = bll.dal.ebay_api.createOffer(api_url, body, api_headers)
    # Return the API Response
    return api_response

# inventory_updateOffer request body uses /api_calls/createOffer.json
# uri_param1 ~~ {offerId}
def inventory_updateOffer(token, uri_env, uri_param1, body):
    """Update the Inventory Offer"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/inventory/v1/offer/' + str(uri_param1) + '/'
    # Method Headers
    api_headers = get_api_headers(token)
    # Call the API Endpoint
    api_response = bll.dal.ebay_api.updateOffer(api_url, body, api_headers)
    # Return the API Response
    return api_response

# uri_param1 ~~ {offerId}
def inventory_deleteOffer(token, uri_env, uri_param1):
    """Delete the Inventory Offer"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/inventory/v1/offer/' + str(uri_param1) + '/'
    # Method Headers
    api_headers = get_api_headers(token)
    # Call the API Endpoint
    api_response = bll.dal.ebay_api.deleteOffer(api_url, api_headers)
    # Return the API Response
    return api_response

# uri_param1 ~~ {offerId}
def inventory_publishOffer(token, uri_env, uri_param1):
    """Publish the Inventory Offer"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/inventory/v1/offer/' + str(uri_param1) + '/publish/'
    # Method Headers
    api_headers = get_api_headers(token)
    # Call the API Endpoint
    api_response = bll.dal.ebay_api.publishOffer(api_url, api_headers)
    # Return the API Response
    return api_response

# uri_param1 ~~ {offerId}
def inventory_withdrawOffer(token, uri_env, uri_param1):
    """Withdraw the Inventory Offer"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/inventory/v1/offer/' + str(uri_param1) + '/withdraw/'
    # Method Headers
    api_headers = get_api_headers(token)
    # Call the API Endpoint
    api_response = bll.dal.ebay_api.withdrawOffer(api_url, api_headers)
    # Return the API Response
    return api_response

# uri_param1 ~~ {offerId}
def inventory_getOffer(token, uri_env, uri_param1):
    """Get the Inventory Offer"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/inventory/v1/offer/' + str(uri_param1) + '/'
    # Method Headers
    api_headers = get_api_headers(token)
    # Call the API Endpoint
    api_response = bll.dal.ebay_api.getOffer(api_url, api_headers)
    # Return the API Response
    return api_response

# uri_param1 ~~ {sku}
# uri_param2 ~~ {marketplace_id}
# uri_param3 ~~ {format}
# uri_param4 ~~ {limit}
# uri_param5 ~~ {offset}
def inventory_getOffers(token, uri_env, uri_param1, uri_param2, uri_param3, uri_param4, uri_param5):
    """Get Inventory Offers"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/inventory/v1/offer/' + \
              '?sku=' + uri_param1 + \
              '&marketplace_id=' + uri_param2 + \
              '&format=' + uri_param3 + \
              '&limit=' + uri_param4 + \
              '&offer=' + uri_param5
    # Method Headers
    api_headers = get_api_headers(token)
    # Call the API Endpoint
    api_response = bll.dal.ebay_api.getOffers(api_url, api_headers)
    # Return the API Response
    return api_response

# inventory_getListingFees request body uses /api_calls/offerGetListingFees.json
def inventory_getListingFees(token, uri_env, body):
    """Get the Inventory Offer Listing Fees"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/inventory/v1/offer/get_listing_fees/'
    # Method Headers
    api_headers = get_api_headers(token)
    # Call the API Endpoint
    api_response = bll.dal.ebay_api.getOffer(api_url, body, api_headers)
    # Return the API Response
    return api_response


# inventory_publishOfferByInventoryItemGroup request body uses /api_calls/offerPublishByInventoryItemGroup.json
def inventory_publishOfferByInventoryItemGroup(token, uri_env, body):
    """Publish the Offer by the Inventory Item Group"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/inventory/v1/offer/publish_by_inventory_item_group'
    # Method Headers
    api_headers = get_api_headers(token)
    # Call the API Endpoint
    api_response = bll.dal.ebay_api.publishOfferByInventoryItemGroup(api_url, body, api_headers)
    # Return the API Response
    return api_response

# inventory_publishOfferByInventoryItemGroup request body uses /api_calls/offerPublishByInventoryItemGroup.json
def inventory_withdrawOfferByInventoryItemGroup(token, uri_env, body):
    """Withdraw the Offer by the Inventory Item Group"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/inventory/v1/offer/withdraw_by_inventory_item_group'
    # Method Headers
    api_headers = get_api_headers(token)
    # Call the API Endpoint
    api_response = bll.dal.ebay_api.withdrawOfferByInventoryItemGroup(api_url, body, api_headers)
    # Return the API Response
    return api_response

# inventory_bulkCreateOffer request body uses /api_calls/bulkCreateOffer.json
def inventory_bulkCreateOffer(token, uri_env, body):
    """Bulk Create Inventory Item Offers"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/inventory/v1/bulk_create_offer/'
    # Method Headers
    api_headers = get_api_headers(token)
    # Specify request body json data and headers
    api_response = bll.dal.ebay_api.bulkCreateOffer(api_url, body, api_headers)
    # Return the API Response
    return api_response

# inventory_bulkCreateOffer request body uses /api_calls/bulkPublishOffer.json
def inventory_bulkPublishOffer(token, uri_env, body):
    """Publish Inventory Item Offers in Bulk"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/inventory/v1/bulk_publish_offer/'
    # Method Headers
    api_headers = get_api_headers(token)
    # Specify request body json data and headers
    api_response = bll.dal.ebay_api.bulkPublishOffer(api_url, body, api_headers)
    # Return the API Response
    return api_response
""" <><><><><><><><><> END Offer Object <><><><><><><><><><><> """

""" <><><><><><><><><> BEGIN Inventory Item Group Object <><><><><><><><><><><> """

# uri_param1 ~~ {inventoryItemGroupKey}
def inventory_getInventoryItemGroup(token, uri_env, uri_param1):
    """Get the Inventory Item Group"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/inventory/v1/inventory_item_group/' + str(uri_param1) + '/'
    # Method Headers
    api_headers = get_api_headers(token)
    # Call the API Endpoint
    api_response = bll.dal.ebay_api.getInventoryItemGroup(api_url, api_headers)
    # Return the API Response
    return api_response

# uri_param1 ~~ {inventoryItemGroupKey}
def inventory_createOrReplaceInventoryItemGroup(token, uri_env, uri_param1, body):
    """Create or Update the Inventory Item Group"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/inventory/v1/inventory_item_group/' + str(uri_param1) + '/'
    # Method Headers
    api_headers = get_api_headers(token)
    # Call the API Endpoint
    api_response = bll.dal.ebay_api.createOrReplaceInventoryItemGroup(api_url, body, api_headers)
    # Return the API Response
    return api_response

# uri_param1 ~~ {inventoryItemGroupKey}
def inventory_deleteInventoryItemGroup(token, uri_env, uri_param1):
    """Delete the Inventory Item Group"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/inventory/v1/inventory_item_group/' + str(uri_param1) + '/'
    # Method Headers
    api_headers = get_api_headers(token)
    # Call the API Endpoint
    api_response = bll.dal.ebay_api.deleteInventoryItemGroup(api_url, api_headers)
    # Return the API Response
    return api_response

""" <><><><><><><><><> END Inventory Item Group Object <><><><><><><><><><><> """