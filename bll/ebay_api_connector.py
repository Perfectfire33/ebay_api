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

def get_api_headers2(token):
    api_headers = {"Authorization": "%s" % token,
                   "Accept": "application/json",
                   "Content-Type": "application/json"
                   }

    return api_headers

#def get_api_headers(token):
#    api_headers = {'Authorization': '%s' % token,
#                   'content-language': 'en-US'}
#
#    return api_headers

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


def mapPayloadBodyToFilename():
    print("aaa")


def getPayloadFilenameMap():
    payloadFilenameMap = {}

    payloadFilenameMap['inventory_createOrReplaceInventoryItem']="createOrReplaceInventoryItem.json"
    payloadFilenameMap['inventory_bulkUpdatePriceQuantity']="bulkUpdatePriceQuantity.json"
    payloadFilenameMap['inventory_bulkCreateOrReplaceInventoryItem']="bulkCreateOrReplaceInventoryItem.json"
    payloadFilenameMap['inventory_createInventoryLocation']="createInventoryLocation.json"
    payloadFilenameMap['inventory_createOffer']="createOffer.json"
    payloadFilenameMap['inventory_updateOffer']="createOffer.json"
    payloadFilenameMap['inventory_getListingFees']="offerGetListingFees.json"
    payloadFilenameMap['inventory_publishOfferByInventoryItemGroup']="offerPublishByInventoryItemGroup.json"
    payloadFilenameMap['inventory_withdrawOfferByInventoryItemGroup']="offerWithdrawByInventoryItemGroup.json"
    payloadFilenameMap['inventory_bulkCreateOffer']="bulkCreateOffer.json"
    payloadFilenameMap['inventory_bulkPublishOffer']="bulkPublishOffer.json"
    payloadFilenameMap['account_createPaymentPolicy']="createPaymentPolicy.json"
    payloadFilenameMap['account_createReturnPolicy']="createReturnPolicy.json"
    payloadFilenameMap['account_createFulfillmentPolicy']="createFulfillmentPolicy.json"
    payloadFilenameMap['account_updatePaymentPolicy']="updatePaymentPolicy.json"
    payloadFilenameMap['account_updateReturnPolicy']="updateReturnPolicy.json"
    payloadFilenameMap['account_updateFulfillmentPolicy']="updateFulfillmentPolicy.json"

    return payloadFilenameMap


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
    api_response = bll.dal.ebay_api.createOrReplaceInventoryItem(api_url, body, api_headers)
    # Return the API Response
    return api_response

# uri_param1 ~~ {sku}
def inventory_getInventoryItem(token, uri_env, uri_param1):
    """Get an Inventory Item"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/inventory/v1/inventory_item/' + str(uri_param1)
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
    api_url = base_uri + '/sell/inventory/v1/inventory_item/' + '?limit=' + str(uri_param1) + '&offset=' + str(uri_param2)
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
    api_url = base_uri + '/sell/inventory/v1/location/' + '?offset=' + str(uri_param1) + '&limit=' + str(uri_param2)
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

# inventory_withdrawOfferByInventoryItemGroup request body uses /api_calls/offerWithdrawByInventoryItemGroup.json
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

# inventory_bulkPublishOffer request body uses /api_calls/bulkPublishOffer.json
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






""" <><><><><><><><><> BEGIN ACCOUNT API Object <><><><><><><><><><><> """

def account_createFulfillmentPolicy(token, uri_env, body):
    """Create the Fulfillment Policy"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/account/v1/fulfillment_policy/'
    # Method Headers
    api_headers = get_api_headers(token)
    # Call the API Endpoint
    api_response = bll.dal.ebay_api.createFulfillmentPolicy(api_url, body, api_headers)
    # Return the API Response
    return api_response

# uri_param1 ~~ {fulfillmentPolicyId}
def account_deleteFulfillmentPolicy(token, uri_env, uri_param1):
    """Delete the Fulfillment Policy"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/inventory/v1/fulfillment_policy/' + str(uri_param1) + '/'
    # Method Headers
    api_headers = get_api_headers(token)
    # Call the API Endpoint
    api_response = bll.dal.ebay_api.deleteFulfillmentPolicy(api_url, api_headers)
    # Return the API Response
    return api_response

# uri_param1 ~~ {marketplace_id}
def account_getFulfillmentPolicies(token, uri_env, uri_param1):
    """Get Fulfillment Policies"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/account/v1/fulfillment_policy/?marketplace_id=' + str(uri_param1)
    # Method Headers
    api_headers = get_api_headers(token)
    # Call the API Endpoint
    api_response = bll.dal.ebay_api.getFulfillmentPolicies(api_url, api_headers)
    # Return the API Response
    return api_response

