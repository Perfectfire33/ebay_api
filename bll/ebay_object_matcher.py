import bll.dal.api_local_file_accessor
import bll.ebay_object_receiver
import json
import bll.ebay_api_connector
import time

# this file matches ebay data to ebay objects
# sends objects out to api_call_sequencer file

# call_ebay_api gets api data, finds the appropriate api call set based on "script runtime" config area
# and will apply the "script runtime" to each row in the selected Google Sheet Area
# and will return an api response
def getScriptExecutionList(configDataSet):
    # Get data from "Script Runtime" Area
    scriptRuntimeData = []
    scriptRuntimeData.append(configDataSet[1][0][1])
    scriptRuntimeData.append(configDataSet[1][1][1])
    scriptRuntimeData.append(configDataSet[1][2][1])
    scriptRuntimeData.append(configDataSet[1][3][1])
    #print("scriptRuntimeData")
    #print(scriptRuntimeData)
    i = 0
    scriptExecuteList = []
    while i < scriptRuntimeData.__len__():
        if scriptRuntimeData[i] == "1":
            #print("Row = 1")
            scriptExecuteList.append(configDataSet[1][i][0])
        i = i + 1
    return scriptExecuteList




# get number of items in inventory from loadJsonData() and operation list from "Script Runtime"
#   (take data from each item and put into a request body)
# getObjectCount retrieves what operations and the number of operation executions
#   based on number of keys in the json variable in appDataSet , and
#   based on the Script Name where Property Value equals 1 in ebay-config-data from configDataSet
def getObjectCount(configDataSet, appDataSet, headers):
    #print("begin getObjectCount")
    # Import JSON header-data matched object
    wjson = bll.ebay_object_receiver.loadJsonData(appDataSet, headers)
    # Get list of object types to count
    script_execute_list = bll.ebay_object_matcher.getScriptExecutionList(configDataSet)
    #print("script_execute_list")
    #print(script_execute_list.__len__())
    # select statement on what scripts are flagged for execution
    i = 0
    objectCountAccumulator = []
    objectScriptTypeAccumulator = []
    while i < script_execute_list.__len__():
        if script_execute_list[i] == "create_item_inventory":
            #print("create_item_inventory")
            counter = 0
            #print("len(wjson)")
            #print(len(wjson))
            #print("range(len(wjson))")
            #print(range(len(wjson)))
            #print("begin for loop")
            #for each row in inventory, make an api request payload with the data
            for object in range(len(wjson[0])):
                #print("object" + str(j))
                #print(object)
                #print("wjson[0][0]")
                #print(wjson[0][1])
                #print("wjson[area0][counter]['item_id']")
                #print(wjson[0][counter]['item_id'])
                counter = counter + 1
            objectCountAccumulator.append(counter)
            objectScriptTypeAccumulator.append(script_execute_list[i])

        if script_execute_list[i] == "create_item_inventory_location":
            #print("create_item_inventory_location")
            counter = 0
            #this for loop in range(len(wjson[0])) might have to be different for inventory location
            #   if data is grabbed from different area of sheet
            for object in range(len(wjson[0])):
                counter = counter + 1
            objectCountAccumulator.append(counter)
            objectScriptTypeAccumulator.append(script_execute_list[i])

        if script_execute_list[i] == "create_item_offer":
            #print("create_item_offer")
            counter = 0
            for object in range(len(wjson[0])):
                counter = counter + 1
            objectCountAccumulator.append(counter)
            objectScriptTypeAccumulator.append(script_execute_list[i])

        if script_execute_list[i] == "publish_offer":
            #print("publish_offer")
            counter = 0
            for object in range(len(wjson[0])):
                counter = counter + 1
            objectCountAccumulator.append(counter)
            objectScriptTypeAccumulator.append(script_execute_list[i])
        i = i + 1
    objectCount = []
    objectCount.append(objectCountAccumulator)
    objectCount.append(objectScriptTypeAccumulator)
    return objectCount

