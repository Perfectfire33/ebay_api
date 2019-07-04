import requests
import simplejson as json

"""
EBAY_API.PY ~ CALL EBAY API 
WITH REQUESTS LIBRARY 
AND RETRIEVE RESPONSE
"""


""" INVENTORY ITEM OBJECT """

def getInventoryItem(url, headers):
    # Send the request with parameters and store it in response
    response = requests.get(url, headers=headers)
    return response

def getInventoryItems(url, headers):
    # Send the request with parameters and store it in response
    response = requests.get(url, headers=headers)
    return response


def createOrReplaceInventoryItem(url, body, headers):
    # Send the request with parameters and store it in response
    response = requests.put(url, data=body, headers=headers)
    return response

def deleteInventoryItem(url, headers):
    # Send the request with parameters and store it in response
    response = requests.delete(url, headers=headers)
    return response

def bulkUpdatePriceQuantity(url, body, headers):
    # Send the request with parameters and store it in response
    response = requests.post(url, data=body, headers=headers)
    return response

def bulkCreateOrReplaceInventoryItem(url, body, headers):
    # Send the request with parameters and store it in response
    response = requests.post(url, data=body, headers=headers)
    return response

def bulkGetInventoryItem(url, headers):
    # Send the request with parameters and store it in response
    response = requests.post(url, headers=headers)
    return response

""" INVENTORY LOCATION OBJECT """

def getInventoryLocation(url, headers):
    # Send the request with parameters and store it in response
    response = requests.get(url, headers=headers)
    return response

def getInventoryLocations(url, headers):
    # Send the request with parameters and store it in response
    response = requests.get(url, headers=headers)
    return response

def createInventoryLocation(url, body, headers):
    # Send the request with parameters and store it in response
    response = requests.post(url, data=body, headers=headers)
    return response

def disableInventoryLocation(url, headers):
    # Send the request with parameters and store it in response
    response = requests.post(url, headers=headers)
    return response

def enableInventoryLocation(url, headers):
    # Send the request with parameters and store it in response
    response = requests.post(url, headers=headers)
    return response

def deleteInventoryLocation(url, headers):
    # Send the request with parameters and store it in response
    response = requests.delete(url, headers=headers)
    return response

def updateInventoryLocation(url, body, headers):
    # Send the request with parameters and store it in response
    response = requests.post(url, data=body, headers=headers)
    return response

""" INVENTORY ITEM GROUP """

def getInventoryItemGroup(url, headers):
    # Send the request with parameters and store it in response
    response = requests.get(url, headers=headers)
    return response

def createOrReplaceInventoryItemGroup(url, body, headers):
    # Send the request with parameters and store it in response
    response = requests.put(url, data=body, headers=headers)
    return response

def deleteInventoryItemGroup(url, headers):
    # Send the request with parameters and store it in response
    response = requests.delete(url, headers=headers)
    return response


""" OFFER OBJECT """

def getOffer(url, headers):
    # Send the request with parameters and store it in response
    response = requests.get(url, headers=headers)
    return response

def createOffer(url, body, headers):
    # Send the request with parameters and store it in response
    response = requests.post(url, data=body, headers=headers)
    return response

def deleteOffer(url, headers):
    # Send the request with parameters and store it in response
    response = requests.delete(url, headers=headers)
    return response

def updateOffer(url, body, headers):
    # Send the request with parameters and store it in response
    response = requests.put(url, data=body, headers=headers)
    return response

def publishOffer(url, headers):
    # Send the request with parameters and store it in response
    response = requests.post(url, headers=headers)
    return response

def withdrawOffer(url, headers):
    # Send the request with parameters and store it in response
    response = requests.post(url, headers=headers)
    return response

def getListingFees(url, headers):
    # Send the request with parameters and store it in response
    response = requests.post(url, headers=headers)
    return response

def getOffers(url, headers):
    # Send the request with parameters and store it in response
    response = requests.get(url, headers=headers)
    return response

def publishOfferByInventoryItemGroup(url, body, headers):
    # Send the request with parameters and store it in response
    response = requests.post(url, data=body, headers=headers)
    return response

def withdrawOfferByInventoryItemGroup(url, body, headers):
    # Send the request with parameters and store it in response
    response = requests.post(url, data=body, headers=headers)
    return response

# NOT MVP
def bulkCreateOffer(url, body, headers):
    # Send the request with parameters and store it in response
    response = requests.post(url, data=body, headers=headers)
    return response

def bulkPublishOffer(url, headers):
    # Send the request with parameters and store it in response
    response = requests.post(url, headers=headers)
    return response