# uri_param1 ~~ {fulfillmentPolicyId}
def account_getFulfillmentPolicy(token, uri_env, uri_param1):
    """Get the Fulfillment Policy"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/inventory/v1/fulfillment_policy/' + str(uri_param1) + '/'
    # Method Headers
    api_headers = get_api_headers(token)
    # Call the API Endpoint
    api_response = bll.dal.ebay_api.getFulfillmentPolicy(api_url, api_headers)
    # Return the API Response
    return api_response

# uri_param1 ~~ {marketplace_id}
# uri_param2 ~~ {name}
def account_getFulfillmentPolicyByName(token, uri_env, uri_param1, uri_param2):
    """Get Fulfillment Policy By Name"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/account/v1/fulfillment_policy/get_by_policy_name?marketplace_id=' + str(uri_param1) + '&name=' + str(uri_param2) + '/'
    # Method Headers
    api_headers = get_api_headers(token)
    # Call the API Endpoint
    api_response = bll.dal.ebay_api.getFulfillmentPolicyByName(api_url, api_headers)
    # Return the API Response
    return api_response

# uri_param1 ~~ {fulfillmentPolicyId}
def account_updateFulfillmentPolicy(token, uri_env, uri_param1, body):
    """Update the Fulfillment Policy"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/inventory/v1/fulfillment_policy/' + str(uri_param1) + '/'
    # Method Headers
    api_headers = get_api_headers(token)
    # Call the API Endpoint
    api_response = bll.dal.ebay_api.updateFulfillmentPolicy(api_url, body, api_headers)
    # Return the API Response
    return api_response


def account_createPaymentPolicy(token, uri_env, body):
    """Create the Payment Policy"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/account/v1/payment_policy/'
    # Method Headers
    api_headers = get_api_headers(token)
    # Call the API Endpoint
    api_response = bll.dal.ebay_api.createPaymentPolicy(api_url, body, api_headers)
    # Return the API Response
    return api_response

# uri_param1 ~~ {paymentPolicyId}
def account_deletePaymentPolicy(token, uri_env, uri_param1):
    """Delete the Payment Policy"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/inventory/v1/payment_policy/' + str(uri_param1) + '/'
    # Method Headers
    api_headers = get_api_headers(token)
    # Call the API Endpoint
    api_response = bll.dal.ebay_api.deletePaymentPolicy(api_url, api_headers)
    # Return the API Response
    return api_response

# uri_param1 ~~ {marketplace_id}
def account_getPaymentPolicies(token, uri_env, uri_param1):
    """Get Payment Policies"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/account/v1/payment_policy/?marketplace_id=' + str(uri_param1)
    # Method Headers
    api_headers = get_api_headers(token)
    # Call the API Endpoint
    api_response = bll.dal.ebay_api.getPaymentPolicies(api_url, api_headers)
    # Return the API Response
    return api_response

# uri_param1 ~~ {paymentPolicyId}
def account_getPaymentPolicy(token, uri_env, uri_param1):
    """Get the Payment Policy"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/inventory/v1/payment_policy/' + str(uri_param1) + '/'
    # Method Headers
    api_headers = get_api_headers(token)
    # Call the API Endpoint
    api_response = bll.dal.ebay_api.getPaymentPolicy(api_url, api_headers)
    # Return the API Response
    return api_response

# uri_param1 ~~ {marketplace_id}
# uri_param2 ~~ {name}
def account_getPaymentPolicyByName(token, uri_env, uri_param1, uri_param2):
    """Get Payment Policy By Name"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/account/v1/payment_policy/get_by_policy_name?marketplace_id=' + str(uri_param1) + '&name=' + str(uri_param2)
    # Method Headers
    api_headers = get_api_headers(token)
    # Call the API Endpoint
    api_response = bll.dal.ebay_api.getPaymentPolicyByName(api_url, api_headers)
    # Return the API Response
    return api_response