def get_headers_data_i():
    # need to define object headers
    headers = []
    headers.append('item_id')
    headers.append('item_title')
    headers.append('item_condition')
    headers.append('item_condition_description')
    headers.append('item_price')
    headers.append('item_qty')
    headers.append('ship_policy')
    headers.append('packed_item_weight_lb')
    headers.append('packed_item_weight_oz')
    headers.append('packed_item_height')
    headers.append('packed_item_length')
    headers.append('packed_item_depth')
    headers.append('payment_policy')
    headers.append('return_policy')

    return headers


def get_headers_data_ii():
    headers2 = []
    headers2.append('item_id')
    headers2.append('box_name')
    headers2.append('box_category')
    headers2.append('unit_price')
    headers2.append('inv_qty')
    headers2.append('total_value')
    headers2.append('box_packing_weight_lb')
    headers2.append('box_packing_weight_oz')
    headers2.append('unit_weight_lb')
    headers2.append('unit_weight_oz')
    headers2.append('qty_weight_lb')
    headers2.append('qty_weight_oz')
    headers2.append('location')
    headers2.append('section')
    headers2.append('box_height')
    headers2.append('box_length')
    headers2.append('box_depth')
    headers2.append('box_type')
    headers2.append('box_style')
    headers2.append('box_details')
    headers2.append('pic_local_uri')
    headers2.append('pic_internet_uri')

    return headers2

def get_headers_data_iii():
    headers3 = []
    headers3.append('addressLine1')
    headers3.append('addressLine2')
    headers3.append('city')
    headers3.append('country')
    headers3.append('county')
    headers3.append('postalCode')
    headers3.append('stateOrProvince')
    headers3.append('locationAdditionalInformation')
    headers3.append('locationInstructions')
    headers3.append('locationTypes')
    headers3.append('merchantLocationStatus')
    headers3.append('name')

    return headers3

def get_all_inventory_items(configDataSet, uri_env):
    api_array = []
    # Set filepath token for ebay api access
    filepath_token = configDataSet[0][2][2] + configDataSet[0][2][1]
    # uri_param1 ~ limit
    uri_param1 = 25
    # uri_param2 ~ offset
    uri_param2 = 0
    # open token file
    token_file = open(filepath_token).read()
    # eBay API requires Bearer token
    tokenPrepared = "Bearer " + token_file
    api_response = bll.ebay_api_connector.inventory_getInventoryItems(tokenPrepared, uri_env, uri_param1, uri_param2)
    api_array.append(api_response)
    api_array.append(api_response.text)
    api_array.append(api_response.status_code)
    return api_array


def get_all_inventory_locations(configDataSet, uri_env):
    api_array = []
    # Set filepath token for ebay api access
    filepath_token = configDataSet[0][2][2] + configDataSet[0][2][1]
    # uri_param1 ~ offset
    uri_param1 = 0
    # uri_param2 ~ limit
    uri_param2 = 25
    # open token file
    token_file = open(filepath_token).read()
    # eBay API requires Bearer token
    tokenPrepared = "Bearer " + token_file
    api_response = bll.ebay_api_connector.inventory_getInventoryLocations(tokenPrepared, uri_env, uri_param1, uri_param2)
    api_array.append(api_response)
    api_array.append(api_response.text)
    api_array.append(api_response.status_code)
    return api_array

