import api_contract_accessor


def api_contract_access_tests(selected_api_contract_data):
    # loads selected_api_contract_data into JSON-accessible format
    selected_api_contract_json = api_contract_accessor.load_selected_api_contract_data(selected_api_contract_data)

    api_contract_base_path = selected_api_contract_json['servers'][0]['variables']['basePath']['default']

    # retrieve list of currently selected API contract paths
    path_list = api_contract_accessor.get_contract_path_list(selected_api_contract_json)
    print("path_list")
    print(path_list)

    selected_path = path_list[0]

    http_operation_list = api_contract_accessor.get_path_http_operation_list(selected_path, selected_api_contract_json)
    print("http_operation_list")
    print(http_operation_list)

    selected_http_operation = http_operation_list[1]

    endpoint_tag_list = api_contract_accessor.get_endpoint_tag_list(selected_path, selected_http_operation, selected_api_contract_json)
    print("endpoint_tag_list")
    print(endpoint_tag_list)

    endpoint_description = api_contract_accessor.get_endpoint_description(selected_path, selected_http_operation, selected_api_contract_json)
    print("endpoint_description")
    print(endpoint_description)

    endpoint_operationId = api_contract_accessor.get_endpoint_operationId(selected_path, selected_http_operation, selected_api_contract_json)
    print("endpoint_operationId")
    print(endpoint_operationId)

    endpoint_parameter_list = api_contract_accessor.get_endpoint_parameter_list(selected_path, selected_http_operation, selected_api_contract_json)
    print("endpoint_parameter_list")
    print(endpoint_parameter_list)

    endpoint_responses_list = api_contract_accessor.get_endpoint_response_list(selected_path, selected_http_operation, selected_api_contract_json)
    print("endpoint_responses_list")
    print(endpoint_responses_list)

    selected_response_code = endpoint_responses_list[1]

    endpoint_response_description = api_contract_accessor.get_endpoint_response_description(selected_path, selected_http_operation, selected_response_code, selected_api_contract_json)
    print("endpoint_response_description")
    print(endpoint_response_description)


    endpoint_response_content = api_contract_accessor.get_endpoint_response_content(selected_path, selected_http_operation, selected_response_code, selected_api_contract_json)
    print("endpoint_response_content")
    print(endpoint_response_content)


    endpoint_request_body = api_contract_accessor.get_endpoint_request_body(selected_path, selected_http_operation, selected_api_contract_json)
    print("endpoint_request_body")
    print(endpoint_request_body)


    component_schema_list = api_contract_accessor.get_component_schema_list(selected_api_contract_json)
    print("component_schema_list")
    print(component_schema_list)

    selected_schema = component_schema_list[2]
    component_schema_data = api_contract_accessor.get_component_schema_data(selected_schema, selected_api_contract_json)
    print("component_schema_data")
    print(component_schema_data)

    security_scheme = api_contract_accessor.get_security_scheme(selected_api_contract_json)
    print("security_scheme")
    print(security_scheme)

    contract_intel = api_contract_accessor.get_contract_intel(selected_api_contract_json)
    print("contract_intel")
    print(contract_intel)

    tests = "all tests completed"
    return tests

