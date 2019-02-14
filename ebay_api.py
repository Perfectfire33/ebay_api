import requests
import simplejson as json





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

def createInventoryLocation(url, body, headers):
    # Send the request with parameters and store it in response
    response = requests.post(url, data=json.dumps(body), headers=headers)
    return response

def deleteInventoryItem(url, headers):
    # Send the request with parameters and store it in response
    response = requests.delete(url, headers=headers)
    return response

def bulkUpdatePriceQuantity(url, body, headers):
    # Send the request with parameters and store it in response
    response = requests.post(url, data=json.dumps(body), headers=headers)
    return response

def bulkCreateOrReplaceInventoryItem(url, body, headers):
    # Send the request with parameters and store it in response
    response = requests.post(url, data=json.dumps(body), headers=headers)
    return response

def bulkGetInventoryItem(url, body, headers):
    # Send the request with parameters and store it in response
    response = requests.post(url, data=json.dumps(body), headers=headers)
    return response
