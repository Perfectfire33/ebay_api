import ebay_api_connector
import simplejson as json






# retrieve list of currently selected API contract paths from loaded JSON format
# returns an array of path names
def getContractPaths(selected_api_contract_json):
    path_list = []
    for path in selected_api_contract_json['paths']:
        print("path")
        print(path)
        path_list.append(path)
    return path_list


# loads selected_api_contract_data into JSON-accessible format
def load_selected_api_contract_data(selected_api_contract_data):
    selected_api_contract_json = json.loads(selected_api_contract_data)
    return selected_api_contract_json