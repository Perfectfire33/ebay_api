import bll.dal.api_local_file_accessor
import bll.ebay_object_receiver
import json
import bll.ebay_api_connector
import time
import os
import base64

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
    headers.append('item_category')
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


def get_headers_payment_policy():
    headers4 = []
    headers4.append('categoryTypes[i].default')
    headers4.append('categoryTypes[i].name')
    headers4.append('description')
    headers4.append('immediatePay')
    headers4.append('marketplaceId')
    headers4.append('name')
    headers4.append('paymentInstructions')
    headers4.append('paymentMethods[i][paymentMethodType]')
    headers4.append('paymentMethods[i][recipientAccountReference.referenceId]')
    headers4.append('paymentMethods[i][recipientAccountReference.referenceType]')

    return headers4


def get_headers_return_policy():
    headers = []
    headers.append('categoryTypes[i].default')
    headers.append('categoryTypes[i].name')
    headers.append('description')
    headers.append('internationalOverride.returnPeriod.unit')
    headers.append('internationalOverride.returnPeriod.value')
    headers.append('internationalOverride.returnsAccepted')
    headers.append('internationalOverride.returnShippingCostPayer')
    headers.append('marketplaceId')
    headers.append('name')
    headers.append('refundMethod')
    headers.append('returnInstructions')
    headers.append('returnPeriod.unit')
    headers.append('returnPeriod.value')
    headers.append('returnsAccepted')
    headers.append('returnShippingCostPayer')

    return headers


def get_auth_data(uri_env):
    if uri_env == "sandbox":
        client_id = "JosephKo-apidashb-SBX-966850dff-4fa8fb98"
        redirect_uri = "Joseph_Kodos-JosephKo-apidas-qffjklr"
        client_secret = "SBX-66850dff5527-e280-46a9-967b-c7a0"

    if uri_env == "production":
        client_id = "JosephKo-apidashb-PRD-5d8c7c7a2-3c0aad96"
        redirect_uri = "Joseph_Kodos-JosephKo-apidas-mvfqrc"
        client_secret = "PRD-d8c7c7a24e43-c089-4662-ba58-4252"

    response_type = "code"
    # state = "custom-state-value"
    scope = "https%3A%2F%2Fapi.ebay.com%2Foauth%2Fapi_scope%2Fsell.inventory%20https%3A%2F%2Fapi.ebay.com%2Foauth%2Fapi_scope%2Fsell.account%20https%3A%2F%2Fapi.ebay.com%2Foauth%2Fapi_scope"
    dataToEncode = client_id + ":" + client_secret
    #https://stackoverflow.com/questions/8908287/why-do-i-need-b-to-encode-a-string-with-base64
    base64_oauth_credentials = base64.b64encode(dataToEncode.encode())

    auth_data = []
    auth_data.append(client_id)
    auth_data.append(response_type)
    auth_data.append(scope)
    auth_data.append(base64_oauth_credentials)
    auth_data.append(redirect_uri)

    return auth_data


def get_authorize_code(uri_env):

    # input test_credentials into webpage:
    # testuser_quincy443
    # P@ssw0rd

    auth_data = get_auth_data(uri_env)
    uri_param1 = auth_data[0]
    uri_param2 = auth_data[4]
    uri_param3 = auth_data[1]
    # uri_param4 = auth_data[5]
    uri_param5 = auth_data[2]

    api_response = bll.ebay_api_connector.app_getAuthorizationAuthCode(uri_env, uri_param1, uri_param2,
                                                                           uri_param3, uri_param5)
    api_array = []
    api_array.append(api_response)
    api_array.append(api_response.text)
    api_array.append(api_response.status_code)
    print("API_ARRAY")
    print(api_array)

    # Set filepath auth_code_generator for ebay api access
    #to add into ebay-config-data
    auth_code_generator_path = r'C:\Users\dick\Documents\GitHub\ebay_api\bll\auth_code_webpage.html'
    auth_code_file_data = api_array[1]
    # write website file
    auth_code_web_file = open(auth_code_generator_path, "w")
    auth_code_web_file.write(auth_code_file_data)
    auth_code_web_file.close()
    #api_array.append(auth_code_generator_path)

    return auth_code_generator_path


#def get_user_refresh_token(configDataSet, uri_env):
#https://ebaydts.com/eBayKBDetails?KBid=5075