def create_inventory_location(configDataSet, appDataSet3, uri_env):
    headers3 = get_headers_data_iii()
    # Import JSON header-data matched object
    print("appDataSet3")
    print(appDataSet3)
    xjson = bll.ebay_object_receiver.loadJsonData(appDataSet3, headers3)
    print("XJSON")
    print(xjson)
    # Set filepath token for ebay api access
    filepath_token = configDataSet[0][2][2] + configDataSet[0][2][1]
    # This is the file that includes the api call data
    filepath_body = configDataSet[0][6][2] + configDataSet[0][6][1]
    # This is the folder of the json request payload files
    api_payload_folder = configDataSet[0][7][2]
    payloadFilenameMap = bll.ebay_api_connector.getPayloadFilenameMap()
    # open the right payload file with json data
    api_payload_filename = api_payload_folder + payloadFilenameMap['inventory_createInventoryLocation']
    api_payload_file = open(api_payload_filename, "r")
    # replace values in json_payload_body with data from wjson variable
    json_payload_body = json.load(api_payload_file)
    time.sleep(0.25)
    api_payload_file.close()
    api_array = []
    body_var1 = xjson[0][0]['addressLine1']
    body_var2 = xjson[0][0]['addressLine2']
    body_var3 = xjson[0][0]['city']
    body_var4 = xjson[0][0]['country']
    body_var5 = xjson[0][0]['county']
    body_var6 = xjson[0][0]['postalCode']
    body_var7 = xjson[0][0]['stateOrProvince']
    body_var8 = xjson[0][0]['locationAdditionalInformation']
    body_var9 = xjson[0][0]['locationInstructions']
    body_var10 = xjson[0][0]['locationTypes']
    body_var11 = xjson[0][0]['merchantLocationStatus']
    body_var12 = xjson[0][0]['name']
    json_payload_body['location']['address']['addressLine1'] = body_var1
    json_payload_body['location']['address']['addressLine2'] = body_var2
    json_payload_body['location']['address']['city'] = body_var3
    json_payload_body['location']['address']['country'] = body_var4
    json_payload_body['location']['address']['county'] = body_var5
    json_payload_body['location']['address']['postalCode'] = body_var6
    json_payload_body['location']['address']['stateOrProvince'] = body_var7
    json_payload_body['locationAdditionalInformation'] = body_var8
    json_payload_body['locationInstructions'] = body_var9
    json_payload_body['locationTypes'][0] = body_var10
    json_payload_body['merchantLocationStatus'] = body_var11
    json_payload_body['name'] = body_var12

    print("json_payload_body")
    print(json_payload_body)

    # merchantLocationKey is the name field in "ebay_item_inventory"."inventory_locations".Cell(C15)
    uri_param1 = body_var12
    # open token file
    token_file = open(filepath_token).read()
    # eBay API requires Bearer token
    tokenPrepared = "Bearer " + token_file
    # read destination file
    # Get JSON body of inventory item from local file (put this on google sheet, get with gsheet api?)
    body_string = str(json_payload_body)
    body = body_string.replace("\'", "\"")
    time.sleep(0.25)
    api_response = bll.ebay_api_connector.inventory_createInventoryLocation(tokenPrepared, uri_env, uri_param1, body)
    api_array.append(api_response)
    api_array.append(api_response.text)
    api_array.append(api_response.status_code)
    #from here, can also send misc data to flask API to create webpage or store data in SQLite DB
    time.sleep(1)
    #print("API_ARRAY")
    #print(api_array)
    return api_array



