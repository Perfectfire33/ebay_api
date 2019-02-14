import ebay_api





def inventory_createOrReplaceInventoryItem(body, token, sku):

    """Create the Test Case"""

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


    """Store the addTestCase response"""

    """Create the Test Case"""

    # Use the .json function() to get the data in json format and then we store it in api_response variable
    # api_response = api_response.json()
    return api_response