def get_user_access_token(configDataSet, uri_env, auth_code):
    # auth_code - run ebay_object_matcher.get_authorize_code()
    auth_data = get_auth_data(uri_env)
    #auth_code_doc = api_response[1]

    # auth_string - "Basic <B64-encoded-oauth-credentials>"
    #auth_string = "Basic " + "Sm9zZXBoS28tYXBpZGFzaGItU0JYLTk2Njg1MGRmZi00ZmE4ZmI5ODpTQlgtNjY4NTBkZmY1NTI3LWUyODAtNDZhOS05NjdiLWM3YTA="
    base64oauth_creds = str(auth_data[3])
    base64oauth_creds = base64oauth_creds[:-1]
    base64oauth_creds = base64oauth_creds[2:]
    auth_string = "Basic " + base64oauth_creds
    print("auth_string")
    print(auth_string)
    # body:
    #     grant_type=authorization_code
    #     code=<authorization-code-value>
    #     redirect_uri=<RuName-value>
    body1 = "grant_type=authorization_code"
    body2 = "&code=" + auth_code
    body3 =  "&redirect_uri=" + auth_data[4]

    body = body1 + body2 + body3
    print("body")
    print(body)

    api_response = bll.ebay_api_connector.app_getUserAccessToken(auth_string, uri_env, body)
    api_array = []
    api_array.append(api_response)
    api_array.append(api_response.text)
    api_array.append(api_response.status_code)
    print("api_array")
    print(api_array)
    api_response_json = json.loads(api_array[1])

    # Set filepath token for ebay api access
    filepath_token = configDataSet[0][2][2] + configDataSet[0][2][1]
    print("filepath_token")
    print(filepath_token)
    # write token file
    token_file = open(filepath_token, "w")
    token_file.write(api_response_json['access_token'])
    token_file.close()

    # Set filepath token for ebay api access
    filepath_refresh_token = configDataSet[0][9][2] + configDataSet[0][9][1]
    print("filepath_refresh_token")
    print(filepath_refresh_token)
    # write refresh token file
    refresh_token_file = open(filepath_refresh_token, "w")
    refresh_token_file.write(api_response_json['refresh_token'])
    refresh_token_file.close()

    return api_array


#get list of rows necessary to go through the number of offers,
# then get list of offer ids based on item_id,
# then publish the list of offer ids one at a time by calling publish_item_offer(configDataSet, uri_env)
#
#def publish_item_offer_set(configDataSet, appDataSet, uri_env):

# pass this data through publish_item_offer_set
# for return data - can select an offer based on a key's value,
#   we can create a checker function to see if there are two offers for one item sku
def get_list_of_item_offers_for_list_of_items(configDataSet, appDataSet, uri_env):
    headers = get_headers_data_i()
    # Import JSON header-data matched object
    wjson = bll.ebay_object_receiver.loadJsonData(appDataSet, headers)
    marketplace_id = "EBAY_US"
    format = "FIXED_PRICE"
    k = 0
    all_item_api_array = []
    while k < len(wjson[0]):
        # uri_param1 ~~ {sku}
        uri_param1 = wjson[0][k]['item_id']
        # uri_param2 ~~ {marketplace_id}
        uri_param2 = marketplace_id
        # uri_param3 ~~ {format}
        uri_param3 = format
        # uri_param4 ~~ {limit}
        uri_param4 = 25
        # uri_param5 ~~ {offset}
        uri_param5 = 0
        api_array = []
        # Set filepath token for ebay api access
        filepath_token = configDataSet[0][2][2] + configDataSet[0][2][1]
        # open token file
        token_file = open(filepath_token).read()
        # eBay API requires Bearer token
        tokenPrepared = "Bearer " + token_file
        api_response = bll.ebay_api_connector.inventory_getOffers(tokenPrepared, uri_env, uri_param1, uri_param2, uri_param3, uri_param4, uri_param5)
        api_array.append(api_response)
        api_array.append(api_response.text)
        api_array.append(api_response.status_code)
        all_item_api_array.append(api_array)
        k = k + 1

    return all_item_api_array

#def get_list_of_offers_for_an_item():


def delete_item_offer(configDataSet, uri_env, offer_id):
    api_array = []
    # Set filepath token for ebay api access
    filepath_token = configDataSet[0][2][2] + configDataSet[0][2][1]
    # uri_param1 ~ offerId
    uri_param1 = offer_id
    # open token file
    token_file = open(filepath_token).read()
    # eBay API requires Bearer token
    tokenPrepared = "Bearer " + token_file
    api_response = bll.ebay_api_connector.inventory_deleteOffer(tokenPrepared, uri_env, uri_param1)
    api_array.append(api_response)
    api_array.append(api_response.text)
    api_array.append(api_response.status_code)
    return api_array



def withdraw_item_offer(configDataSet, uri_env, offer_id):
    api_array = []
    # Set filepath token for ebay api access
    filepath_token = configDataSet[0][2][2] + configDataSet[0][2][1]
    # uri_param1 ~ offerId
    uri_param1 = offer_id
    # open token file
    token_file = open(filepath_token).read()
    # eBay API requires Bearer token
    tokenPrepared = "Bearer " + token_file
    api_response = bll.ebay_api_connector.inventory_withdrawOffer(tokenPrepared, uri_env, uri_param1)
    api_array.append(api_response)
    api_array.append(api_response.text)
    api_array.append(api_response.status_code)
    return api_array

def publish_item_offer(configDataSet, uri_env, offer_id):
    api_array = []
    # Set filepath token for ebay api access
    filepath_token = configDataSet[0][2][2] + configDataSet[0][2][1]
    # uri_param1 ~ offerId
    uri_param1 = offer_id
    # open token file
    token_file = open(filepath_token).read()
    # eBay API requires Bearer token
    tokenPrepared = "Bearer " + token_file
    api_response = bll.ebay_api_connector.inventory_publishOffer(tokenPrepared, uri_env, uri_param1)
    api_array.append(api_response)
    api_array.append(api_response.text)
    api_array.append(api_response.status_code)
    return api_array



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

