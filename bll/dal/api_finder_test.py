import bll.ebay_api_connector

operationId = "createOrReplaceInventoryItem"

found_api = bll.ebay_api_connector.api_finder(operationId)

print(found_api)