def create_item_inventory(configDataSet, appDataSet, appDataSet2, uri_env):
    headers = get_headers_data_i()
    headers2 = get_headers_data_ii()

    # for each row in inventory, make an api request payload with the data
    object_count = bll.ebay_object_matcher.getObjectCount(configDataSet, appDataSet, headers)
    #print("object_count")
    #print(object_count)
    # Import JSON header-data matched object
    wjson = bll.ebay_object_receiver.loadJsonData(appDataSet, headers)
    vjson = bll.ebay_object_receiver.loadJsonData(appDataSet2, headers2)
    print("VJSON")
    print(vjson)
    # Set filepath token for ebay api access
    filepath_token = configDataSet[0][2][2] + configDataSet[0][2][1]
    # This is the file that includes the api call data
    filepath_body = configDataSet[0][6][2] + configDataSet[0][6][1]
    # This is the folder of the json request payload files
    api_payload_folder = configDataSet[0][7][2]
    payloadFilenameMap = bll.ebay_api_connector.getPayloadFilenameMap()

    # open the right payload file with json data
    api_payload_filename = api_payload_folder + payloadFilenameMap['inventory_createOrReplaceInventoryItem']
    api_payload_file = open(api_payload_filename, "r")
    # replace values in json_payload_body with data from wjson variable
    json_payload_body = json.load(api_payload_file)
    time.sleep(0.25)
    api_payload_file.close()
    k = 0
    #array for the api calls in the batch
    api_array = []
    while k < object_count[0][0]:
        body_var1 = wjson[0][k]['item_title']
        body_var2 = wjson[1][k]['item_condition']
        body_var3 = wjson[1][k]['item_condition_description']
        body_var4 = wjson[1][k]['item_qty']
        body_var6a = wjson[2][k]['packed_item_weight_lb']
        body_var6b = wjson[2][k]['packed_item_weight_oz']
        body_var7 = wjson[2][k]['packed_item_height']
        body_var8 = wjson[2][k]['packed_item_length']
        body_var9 = wjson[2][k]['packed_item_depth']
        json_payload_body['product']['title'] = body_var1
        json_payload_body['condition'] = body_var2
        json_payload_body['conditionDescription'] = body_var3
        json_payload_body['availability']['shipToLocationAvailability']['quantity'] = body_var4
        # convert weight to single unit
        body_var6a = body_var6a * 16
        body_var6b = body_var6a + body_var6b
        # json_payload_body['packageWeightAndSize']['packageType'] = body_var5
        json_payload_body['packageWeightAndSize']['weight']['value'] = body_var6b
        json_payload_body['packageWeightAndSize']['dimensions']['height'] = body_var7
        json_payload_body['packageWeightAndSize']['dimensions']['length'] = body_var8
        json_payload_body['packageWeightAndSize']['dimensions']['width'] = body_var9

        # assign second google sheet profile (vjson) (sheet2) in the inventory and grab sku
        # for now, set item_id to sku
        uri_param1 = wjson[0][k]['item_id']
        # open token file
        token_file = open(filepath_token).read()
        # eBay API requires Bearer token
        tokenPrepared = "Bearer " + token_file
        # read destination file
        # Get JSON body of inventory item from local file (put this on google sheet, get with gsheet api?)
        body_string = str(json_payload_body)
        body = body_string.replace("\'", "\"")
        time.sleep(0.25)
        api_response = bll.ebay_api_connector.inventory_createOrReplaceInventoryItem(tokenPrepared, uri_env, uri_param1,
                                                                                     body)
        api_array.append(api_response)
        api_array.append(api_response.text)
        api_array.append(api_response.status_code)
        #from here, can also send misc data to flask API to create webpage or store data in SQLite DB
        time.sleep(3)
        k = k + 1

    #print("API_ARRAY")
    #print(api_array)
    return api_array