def get_all_payment_policies(configDataSet, uri_env):
    api_array = []
    # Set filepath token for ebay api access
    filepath_token = configDataSet[0][2][2] + configDataSet[0][2][1]
    # uri_param1 ~ marketplace_id
    uri_param1 = "EBAY_US"
    # open token file
    token_file = open(filepath_token).read()
    # eBay API requires Bearer token
    tokenPrepared = "Bearer " + token_file
    api_response = bll.ebay_api_connector.account_getPaymentPolicies(tokenPrepared, uri_env, uri_param1)
    api_array.append(api_response)
    api_array.append(api_response.text)
    api_array.append(api_response.status_code)
    return api_array

def get_all_return_policies(configDataSet, uri_env):
    api_array = []
    # Set filepath token for ebay api access
    filepath_token = configDataSet[0][2][2] + configDataSet[0][2][1]
    # uri_param1 ~ marketplace_id
    uri_param1 = "EBAY_US"
    # open token file
    token_file = open(filepath_token).read()
    # eBay API requires Bearer token
    tokenPrepared = "Bearer " + token_file
    api_response = bll.ebay_api_connector.account_getReturnPolicies(tokenPrepared, uri_env, uri_param1)
    api_array.append(api_response)
    api_array.append(api_response.text)
    api_array.append(api_response.status_code)
    return api_array

def get_all_fulfillment_policies(configDataSet, uri_env):
    api_array = []
    # Set filepath token for ebay api access
    filepath_token = configDataSet[0][2][2] + configDataSet[0][2][1]
    # uri_param1 ~ marketplace_id
    uri_param1 = "EBAY_US"
    # open token file
    token_file = open(filepath_token).read()
    # eBay API requires Bearer token
    tokenPrepared = "Bearer " + token_file
    api_response = bll.ebay_api_connector.account_getFulfillmentPolicies(tokenPrepared, uri_env, uri_param1)
    api_array.append(api_response)
    api_array.append(api_response.text)
    api_array.append(api_response.status_code)
    return api_array


def getListOfFulfillmentPolicyNames(configDataSet, uri_env):
    api_array = bll.ebay_object_matcher.get_all_fulfillment_policies(configDataSet, uri_env)
    data = api_array[1]
    json_data = json.loads(data)
    print("json_data")
    print(json_data)
    name_array = []
    i = 0
    while i < len(json_data['fulfillmentPolicies']):
        name_array.append(json_data['fulfillmentPolicies'][i]['name'])
        i = i + 1

    return name_array



def getListOfPaymentPolicyNames(configDataSet, uri_env):
    api_array = bll.ebay_object_matcher.get_all_payment_policies(configDataSet, uri_env)
    data = api_array[1]
    json_data = json.loads(data)
    print("json_data")
    print(json_data)
    name_array = []
    i = 0
    while i < len(json_data['paymentPolicies']):
        name_array.append(json_data['paymentPolicies'][i]['name'])
        i = i + 1

    return name_array


def getListOfReturnPolicyNames(configDataSet, uri_env):
    api_array = bll.ebay_object_matcher.get_all_return_policies(configDataSet, uri_env)
    data = api_array[1]
    json_data = json.loads(data)
    print("json_data")
    print(json_data)
    name_array = []
    i = 0
    while i < len(json_data['returnPolicies']):
        name_array.append(json_data['returnPolicies'][i]['name'])
        i = i + 1

    return name_array

#def write_fulfillment_policy_name_list_to_file():





#gets list of policies from appDataSet and creates an API call for each unique policy
#returns response from each API call: must return list of policies, Ids for those policies, and currentItemId
def get_payment_policy_id_list_via_name(configDataSet, appDataSet, uri_env):
    headers = get_headers_data_i()
    # Import JSON header-data matched object
    wjson = bll.ebay_object_receiver.loadJsonData(appDataSet, headers)
    # Set filepath token for ebay api access
    filepath_token = configDataSet[0][2][2] + configDataSet[0][2][1]
    # uri_param1 ~ marketplace_id
    uri_param1 = "EBAY_US"
    # list of payment policies in current selected inventory area
    payment_policy_list = []
    payment_policy_init_list = []
    # for each row in inventory, make an api request payload with the data
    object_count = bll.ebay_object_matcher.getObjectCount(configDataSet, appDataSet, headers)
    j = 0
    while j < object_count[0][0]:
        payment_policy_init_list.append(wjson[2][j]['payment_policy'])
        j = j + 1

    payment_policy_list = list(dict.fromkeys(payment_policy_init_list))
    print("payment_policy_list")
    print(payment_policy_list)
    #array for all api calls made
    api_arrayAll = []
    # open token file
    token_file = open(filepath_token).read()
    # eBay API requires Bearer token
    tokenPrepared = "Bearer " + token_file
    k = 0
    #for each item in payment_policy_list
    while k < len(payment_policy_list):
        api_array = []
        #get current payment policy list name
        uri_param2 = payment_policy_list[k]
        print("uri_param2")
        print(uri_param2)
        time.sleep(1)
        api_response = bll.ebay_api_connector.account_getPaymentPolicyByName(tokenPrepared, uri_env, uri_param1,
                                                                             uri_param2)
        api_array.append(api_response)
        api_array.append(api_response.text)
        api_array.append(api_response.status_code)
        api_arrayAll.append(api_array)
        k = k + 1

    print("api_arrayAll")
    print(api_arrayAll)
    #get policy id for each item based on policy_name
    api_responseList = []
    for item in api_arrayAll:
        api_responseList.append(api_arrayAll[api_arrayAll.index(item)][1])

    j = 0
    print("api_responseList")
    print(api_responseList)
    result_list = {}
    while j < object_count[0][0]:
        for api_response in api_responseList:
            api_json_response = json.loads(api_response)
            if api_json_response['name'] == wjson[2][j]['payment_policy']:
                result_list[wjson[0][j]['item_id']]=api_json_response['paymentPolicyId']
        j = j + 1
    # result_list ~ a list of ids that match 1:1 with each item in inventory for e.g. create_item_offer
    # use this in create_item_offer while loop
    return result_list


