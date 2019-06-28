import ebay_api_connector
import simplejson as json
import api_contract_accessor

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
    api_response = ebay_api_connector.inventory_createOrReplaceInventoryItem(body, tokenPrepared, sku)

    code = api_response.status_code
    print("code")
    print(code)

    print("api_response")
    print(api_response)

    return api_response

# determine what inventory type this object will be
# object_type - one of the items in the object list:
    #     inventory_item
    #     location
    #     offer
    #     inventory_item_group
def determineInventoryObject(object_type):
    print("determineInventoryObject")
    print("determine what inventory type this object will be")

    if object_type == "inventory_item":
        print("object_type == inventory_item")

    if object_type == "inventory_item":
        print("object_type == inventory_item")

    if object_type == "inventory_item":
        print("object_type == inventory_item")



