import ebay_api_connector

operationId = "createOrReplaceInventoryItem"

found_api = ebay_api_connector.api_finder(operationId)

print(found_api)