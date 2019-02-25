import ebay_api_connector
import simplejson as json

"""
Structure of Inventory API OpenAPI JSON Contract:
    { 
        openapi:"openapi version",
        info:{ title, description, contact:{ name:"" }, license, version},
        servers:[ url, description, variables:{ basePath:{ default:"" } } ],
        paths:{ "path_name":{ "http_type":{ 
            tags:[], 
            description:"", 
            operationId:"", 
            parameters:[ name:"", in:"", description:"", required:"", schema:{ type:"" } ], 
            responses:{ response_code:{ description:"", content:{ content_type:{ schema:{ $ref:"" } } } } } 
        }, 
        components:{ schemas:{ schema_name:{ }, securitySchemas: { api_auth: { type:"", description:"", flows:{ authorizationCode:{ authorizationUrl:"", tokenUrl:"", scopes:{ scope_list:"" } } } } } }
    }
    where
        path_name is <create function to return list of paths>
        http_type is "get", "put", "post", "delete"
        response_code is "200", "400", "404", "500"
        content_type is "application/json"
        schema_name is <create function to return list of schemas>
        scope_name is <create function to return list of scopes>

"""

# loads selected_api_contract_data into JSON-accessible format
def load_selected_api_contract_data(selected_api_contract_data):
    selected_api_contract_json = json.loads(selected_api_contract_data)
    return selected_api_contract_json


# retrieve list of currently selected API contract paths from loaded JSON format
# returns an array of path names
def getContractPaths(selected_api_contract_json):
    path_list = []
    for path in selected_api_contract_json['paths']:
        # print("path")
        # print(path)
        path_list.append(path)
    return path_list




# def getContractP







