import bll.dal.api_contract_accessor
import bll.dal.api_contract_access_tests
import bll.dal.api_local_file_accessor

#   This should eventually be set in config file
#   JOSEPH-PC:          api_calls_dir = r'C:\Users\Joseph\PycharmProjects\ebay_api\api_calls'
#   DICK-PC:            api_calls_dir = r'C:\Users\dick\Documents\GitHub\ebay_api\api_calls'
#   WIN-UJAOO6FHEGF:    api_calls_dir = r'C:\Users\Joseph\Documents\GitHub\ebay_api\api_calls'
# repo_path = r'C:\Users\Joseph\Documents\GitHub'
repo_path = r'C:\Users\dick\Documents\GitHub'

# Set api contract file directory
api_contract_dir = repo_path + r'\ebay_api\api_contracts'
# Get list of api contract filenames within directory
api_contract_filename_list = bll.dal.api_local_file_accessor.get_api_contract_filename_list(api_contract_dir)

# print("api_contract_filename_list")
# print(api_contract_filename_list)

# contract_data_array is an array of all the JSON contract bodies (or data of the files in the api_contracts folder)
contract_data_array = bll.dal.api_local_file_accessor.load_api_contracts(api_contract_dir, api_contract_filename_list)
# print("contract_data_array.0")
# print(contract_data_array[0])
contract_identifier = 'sell_inventory_v1_oas3.json'
selected_contract_fileinfo = bll.dal.api_local_file_accessor.apiContractSelector(api_contract_filename_list, contract_identifier)

# print("selected_contract_fileinfo")
# print(selected_contract_fileinfo)
# print("selected_contract_fileinfo")

selected_api_contract_data = bll.dal.api_local_file_accessor.apiContractAccessor(selected_contract_fileinfo, contract_data_array)




# loads selected_api_contract_data into JSON-accessible format
selected_api_contract_json = api_contract_accessor.load_selected_api_contract_data(selected_api_contract_data)

built_api_call = api_contract_access_tests.api_contract_access_tests(selected_api_contract_data)