# gets list of policies from appDataSet and creates an API call for each unique policy
# returns response from each API call: must return list of policies, Ids for those policies, and currentItemId
def get_return_policy_id_list_via_name(configDataSet, appDataSet, uri_env):
    headers = get_headers_data_i()
    # Import JSON header-data matched object
    wjson = bll.ebay_object_receiver.loadJsonData(appDataSet, headers)
    # Set filepath token for ebay api access
    filepath_token = configDataSet[0][2][2] + configDataSet[0][2][1]
    # uri_param1 ~ marketplace_id
    uri_param1 = "EBAY_US"
    # list of payment policies in current selected inventory area
    return_policy_list = []
    return_policy_init_list = []
    # for each row in inventory, make an api request payload with the data
    object_count = bll.ebay_object_matcher.getObjectCount(configDataSet, appDataSet, headers)
    j = 0
    while j < object_count[0][0]:
        return_policy_init_list.append(wjson[2][j]['return_policy'])
        j = j + 1

    return_policy_list = list(dict.fromkeys(return_policy_init_list))
    print("return_policy_list")
    print(return_policy_list)
    # array for all api calls made
    api_arrayAll = []
    # open token file
    token_file = open(filepath_token).read()
    # eBay API requires Bearer token
    tokenPrepared = "Bearer " + token_file
    k = 0
    # for each item in payment_policy_list
    while k < len(return_policy_list):
        api_array = []
        # get current payment policy list name
        uri_param2 = return_policy_list[k]
        time.sleep(1)
        api_response = bll.ebay_api_connector.account_getReturnPolicyByName(tokenPrepared, uri_env, uri_param1,
                                                                             uri_param2)
        api_array.append(api_response)
        api_array.append(api_response.text)
        api_array.append(api_response.status_code)
        api_arrayAll.append(api_array)
        time.sleep(1)
        k = k + 1

    # get policy id for each item based on policy_name
    api_responseList = []
    for item in api_arrayAll:
        api_responseList.append(api_arrayAll[api_arrayAll.index(item)][1])

    j = 0
    result_list = {}
    while j < object_count[0][0]:
        for api_response in api_responseList:
            api_json_response = json.loads(api_response)
            if api_json_response['name'] == wjson[2][j]['return_policy']:
                result_list[wjson[0][j]['item_id']] = api_json_response['returnPolicyId']
        j = j + 1
    # result_list ~ a list of ids that match 1:1 with each item in inventory for e.g. create_item_offer
    # use this in create_item_offer while loop
    return result_list



# gets list of policies from appDataSet and creates an API call for each unique policy
# returns response from each API call: must return list of policies, Ids for those policies, and currentItemId
def get_fulfillment_policy_id_list_via_name(configDataSet, appDataSet, uri_env):
    headers = get_headers_data_i()
    # Import JSON header-data matched object
    wjson = bll.ebay_object_receiver.loadJsonData(appDataSet, headers)
    # Set filepath token for ebay api access
    filepath_token = configDataSet[0][2][2] + configDataSet[0][2][1]
    # uri_param1 ~ marketplace_id
    uri_param1 = "EBAY_US"
    # list of payment policies in current selected inventory area
    fulfillment_policy_list = []
    fulfillment_policy_init_list = []
    # for each row in inventory, make an api request payload with the data
    object_count = bll.ebay_object_matcher.getObjectCount(configDataSet, appDataSet, headers)
    j = 0
    while j < object_count[0][0]:
        fulfillment_policy_init_list.append(wjson[2][j]['ship_policy'])
        j = j + 1

    fulfillment_policy_list = list(dict.fromkeys(fulfillment_policy_init_list))
    #print("fulfillment_policy_list")
    #print(fulfillment_policy_list)
    # array for all api calls made
    api_arrayAll = []
    # open token file
    token_file = open(filepath_token).read()
    # eBay API requires Bearer token
    tokenPrepared = "Bearer " + token_file
    k = 0
    # for each item in payment_policy_list
    while k < len(fulfillment_policy_list):
        api_array = []
        # get current payment policy list name
        uri_param2 = fulfillment_policy_list[k]
        time.sleep(1)
        api_response = bll.ebay_api_connector.account_getFulfillmentPolicyByName(tokenPrepared, uri_env, uri_param1,
                                                                             uri_param2)
        api_array.append(api_response)
        api_array.append(api_response.text)
        api_array.append(api_response.status_code)
        api_arrayAll.append(api_array)
        k = k + 1

    # get policy id for each item based on policy_name
    api_responseList = []
    for item in api_arrayAll:
        api_responseList.append(api_arrayAll[api_arrayAll.index(item)][1])

    j = 0
    result_list = {}
    while j < object_count[0][0]:
        for api_response in api_responseList:
            api_json_response = json.loads(api_response)
            if api_json_response['name'] == wjson[2][j]['ship_policy']:
                result_list[wjson[0][j]['item_id']] = api_json_response['fulfillmentPolicyId']
        j = j + 1
    # result_list ~ a list of ids that match 1:1 with each item in inventory for e.g. create_item_offer
    # use this in create_item_offer while loop
    return result_list