# uri_param1 ~~ {paymentPolicyId}
def account_updatePaymentPolicy(token, uri_env, uri_param1, body):
    """Update the Payment Policy"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/inventory/v1/payment_policy/' + str(uri_param1) + '/'
    # Method Headers
    api_headers = get_api_headers(token)
    # Call the API Endpoint
    api_response = bll.dal.ebay_api.updatePaymentPolicy(api_url, body, api_headers)
    # Return the API Response
    return api_response



def account_createReturnPolicy(token, uri_env, body):
    """Create the Return Policy"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/account/v1/return_policy/'
    # Method Headers
    api_headers = get_api_headers(token)
    # Call the API Endpoint
    api_response = bll.dal.ebay_api.createReturnPolicy(api_url, body, api_headers)
    # Return the API Response
    return api_response

# uri_param1 ~~ {returnPolicyId}
def account_deleteReturnPolicy(token, uri_env, uri_param1):
    """Delete the Return Policy"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/inventory/v1/return_policy/' + str(uri_param1) + '/'
    # Method Headers
    api_headers = get_api_headers(token)
    # Call the API Endpoint
    api_response = bll.dal.ebay_api.deleteReturnPolicy(api_url, api_headers)
    # Return the API Response
    return api_response

# uri_param1 ~~ {marketplace_id}
def account_getReturnPolicies(token, uri_env, uri_param1):
    """Get Return Policies"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/account/v1/return_policy/?marketplace_id=' + str(uri_param1)
    # Method Headers
    api_headers = get_api_headers(token)
    # Call the API Endpoint
    api_response = bll.dal.ebay_api.getReturnPolicies(api_url, api_headers)
    # Return the API Response
    return api_response

# uri_param1 ~~ {returnPolicyId}
def account_getReturnPolicy(token, uri_env, uri_param1):
    """Get the Return Policy"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/inventory/v1/return_policy/' + str(uri_param1) + '/'
    # Method Headers
    api_headers = get_api_headers(token)
    # Call the API Endpoint
    api_response = bll.dal.ebay_api.getReturnPolicy(api_url, api_headers)
    # Return the API Response
    return api_response

# uri_param1 ~~ {marketplace_id}
# uri_param2 ~~ {name}
def account_getReturnPolicyByName(token, uri_env, uri_param1, uri_param2):
    """Get Return Policy By Name"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/account/v1/return_policy/get_by_policy_name?marketplace_id=' + str(uri_param1) + '&name=' + str(uri_param2) + '/'
    # Method Headers
    api_headers = get_api_headers(token)
    # Call the API Endpoint
    api_response = bll.dal.ebay_api.getReturnPolicyByName(api_url, api_headers)
    # Return the API Response
    return api_response

# uri_param1 ~~ {returnPolicyId}
def account_updateReturnPolicy(token, uri_env, uri_param1, body):
    """Update the Return Policy"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/sell/inventory/v1/return_policy/' + str(uri_param1) + '/'
    # Method Headers
    api_headers = get_api_headers(token)
    # Call the API Endpoint
    api_response = bll.dal.ebay_api.updateReturnPolicy(api_url, body, api_headers)
    # Return the API Response
    return api_response

""" <><><><><><><><><> END ACCOUNT API Object <><><><><><><><><><><> """

""" <><><><><><><><><> BEGIN COMMERCE API Object <><><><><><><><><><><> """


# uri_param1 ~~ {category_tree_id}
# uri_param2 ~~ {q}
def taxonomy_getCategorySuggestions(token, uri_env, uri_param1, uri_param2):
    """Get Category Suggestions"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/commerce/taxonomy/v1_beta/category_tree/' + str(uri_param1) + '/get_category_suggestions?q=' + str(uri_param2)
    # Method Headers
    api_headers = get_api_headers(token)
    # Call the API Endpoint
    api_response = bll.dal.ebay_api.getCategorySuggestions(api_url, api_headers)
    # Return the API Response
    return api_response

# uri_param1 ~~ {marketplace_id}
def taxonomy_getDefaultCategoryTreeId(token, uri_env, uri_param1):
    """Get the Default Category Tree Id"""
    base_uri = getBaseUri(uri_env)
    # This is the ebay URL used to get an inventory item
    api_url = base_uri + '/commerce/taxonomy/v1_beta/get_default_category_tree_id?marketplace_id=' + str(uri_param1)
    # Method Headers
    api_headers = get_api_headers(token)
    # Call the API Endpoint
    api_response = bll.dal.ebay_api.getDefaultCategoryTreeId(api_url, api_headers)
    # Return the API Response
    return api_response
""" <><><><><><><><><> END COMMERCE API Object <><><><><><><><><><><> """


