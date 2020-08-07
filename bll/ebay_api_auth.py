import bll.ebay_api_connector
import base64
import json

def get_auth_data(uri_env, configDataSet):
    if uri_env == "sandbox":
        #client_id = "JosephKo-apidashb-SBX-966850dff-4fa8fb98"
        client_id = configDataSet[10][1][1]
        #redirect_uri = "Joseph_Kodos-JosephKo-apidas-qffjklr"
        redirect_uri = configDataSet[10][2][1]
        #client_secret = "SBX-66850dff5527-e280-46a9-967b-c7a0"
        client_secret = configDataSet[10][3][1]

    if uri_env == "production":
        #client_id = "JosephKo-apidashb-PRD-5d8c7c7a2-3c0aad96"
        client_id = configDataSet[10][4][1]
        #redirect_uri = "Joseph_Kodos-JosephKo-apidas-mvfqrc"
        redirect_uri = configDataSet[10][5][1]
        #client_secret = "PRD-d8c7c7a24e43-c089-4662-ba58-4252"
        client_secret = configDataSet[10][6][1]

    response_type = "code"
    # state = "custom-state-value"
    #scope = "https%3A%2F%2Fapi.ebay.com%2Foauth%2Fapi_scope%2Fsell.inventory%20https%3A%2F%2Fapi.ebay.com%2Foauth%2Fapi_scope%2Fsell.account%20https%3A%2F%2Fapi.ebay.com%2Foauth%2Fapi_scope"
    scope = configDataSet[10][7][1]
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



def get_authorize_code(uri_env, configDataSet):

    # input test_credentials into webpage:
    # testuser_quincy443
    # P@ssw0rd

    auth_data = get_auth_data(uri_env, configDataSet)
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
    #auth_code_generator_path = r'C:\Users\dick\Documents\GitHub\ebay_api\bll\auth_code_webpage.html'
    auth_code_generator_path = configDataSet[10][8][1]
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