#read suggestion query from google sheet
#write back id to google sheet
# def get_category_suggestions_from_inventory():


def get_category_suggestions(configDataSet, uri_env):
    api_array = []
    # Set filepath token for ebay api access
    filepath_token = configDataSet[0][2][2] + configDataSet[0][2][1]
    # uri_param1 ~ category_tree_id
    #get default category tree
    uri_param1a = get_default_category_tree(configDataSet, uri_env)
    print("uri_param1a")
    print(uri_param1a)
    uri_param1b = json.loads(uri_param1a[1])
    uri_param1 = uri_param1b['categoryTreeId']
    # uri_param1 ~ query string ~ from stage2+stage3
    uri_param2 = "Rosenthal China & Dinnerware"
    # open token file
    token_file = open(filepath_token).read()
    # eBay API requires Bearer token
    tokenPrepared = "Bearer " + token_file
    api_response = bll.ebay_api_connector.taxonomy_getCategorySuggestions(tokenPrepared, uri_env, uri_param1, uri_param2)
    api_array.append(api_response)
    api_array.append(api_response.text)
    api_array.append(api_response.status_code)
    return api_array

def get_default_category_tree(configDataSet, uri_env):
    api_array = []
    # Set filepath token for ebay api access
    filepath_token = configDataSet[0][2][2] + configDataSet[0][2][1]
    # uri_param1 ~ marketplace_id
    uri_param1 = "EBAY_US"
    # uri_param1 ~ query string ~ from
    # open token file
    token_file = open(filepath_token).read()
    # eBay API requires Bearer token
    tokenPrepared = "Bearer " + token_file
    api_response = bll.ebay_api_connector.taxonomy_getDefaultCategoryTreeId(tokenPrepared, uri_env, uri_param1)
    api_array.append(api_response)
    api_array.append(api_response.text)
    api_array.append(api_response.status_code)
    return api_array




# creates folders with the box_name from stage2 in ebay_item_inventory in the pictures directory in ebay-config-data
def createPictureFolders(configDataSet, appDataSet2):
    print("createPictureFolders")
    headers2 = get_headers_data_ii()
    # Import config Picture Folder
    picture_folder = configDataSet[0][8][2]
    print("picture_folder")
    print(picture_folder)
    # Import JSON header-data matched object
    vjson = bll.ebay_object_receiver.loadJsonData(appDataSet2, headers2)
    k = 0
    while k < len(vjson[0]):
        os.mkdir(picture_folder + vjson[0][k]['box_name'])
        print(vjson[0][k]['box_name'])
        k = k + 1


#def getPictureFilepaths():

#1|create picture folders
#2|put pictures in folders
#3|get picture filepaths for each folder where folderName = box_name
#3.5| host pictures on webserver so we can get a public url with the image
#3.7| generate list of http:\\ locations of each image for each box_name
#4|in createOrReplaceInventoryItem, add list of picture urls for each item





def create_payment_policy(configDataSet, uri_env):
    #headers4 = get_headers_payment_policy()
    # Import JSON header-data matched object
    #print("appDataSet4")
    #print(appDataSet4)
    #xjson = bll.ebay_object_receiver.loadJsonData(appDataSet4, headers4)
    #print("XJSON")
    #print(xjson)
    # Set filepath token for ebay api access
    filepath_token = configDataSet[0][2][2] + configDataSet[0][2][1]
    # This is the file that includes the api call data
    filepath_body = configDataSet[0][6][2] + configDataSet[0][6][1]
    # This is the folder of the json request payload files
    api_payload_folder = configDataSet[0][7][2]
    payloadFilenameMap = bll.ebay_api_connector.getPayloadFilenameMap()
    # open the right payload file with json data
    api_payload_filename = api_payload_folder + payloadFilenameMap['account_createPaymentPolicy']
    api_payload_file = open(api_payload_filename, "r")
    # replace values in json_payload_body with data from wjson variable
    json_payload_body = json.load(api_payload_file)
    api_payload_file.close()
    api_array = []
    body_var1 = "description_03"
    body_var2 = "name_03"
    body_var3 = "paymentInstructions_03"
    json_payload_body['categoryTypes'][0]['default'] = "true"
    json_payload_body['categoryTypes'][0]['name'] = "ALL_EXCLUDING_MOTORS_VEHICLES"
    json_payload_body['description'] = body_var1
    json_payload_body['immediatePay'] = "true"
    json_payload_body['marketplaceId'] = "EBAY_US"
    json_payload_body['name'] = body_var2
    json_payload_body['paymentInstructions'] = body_var3
    json_payload_body['paymentMethods'][0]['paymentMethodType'] = "PAYPAL"
    json_payload_body['paymentMethods'][0]['recipientAccountReference']['referenceId'] = "perfectfireiii@gmail.com"
    json_payload_body['paymentMethods'][0]['recipientAccountReference']['referenceType'] = "PAYPAL_EMAIL"
    print("json_payload_body")
    print(json_payload_body)
    # open token file
    token_file = open(filepath_token).read()
    # eBay API requires Bearer token
    tokenPrepared = "Bearer " + token_file
    # read destination file
    # Get JSON body of inventory item from local file (put this on google sheet, get with gsheet api?)
    body_string = str(json_payload_body)
    body = body_string.replace("\'", "\"")
    time.sleep(0.25)
    api_response = bll.ebay_api_connector.account_createPaymentPolicy(tokenPrepared, uri_env, body)
    api_array.append(api_response)
    api_array.append(api_response.text)
    api_array.append(api_response.status_code)
    #from here, can also send misc data to flask API to create webpage or store data in SQLite DB
    #print("API_ARRAY")
    #print(api_array)
    return api_array

