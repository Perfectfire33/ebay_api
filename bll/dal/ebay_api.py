import requests
import simplejson as json

"""
EBAY_API.PY ~ CALL EBAY API 
WITH REQUESTS LIBRARY 
AND RETRIEVE RESPONSE
"""

""" COMMERCE TAXONOMY API API ~ POLICY OBJECTS """

def getCategorySuggestions(url, headers):
    # Send the request with parameters and store it in response
    response = requests.get(url, headers=headers)
    return response

def getDefaultCategoryTreeId(url, headers):
    # Send the request with parameters and store it in response
    response = requests.get(url, headers=headers)
    return response


""" ACCOUNT API ~ POLICY OBJECTS """
def createFulfillmentPolicy(url, body, headers):
    # Send the request with parameters and store it in response
    response = requests.post(url, data=body, headers=headers)
    return response

def deleteFulfillmentPolicy(url, headers):
    # Send the request with parameters and store it in response
    response = requests.delete(url, headers=headers)
    return response

def getFulfillmentPolicies(url, headers):
    # Send the request with parameters and store it in response
    response = requests.get(url, headers=headers)
    return response

def getFulfillmentPolicy(url, headers):
    # Send the request with parameters and store it in response
    response = requests.get(url, headers=headers)
    return response

def getFulfillmentPolicyByName(url, headers):
    # Send the request with parameters and store it in response
    response = requests.get(url, headers=headers)
    return response

def updateFulfillmentPolicy(url, body, headers):
    # Send the request with parameters and store it in response
    response = requests.put(url, data=body, headers=headers)
    return response



def createPaymentPolicy(url, body, headers):
    # Send the request with parameters and store it in response
    response = requests.post(url, data=body, headers=headers)
    return response

def deletePaymentPolicy(url, headers):
    # Send the request with parameters and store it in response
    response = requests.delete(url, headers=headers)
    return response

def getPaymentPolicies(url, headers):
    # Send the request with parameters and store it in response
    response = requests.get(url, headers=headers)
    return response

def getPaymentPolicy(url, headers):
    # Send the request with parameters and store it in response
    response = requests.get(url, headers=headers)
    return response

def getPaymentPolicyByName(url, headers):
    # Send the request with parameters and store it in response
    response = requests.get(url, headers=headers)
    return response

def updatePaymentPolicy(url, body, headers):
    # Send the request with parameters and store it in response
    response = requests.put(url, data=body, headers=headers)
    return response




def createReturnPolicy(url, body, headers):
    # Send the request with parameters and store it in response
    response = requests.post(url, data=body, headers=headers)
    return response

def deleteReturnPolicy(url, headers):
    # Send the request with parameters and store it in response
    response = requests.delete(url, headers=headers)
    return response

def getReturnPolicies(url, headers):
    # Send the request with parameters and store it in response
    response = requests.get(url, headers=headers)
    return response

def getReturnPolicy(url, headers):
    # Send the request with parameters and store it in response
    response = requests.get(url, headers=headers)
    return response

def getReturnPolicyByName(url, headers):
    # Send the request with parameters and store it in response
    response = requests.get(url, headers=headers)
    return response

def updateReturnPolicy(url, body, headers):
    # Send the request with parameters and store it in response
    response = requests.put(url, data=body, headers=headers)
    return response









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

def bulkCreateOffer(url, body, headers):
    # Send the request with parameters and store it in response
    response = requests.post(url, data=body, headers=headers)
    return response

def bulkPublishOffer(url, body, headers):
    # Send the request with parameters and store it in response
    response = requests.post(url, data=body, headers=headers)
    return response







