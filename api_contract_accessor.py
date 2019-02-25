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


def get_contract_intel(selected_api_contract_json):
    contract_intel = {}
    contract_intel['api_name'] = selected_api_contract_json['info']['title']
    server_list = []
    server_data = {}
    for server in selected_api_contract_json['servers']:
        server_data['api_server_url'] = selected_api_contract_json['servers'][selected_api_contract_json['servers'].index(server)]['url']
        server_data['api_server_base_path'] = selected_api_contract_json['servers'][selected_api_contract_json['servers'].index(server)]['variables']['basePath']['default']
        server_list.append(server_data)

    contract_intel['server_list'] = server_list

    return contract_intel



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

def get_endpoint_response_content(selected_path, selected_http_operation, selected_response_code, selected_api_contract_json):
    if 'content' in selected_api_contract_json['paths'][selected_path][selected_http_operation]['responses'][selected_response_code]:
        endpoint_response_content = selected_api_contract_json['paths'][selected_path][selected_http_operation]['responses'][selected_response_code]['content']
    else:
        endpoint_response_content = "no response content present"

    return endpoint_response_content


def get_endpoint_request_body(selected_path, selected_http_operation, selected_api_contract_json):
    if 'requestBody' in selected_api_contract_json['paths'][selected_path][selected_http_operation]:
        endpoint_request_body = selected_api_contract_json['paths'][selected_path][selected_http_operation]['requestBody']
    else:
        endpoint_request_body = "no request body present"
    return endpoint_request_body


def get_component_schema_list(selected_api_contract_json):
    component_schema_list = []
    for schema in selected_api_contract_json['components']['schemas']:
        component_schema_list.append(schema)
    return component_schema_list


def get_component_schema_data(selected_schema, selected_api_contract_json):
    component_schema_data = selected_api_contract_json['components']['schemas'][selected_schema]
    return component_schema_data



def get_security_scheme(selected_api_contract_json):
    security_scheme = {}
    security_scheme['authUrl'] = selected_api_contract_json['components']['securitySchemes']['api_auth']['flows']['authorizationCode']['authorizationUrl']
    security_scheme['tokenUrl'] = selected_api_contract_json['components']['securitySchemes']['api_auth']['flows']['authorizationCode']['tokenUrl']
    scope_list = []
    for scope in selected_api_contract_json['components']['securitySchemes']['api_auth']['flows']['authorizationCode']['scopes']:
        scope_list.append(scope)

    security_scheme['scopeList'] = scope_list

    return security_scheme