def create_return_policy(configDataSet, uri_env):
    #headers = get_headers_return_policy()
    # Import JSON header-data matched object
    #print("appDataSet4")
    #print(appDataSet4)
    #xjson = bll.ebay_object_receiver.loadJsonData(appDataSet4, headers4)
    #print("XJSON")
    #print(xjson)
    # Set filepath token for ebay api access
    filepath_token = configDataSet[0][2][2] + configDataSet[0][2][1]
    # This is the file that includes the api call data
    filepath_body = configDataSet[0][6][2] + configDataSet[0][6][1]
    # This is the folder of the json request payload files
    api_payload_folder = configDataSet[0][7][2]
    payloadFilenameMap = bll.ebay_api_connector.getPayloadFilenameMap()
    # open the right payload file with json data
    api_payload_filename = api_payload_folder + payloadFilenameMap['account_createReturnPolicy']
    api_payload_file = open(api_payload_filename, "r")
    # replace values in json_payload_body with data from wjson variable
    json_payload_body = json.load(api_payload_file)
    api_payload_file.close()
    api_array = []
    body_var1 = "description_03"
    body_var2 = "name_03"
    body_var3 = "returnInstructions_03"

    json_payload_body['categoryTypes'][0]['default'] = "true"
    json_payload_body['categoryTypes'][0]['name'] = "ALL_EXCLUDING_MOTORS_VEHICLES"
    json_payload_body['description'] = body_var1
    json_payload_body['internationalOverride']['returnPeriod']['unit'] = "DAY"
    json_payload_body['internationalOverride']['returnPeriod']['value'] = "30"
    json_payload_body['internationalOverride']['returnsAccepted'] = "true"
    json_payload_body['internationalOverride']['returnShippingCostPayer'] = "SELLER"
    json_payload_body['marketplaceId'] = "EBAY_US"
    json_payload_body['name'] = body_var2
    json_payload_body['refundMethod'] = "MONEY_BACK"
    json_payload_body['returnInstructions'] = body_var3
    json_payload_body['returnPeriod']['unit'] = "DAY"
    json_payload_body['returnPeriod']['value'] = "30"
    json_payload_body['returnsAccepted'] = "true"
    json_payload_body['returnShippingCostPayer'] = "SELLER"
    print("json_payload_body")
    print(json_payload_body)
    # open token file
    token_file = open(filepath_token).read()
    # eBay API requires Bearer token
    tokenPrepared = "Bearer " + token_file
    # read destination file
    # Get JSON body of inventory item from local file (put this on google sheet, get with gsheet api?)
    body_string = str(json_payload_body)
    body = body_string.replace("\'", "\"")
    time.sleep(0.25)
    api_response = bll.ebay_api_connector.account_createReturnPolicy(tokenPrepared, uri_env, body)
    api_array.append(api_response)
    api_array.append(api_response.text)
    api_array.append(api_response.status_code)
    #from here, can also send misc data to flask API to create webpage or store data in SQLite DB
    #print("API_ARRAY")
    #print(api_array)
    return api_array

