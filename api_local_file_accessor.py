from os import listdir
from os.path import isfile, join
import simplejson as json


# get_api_contract_filename_list retrieves filename list of api contracts
def get_api_contract_filename_list(api_contract_dir):
    api_contract_filename_list = [f for f in listdir(api_contract_dir) if isfile(join(api_contract_dir, f))]
    return api_contract_filename_list


# load_api_contracts retrieves the data content of the contracts specified in api_contract_filename_list
#   example: contract_data_array = load_api_contracts(api_contract_dir, api_contract_filename_list)
def load_api_contracts(api_contract_dir, api_contract_filename_list):
    contract_data_array = []
    for api_contract_file in api_contract_filename_list:
        currentPath = api_contract_dir + "\\" + api_contract_file
        # print(currentPath)
        contract_data_array.append(open(currentPath).read())
    return contract_data_array


# apiContractSelector selects an api contract to employ based on caller function
#   returns a filename and data of file from bigger array based on matching contract_identifier
# Variables:
#   contract_data_array is the data of the file
#   api_contract_filename_list is the file name (1:1 ratio with call_data_array)
#   contract_identifier is the api contract identifier (should be almost same as file name)
#   example: selected_contract_fileinfo = apiContractSelector(api_contract_filename_list, contract_identifier)
def apiContractSelector(api_contract_filename_list, contract_identifier):
    selected_contract_fileinfo = {}
    for api_contract_filename in api_contract_filename_list:
        if contract_identifier == api_contract_filename:
            selected_contract_fileinfo['filename'] = api_contract_filename
            selected_contract_fileinfo['index'] = api_contract_filename_list.index(api_contract_filename)
    return selected_contract_fileinfo


# apiContractAccessor retrieves critical data from the selected contract and returns it in a prepared format
# example: selected_api_contract_data = apiContractAccessor(selected_contract_fileinfo, contract_data_array)
def apiContractAccessor(selected_contract_fileinfo, contract_data_array):
    # get data from the api contract file
    selected_api_contract_data = contract_data_array[selected_contract_fileinfo['index']]
    return selected_api_contract_data


# load_api_calls ~ reads in folder of request body .json files and returns array of filenames and filecontent
# filepath_token = r'\Users\Joseph\PycharmProjects\ebay_api\token.txt'
# filepath_body = r'C:\Users\Joseph\PycharmProjects\ebay_api\request_payload.json'
# api_calls_dir = r'C:\Users\Joseph\PycharmProjects\ebay_api\'
def get_api_call_filename_list(api_calls_dir):
    api_call_filename_list = [f for f in listdir(api_calls_dir) if isfile(join(api_calls_dir, f))]
    # Get JSON body of inventory item from local file (put this on google sheet, get with gsheet api?)
    return api_call_filename_list


# load_api_calls retrieves the data content of the api calls specified in api_call_filename_list
def load_api_calls(api_calls_dir, api_call_filename_list):
    call_data_array = []
    for api_call_file in api_call_filename_list:
        currentPath = api_calls_dir + "\\" + api_call_file
        # print(currentPath)
        call_data_array.append(open(currentPath).read())
    return call_data_array


# apiCallSelector selects an api call to prepare based on caller function
#   returns a filename and data of file from bigger array based on matching call_identifier
# Variables:
#   call_data_array is the data of the file
#   api_call_filename_list is the file name (1:1 ratio with call_data_array)
#   call_identifier is the api call identifier (should be almost same as file name)
def apiCallSelector(api_call_filename_list, call_identifier):
    selected_call_fileinfo = {}
    for api_call_filename in api_call_filename_list:
        if call_identifier == api_call_filename:
            selected_call_fileinfo['filename'] = api_call_filename
            selected_call_fileinfo['index'] = api_call_filename_list.index(api_call_filename)
    return selected_call_fileinfo