def create_item_offer(configDataSet, appDataSet, appDataSet2, uri_env):
    headers = get_headers_data_i()
    headers2 = get_headers_data_ii()
    # for each row in inventory, make an api request payload with the data
    object_count = bll.ebay_object_matcher.getObjectCount(configDataSet, appDataSet, headers)
    #print("object_count")
    #print(object_count)
    # Import JSON header-data matched object
    wjson = bll.ebay_object_receiver.loadJsonData(appDataSet, headers)
    vjson = bll.ebay_object_receiver.loadJsonData(appDataSet2, headers2)
    print("VJSON")
    print(vjson)
    # Set filepath token for ebay api access
    filepath_token = configDataSet[0][2][2] + configDataSet[0][2][1]
    # This is the file that includes the api call data
    filepath_body = configDataSet[0][6][2] + configDataSet[0][6][1]
    # This is the folder of the json request payload files
    api_payload_folder = configDataSet[0][7][2]
    payloadFilenameMap = bll.ebay_api_connector.getPayloadFilenameMap()

    # open the right payload file with json data
    api_payload_filename = api_payload_folder + payloadFilenameMap['inventory_createOffer']
    api_payload_file = open(api_payload_filename, "r")
    # replace values in json_payload_body with data from wjson variable
    json_payload_body = json.load(api_payload_file)
    api_payload_file.close()
    k = 0
    #array for the api calls in the batch
    api_array = []
    while k < object_count[0][0]:
        # paymentPolicyId from other API
        body_var1a = wjson[1][k]['ship_policy']
        #body_var1 = bll.ebay_object_matcher.getShipPolicyIdBasedOnInventory(body_var1a)
        body_var1 = ""
        # returnPolicyId from other API
        body_var2a = wjson[1][k]['payment_policy']
        #body_var2 = bll.ebay_object_matcher.getShipPolicyIdBasedOnInventory(body_var2a)
        body_var2 = ""
        # fulfillmentPolicyId from other API
        body_var3a = wjson[1][k]['return_policy']
        #body_var3 = bll.ebay_object_matcher.getShipPolicyIdBasedOnInventory(body_var3a)
        body_var3 = ""
        # availableQuantity
        body_var4 = wjson[1][k]['item_qty']
        # categoryId from category API
        body_var5a = wjson[1][k]['item_category']
        body_var5b = vjson[0][k]['box_category']
        # body_var5 = bll.ebay_object_matcher.getCategoryIdBasedOnInventory(body_var5a, body_var5b)
        body_var5 = ""
        # merchantLocationKey
        body_var6a = vjson[0][k]['location']
        body_var6b = vjson[0][k]['section']
        body_var6 = body_var6a + "_" + body_var6b
        body_var7 = vjson[0][k]['item_price']
        body_var8 = "EBAY_US"
        body_var9 = "FIXED_PRICE"
        body_var10 = vjson[0][k]['box_name']


        json_payload_body['listingPolicies']['paymentPolicyId'] = body_var1
        json_payload_body['listingPolicies']['returnPolicyId'] = body_var2
        json_payload_body['listingPolicies']['fulfillmentPolicyId'] = body_var3
        json_payload_body['listingPolicies']['ebayPlusIfEligible'] = "false"
        json_payload_body['availableQuantity'] = body_var4
        # derive this from "stage3"."Item Category"
        json_payload_body['categoryId'] = body_var5
        # derive this from "stage2"."location"."Section"
        json_payload_body['merchantLocationKey'] = body_var6
        json_payload_body['pricingSummary']['price']['value'] = body_var7
        json_payload_body['pricingSummary']['price']['currency'] = "USD"
        json_payload_body['marketplaceId'] = body_var8
        json_payload_body['format'] = body_var9
        json_payload_body['sku'] = body_var10

        # assign second google sheet profile (vjson) (sheet2) in the inventory and grab sku
        # for now, set item_id to sku
        uri_param1 = wjson[0][k]['item_id']
        # open token file
        token_file = open(filepath_token).read()
        # eBay API requires Bearer token
        tokenPrepared = "Bearer " + token_file
        # read destination file
        # Get JSON body of inventory item from local file (put this on google sheet, get with gsheet api?)
        body_string = str(json_payload_body)
        body = body_string.replace("\'", "\"")
        time.sleep(0.25)
        api_response = bll.ebay_api_connector.inventory_createOrReplaceInventoryItem(tokenPrepared, uri_env, uri_param1,
                                                                                     body)
        api_array.append(api_response)
        api_array.append(api_response.text)
        api_array.append(api_response.status_code)
        # from here, can also send misc data to flask API to create webpage or store data in SQLite DB
        time.sleep(3)
        k = k + 1

    #print("API_ARRAY")
    #print(api_array)
    return api_array