def create_fulfillment_policy(configDataSet, uri_env):
    #headers = get_headers_fulfillment_policy()
    # Import JSON header-data matched object
    #print("appDataSet4")
    #print(appDataSet4)
    #xjson = bll.ebay_object_receiver.loadJsonData(appDataSet4, headers4)
    #print("XJSON")
    #print(xjson)
    # Set filepath token for ebay api access
    filepath_token = configDataSet[0][2][2] + configDataSet[0][2][1]
    # This is the file that includes the api call data
    filepath_body = configDataSet[0][6][2] + configDataSet[0][6][1]
    # This is the folder of the json request payload files
    api_payload_folder = configDataSet[0][7][2]
    payloadFilenameMap = bll.ebay_api_connector.getPayloadFilenameMap()
    # open the right payload file with json data
    api_payload_filename = api_payload_folder + payloadFilenameMap['account_createFulfillmentPolicy']
    api_payload_file = open(api_payload_filename, "r")
    # replace values in json_payload_body with data from wjson variable
    json_payload_body = json.load(api_payload_file)
    api_payload_file.close()
    api_array = []
    body_var1 = "description_01"
    body_var2 = "name_01"
    #Handling Time
    body_var3 = "2"
    #CarrierType
    body_var4 = "USPS"
    #Shipping Cost
    body_var5 = "8.55"
    #ShippingServiceCode https://developer.ebay.com/api-docs/sell/static/seller-accounts/ht_shipping-free.html#shippingServices
    body_var6 = "USPSPriorityFlatRateBox"

    # API https://developer.ebay.com/api-docs/sell/account/resources/fulfillment_policy/methods/createFulfillmentPolicy
    json_payload_body['categoryTypes'][0]['default'] = "true"
    json_payload_body['categoryTypes'][0]['name'] = "ALL_EXCLUDING_MOTORS_VEHICLES"
    json_payload_body['description'] = body_var1
    json_payload_body['globalShipping']= "false"
    json_payload_body['handlingTime']['unit'] = "DAY"
    json_payload_body['handlingTime']['value'] = body_var3
    json_payload_body['localPickup'] = "false"
    json_payload_body['marketplaceId'] = "EBAY_US"
    json_payload_body['name'] = body_var2
    json_payload_body['pickupDropOff'] = "false"
    json_payload_body['shippingOptions'][0]['costType'] = "CALCULATED"
    #json_payload_body['shippingOptions'][0]['insuranceFee']['currency'] = "USD"
    #json_payload_body['shippingOptions'][0]['insuranceFee']['value'] = "0"
    json_payload_body['shippingOptions'][0]['insuranceOffered'] = "false"
    json_payload_body['shippingOptions'][0]['optionType'] = "DOMESTIC"
    json_payload_body['shippingOptions'][0]['packageHandlingCost']['currency'] = "USD"
    json_payload_body['shippingOptions'][0]['packageHandlingCost']['value'] = "0"
    #json_payload_body['shippingOptions'][0]['rateTableId'] = "36-char-uuid"
    #json_payload_body['shippingOptions'][0]['shippingServices'][0]['additionalShippingCost']['currency'] = "USD" #applies to multi quantity
    #json_payload_body['shippingOptions'][0]['shippingServices'][0]['additionalShippingCost']['value'] = "0" #applies to multi quantity
    #json_payload_body['shippingOptions'][0]['shippingServices'][0]['buyerResponsibleForPickup'] = "false" #applies to Motor vehicles only
    #json_payload_body['shippingOptions'][0]['shippingServices'][0]['buyerResponsibleForShipping'] = "false" #applies to Motor vehicles only
    #json_payload_body['shippingOptions'][0]['shippingServices'][0]['cashOnDeliveryFee']['currency'] = "USD"
    #json_payload_body['shippingOptions'][0]['shippingServices'][0]['cashOnDeliveryFee']['value'] = "0"
    json_payload_body['shippingOptions'][0]['shippingServices'][0]['freeShipping'] = "false"
    json_payload_body['shippingOptions'][0]['shippingServices'][0]['shippingCarrierCode'] = body_var4
    json_payload_body['shippingOptions'][0]['shippingServices'][0]['shippingCost']['currency'] = "USD"
    json_payload_body['shippingOptions'][0]['shippingServices'][0]['shippingCost']['value'] = body_var5
    json_payload_body['shippingOptions'][0]['shippingServices'][0]['shippingServiceCode'] = body_var6
    #json_payload_body['shippingOptions'][0]['shippingServices'][0]['shipToLocations']['regionExcluded'][0]['regionName'] = ""
    #json_payload_body['shippingOptions'][0]['shippingServices'][0]['shipToLocations']['regionExcluded'][0]['regionType'] = ""
    #json_payload_body['shippingOptions'][0]['shippingServices'][0]['shipToLocations']['regionIncluded'][0]['regionName'] = ""
    #json_payload_body['shippingOptions'][0]['shippingServices'][0]['shipToLocations']['regionIncluded'][0]['regionType'] = ""
    #json_payload_body['shippingOptions'][0]['shippingServices'][0]['sortOrder'] = "0"
    #json_payload_body['shippingOptions'][0]['shippingServices'][0]['surcharge']['currency'] = "USD"
    #json_payload_body['shippingOptions'][0]['shippingServices'][0]['surcharge']['value'] = "0"
    #json_payload_body['shipToLocations']['RegionExcluded'][0]['regionName'] = "0"
    #json_payload_body['shipToLocations']['RegionExcluded'][0]['regionType'] = "0"
    #json_payload_body['shipToLocations']['RegionIncluded'][0]['regionName'] = "0"
    #json_payload_body['shipToLocations']['RegionIncluded'][0]['regionType'] = "0"

    print("json_payload_body")
    print(json_payload_body)
    # open token file
    token_file = open(filepath_token).read()
    # eBay API requires Bearer token
    tokenPrepared = "Bearer " + token_file
    # read destination file
    # Get JSON body of inventory item from local file (put this on google sheet, get with gsheet api?)
    body_string = str(json_payload_body)
    body = body_string.replace("\'", "\"")
    time.sleep(0.25)
    api_response = bll.ebay_api_connector.account_createFulfillmentPolicy(tokenPrepared, uri_env, body)
    api_array.append(api_response)
    api_array.append(api_response.text)
    api_array.append(api_response.status_code)
    #from here, can also send misc data to flask API to create webpage or store data in SQLite DB
    #print("API_ARRAY")
    #print(api_array)
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

    # get the list of paymentPolicyIds by Payment Policy Name (in inventory)
    # this is a list of item_ids and paymentPolicyIds
    #result_list_paymentPolicyId = get_payment_policy_id_list_via_name(configDataSet, appDataSet, uri_env)
    #json_loaded_list_paymentPolicyId = json.loads(result_list_paymentPolicyId)

    # get the list of returnPolicyIds by Return Policy Name (in inventory)
    # this is a list of item_ids and returnPolicyIds
    #result_list_returnPolicyId = get_return_policy_id_list_via_name(configDataSet, appDataSet, uri_env)
    #json_loaded_list_returnPolicyId = json.loads(result_list_returnPolicyId)

    # get the list of fulfillmentPolicyIds by Fulfillment Policy Name (in inventory)
    # this is a list of item_ids and fulfillmentPolicyIds
    result_list_fulfillmentPolicyId = get_fulfillment_policy_id_list_via_name(configDataSet, appDataSet, uri_env)
    #json_loaded_list_fulfillmentPolicyId = json.loads(result_list_fulfillmentPolicyId)

    #print("result_list_paymentPolicyId")
    #print(result_list_paymentPolicyId)

    #print("result_list_returnPolicyId")
    #print(result_list_returnPolicyId)

    print("result_list_fulfillmentPolicyId")
    print(result_list_fulfillmentPolicyId)

    k = 0
    #array for the api calls in the batch
    api_array = []
    while k < object_count[0][0]:

        # paymentPolicyId from other API
        #body_var1 = result_list_paymentPolicyId[wjson[0][k]['item_id']]
        body_var1 = "114522006022"

        # returnPolicyId from other API
        #body_var2 = result_list_returnPolicyId[wjson[0][k]['item_id']]
        body_var2 = "141882657022"

        # fulfillmentPolicyId from other API
        body_var3 = result_list_fulfillmentPolicyId[wjson[0][k]['item_id']]

        # availableQuantity
        body_var4 = wjson[1][k]['item_qty']

        # categoryId from category API
        #getCategoryIds - list of category ids that are suggested search with categories in item listing
        #then getCategoryName by selected Id
        #Need area in spreadsheet: Get Categories by Search: "category search query: " "category results: ~~ "
        #then, can manually put in a category by Id for the item in the inventory
        #Need area in spreadsheet: Get Category by Id: "category Id: " "category name"
        #This way the user can check for categories and know category name
        #Best to put in id in stage3-item-category (stage2:boxCategory can be for offline use)
        #This file can read from stage3-item-category
        #body_var5a = wjson[1][k]['item_category']
        #body_var5b = vjson[0][k]['box_category']
        # body_var5 = bll.ebay_object_matcher.getCategoryIdBasedOnInventory(body_var5a, body_var5b)
        body_var5 = wjson[1][k]['item_category']

        # merchantLocationKey
        #body_var6a = vjson[0][k]['location']
        #body_var6b = vjson[0][k]['section']
        #body_var6 = body_var6a + "_" + body_var6b
        body_var6 = vjson[0][k]['location']

        # item price
        body_var7a = vjson[0][k]['unit_price'].split("$")
        #body_var7a = wjson[1][k]['item_price'].split("$")
        body_var7b = body_var7a[1]
        print("body_var7a")
        print(body_var7a)
        print("body_var7b")
        print(body_var7b)
        body_var7 = body_var7b
        body_var8 = "EBAY_US"
        body_var9 = "FIXED_PRICE"

        #sku
        body_var10 = wjson[0][k]['item_id']
        #body_var10 = vjson[0][k]['box_name']


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
        #json_payload_body['lotSize'] = ""
        #json_payload_body['storeCategoryNames'][0] = ""
        #json_payload_body['quantityLimitPerBuyer'] = ""
        #json_payload_body['tax']['applyTax'] = ""
        #json_payload_body['tax']['thirdPartyTaxCategory'] = ""
        #json_payload_body['tax']['vatPercentage'] = ""

        # open token file
        token_file = open(filepath_token).read()
        # eBay API requires Bearer token
        tokenPrepared = "Bearer " + token_file
        # read destination file
        # Get JSON body of inventory item from local file (put this on google sheet, get with gsheet api?)
        body_string = str(json_payload_body)
        body = body_string.replace("\'", "\"")
        time.sleep(0.25)
        api_response = bll.ebay_api_connector.inventory_createOffer(tokenPrepared, uri_env,
                                                                                     body)
        api_array.append(api_response)
        api_array.append(api_response.text)
        api_array.append(api_response.status_code)
        # from here, can also send misc data to flask API to create webpage or store data in SQLite DB
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