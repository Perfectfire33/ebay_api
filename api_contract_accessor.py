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
            requestBody:{ description:"", content:{ content_type: { schema:{ description:"", $ref:"" } } } },
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
    and
        paths.requestBody is only present for calls that have a request body

"""
# loads selected_api_contract_data into JSON-accessible format
def load_selected_api_contract_data(selected_api_contract_data):
    selected_api_contract_json = json.loads(selected_api_contract_data)
    return selected_api_contract_json

# retrieve list of currently selected API contract paths from loaded JSON format
# returns an array of path names
def get_contract_path_list(selected_api_contract_json):
    path_list = []
    for path in selected_api_contract_json['paths']:
        path_list.append(path)
    return path_list

def get_path_http_operation_list(selected_path, selected_api_contract_json):
    path_http_operation_list = []
    for http_operation in selected_api_contract_json['paths'][selected_path]:
        path_http_operation_list.append(http_operation)
    return path_http_operation_list

def get_endpoint_tag_list(selected_path, selected_http_operation, selected_api_contract_json):
    endpoint_tag_list = []
    for tag in selected_api_contract_json['paths'][selected_path][selected_http_operation]['tags']:
        endpoint_tag_list.append(tag)
    return endpoint_tag_list

def get_endpoint_description(selected_path, selected_http_operation, selected_api_contract_json):
    endpoint_description = selected_api_contract_json['paths'][selected_path][selected_http_operation]['description']
    return endpoint_description

def get_endpoint_operationId(selected_path, selected_http_operation, selected_api_contract_json):
    endpoint_operationId = selected_api_contract_json['paths'][selected_path][selected_http_operation]['operationId']
    return endpoint_operationId

def get_endpoint_parameter_list(selected_path, selected_http_operation, selected_api_contract_json):
    endpoint_parameter_list = selected_api_contract_json['paths'][selected_path][selected_http_operation]['parameters']
    return endpoint_parameter_list

def get_endpoint_response_list(selected_path, selected_http_operation, selected_api_contract_json):
    endpoint_responses_list = []
    for response in selected_api_contract_json['paths'][selected_path][selected_http_operation]['responses']:
        endpoint_responses_list.append(response)
    return endpoint_responses_list


def get_endpoint_response_description(selected_path, selected_http_operation, selected_response_code, selected_api_contract_json):
    endpoint_response_description = selected_api_contract_json['paths'][selected_path][selected_http_operation]['responses'][selected_response_code]['description']
    return endpoint_response_description