def call_ebay_api(configDataSet, appDataSet, uri_env):
    # need to define object headers
    headers = []
    headers.append('item_id')
    headers.append('item_title')
    headers.append('item_condition')
    headers.append('item_condition_description')
    headers.append('item_price')
    headers.append('item_qty')
    headers.append('ship_policy')
    headers.append('packed_item_weight_lb')
    headers.append('packed_item_weight_oz')
    headers.append('packed_item_height')
    headers.append('packed_item_length')
    headers.append('packed_item_depth')
    headers.append('payment_policy')
    headers.append('return_policy')

    # for each row in inventory, make an api request payload with the data
    object_count = bll.ebay_object_matcher.getObjectCount(configDataSet, appDataSet, headers)
    #print("object_count")
    #print(object_count)
    # Import JSON header-data matched object
    wjson = bll.ebay_object_receiver.loadJsonData(appDataSet, headers)
    # Set filepath token for ebay api access
    filepath_token = configDataSet[0][2][2] + configDataSet[0][2][1]
    # This is the file that includes the api call data
    filepath_body = configDataSet[0][6][2] + configDataSet[0][6][1]
    # This is the folder of the json request payload files
    api_payload_folder = configDataSet[0][7][2]
    payloadFilenameMap = bll.ebay_api_connector.getPayloadFilenameMap()
    """
    For each script:
        1| select each json payload and update it according to the endpoint
    """
    api_all_script_array = []
    for script in object_count[1]:
        #call new function
        #returns api_array


        #array of API call responses
        api_array = []





        if script == "create_item_inventory":
            # open the right payload file with json data
            api_payload_filename = api_payload_folder + payloadFilenameMap['inventory_createOrReplaceInventoryItem']
            api_payload_file = open(api_payload_filename, "r")
            # replace values in json_payload_body with data from wjson variable
            json_payload_body = json.load(api_payload_file)
            time.sleep(0.25)
            api_payload_file.close()
            k = 0
            while k < object_count[0][0]:
                body_var1 = wjson[0][k]['item_title']
                body_var2 = wjson[1][k]['item_condition']
                body_var3 = wjson[1][k]['item_condition_description']
                body_var4 = wjson[1][k]['item_qty']
                body_var6a = wjson[2][k]['packed_item_weight_lb']
                body_var6b = wjson[2][k]['packed_item_weight_oz']
                body_var7 = wjson[2][k]['packed_item_height']
                body_var8 = wjson[2][k]['packed_item_length']
                body_var9 = wjson[2][k]['packed_item_depth']
                json_payload_body['product']['title'] = body_var1
                json_payload_body['condition'] = body_var2
                json_payload_body['conditionDescription'] = body_var3
                json_payload_body['availability']['shipToLocationAvailability']['quantity'] = body_var4
                #convert weight to single unit
                body_var6a = body_var6a * 16
                body_var6b = body_var6a + body_var6b
                #json_payload_body['packageWeightAndSize']['packageType'] = body_var5
                json_payload_body['packageWeightAndSize']['weight']['value'] = body_var6b
                json_payload_body['packageWeightAndSize']['dimensions']['height'] = body_var7
                json_payload_body['packageWeightAndSize']['dimensions']['length'] = body_var8
                json_payload_body['packageWeightAndSize']['dimensions']['width'] = body_var9

                # assign second google sheet profile (vjson) (sheet2) in the inventory and grab sku
                #for now, set item_id to sku
                uri_param1 = wjson[0][k]['item_id']
                #open token file
                token_file = open(filepath_token).read()
                # eBay API requires Bearer token
                tokenPrepared = "Bearer " + token_file
                #read destination file
                # Get JSON body of inventory item from local file (put this on google sheet, get with gsheet api?)
                body_string = str(json_payload_body)
                body = body_string.replace("\'", "\"")
                time.sleep(0.25)
                api_response = bll.ebay_api_connector.inventory_createOrReplaceInventoryItem(tokenPrepared, uri_env, uri_param1, body)
                api_array.append(api_response)
                api_array.append(api_response.text)
                api_array.append(api_response.status_code)
                time.sleep(3)
                k = k + 1

            print("API_ARRAY")
            print(api_array)

        # reset api_array for next if statement
        api_array = []
        if script == "create_item_offer":
            # open the right payload file with json data
            api_payload_filename = api_payload_folder + payloadFilenameMap['inventory_createOffer']
            api_payload_file = open(api_payload_filename, "r")
            # replace values in json_payload_body with data from wjson variable
            json_payload_body = json.load(api_payload_file)
            api_payload_file.close()
            k = 0
            while k < object_count[0][0]:
                body_var1 = wjson[2][k]['ship_policy']
                body_var2 = wjson[2][k]['payment_policy']
                body_var3 = wjson[2][k]['return_policy']
                body_var4 = wjson[1][k]['item_qty']
                # categoryId from category API
                body_var5 = wjson[1][k]['item_category']
                body_var6 = wjson[1][k]['item_condition_description']
                body_var7 = wjson[3][k]['item_merchantLocationKey']
                body_var8 = wjson[1][k]['item_price']
                json_payload_body['listingPolicies']['paymentPolicyId'] = body_var1
                json_payload_body['listingPolicies']['returnPolicyId'] = body_var2
                json_payload_body['listingPolicies']['fulfillmentPolicyId'] = body_var3
                json_payload_body['listingPolicies']['ebayPlusIfEligible'] = "false"
                json_payload_body['availableQuantity'] = body_var4
                #derive this from "stage3"."Item Category"
                json_payload_body['categoryId'] = body_var5
                json_payload_body['conditionDescription'] = body_var6
                #derive this from "stage2"."location"."Section"
                json_payload_body['merchantLocationKey'] = body_var7
                json_payload_body['pricingSummary']['price']['value'] = body_var8
                json_payload_body['pricingSummary']['price']['currency'] = "USD"

                #open token file
                token_file = open(filepath_token).read()
                # eBay API requires Bearer token
                tokenPrepared = "Bearer " + token_file
                #read destination file
                # Get JSON body of inventory item from local file (put this on google sheet, get with gsheet api?)
                body_string = str(json_payload_body)
                body = body_string.replace("\'", "\"")
                api_response = bll.ebay_api_connector.inventory_createOffer(tokenPrepared, uri_env, body)
                api_array.append(api_response)
                api_array.append(api_response.text)
                api_array.append(api_response.status_code)
                time.sleep(1)
                k = k + 1

            print("API_ARRAY")
            print(api_array)







    # return api_response_set





# Execute API calls per configDataSet values ("Script Runtime" area2), returning api response data into proper file

# once this file (_main_exe.py) has ran, write back current time in
#   "ebay-config-data"."config_data"."Script Runtime"."Script Last Executed"

# This definition builds the call sequence file based on needed API body response payloads
# current_api_call_body ~ a list of api call response filenames
#   (each api call with a body is associated with a filename in mapPayloadBodyToFilename in ebay_api_connector)
def writeCallSequenceFile(current_api_call_body):
    print("writeCallSequenceFile")
    configFileName = "callSequenceFile.csf"
    file = open(configFileName, 'w')
    for call_body in current_api_call_body:
        file.write(call_body)

    file.close()





def tempStuff():
    repo_path = r'C:\Users\dick\Documents\GitHub'
    # api_calls_dir is the file path of the api_calls folder
    api_calls_dir = repo_path + r'\ebay_api\bll\dal\api_calls'
    # api_call_filename_list is a list of JSON file names of the api calls in the api_calls folder
    api_call_filename_list = bll.dal.api_local_file_accessor.get_api_call_filename_list(api_calls_dir)



    # Identifies what api call to make
    call_identifier = "createOrReplaceInventoryItem.json"
    # currently selected call fileinfo (filename and index in its array)
    selected_call_fileinfo = bll.dal.api_local_file_accessor.apiCallSelector(api_call_filename_list, call_identifier)
    # File that contains filenames of api calls to cycle through, one per line
    callSequenceFile = repo_path + r'\ebay_api\bll\callSequenceFile.csf'

    """ Data of call_sequence_with_dir:
    #   # create array of filepaths and filedata
    #   call_sequence_set = []
    #   call_sequence_set.append(call_sequence_set_fileinfo)
    #   call_sequence_set.append(call_sequence_set_filedata)
    #   call_sequence_with_dir = {}
    #
    #   # add set of call sequence to list
    #   call_sequence_with_dir['call_sequence_set'] = call_sequence_set
    #   # add the api_calls_dir to the list as well
    #   call_sequence_with_dir['api_calls_dir'] = api_calls_dir
    """
    # Get the data of the call sequence
    # (object includes:
    #   current api_calls directory and
    #   array of api calls that includes:
    #       filename,
    #       index of filename,
    #       and data of file
    # )
    call_sequence_with_dir = bll.dal.api_sequencer.callSequence(callSequenceFile, api_call_filename_list, api_calls_dir)
    print(call_sequence_with_dir)