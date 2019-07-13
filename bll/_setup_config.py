import bll.gsheets_api_connector
import bll.dal.api_local_file_accessor
import bll.dal.api_sequencer
"""
This Script specifies the google sheet and data for all config data
01  Run This First  01
"""

def getGoogleSheetDataSet(data_set_type, data_set_data):
    print("\n")
    print("-------------- Start getGoogleSheetDataSet " + data_set_type + " Script ------------------")
    print("-------------- Get Sheet Area Info & Retrieve Sheet Data  -----------------")
    print("\n")
    configData = []
    if data_set_type == "config":
        # Get Config Data
        configData = bll.gsheets_api_connector.readConfigFile()

    if data_set_type == "app":
        # Get Config Data and do stuff to break out the configData p1 through p7 of the correct profile
        scopes = data_set_data[2][0][1]
        tokenPath = data_set_data[2][1][1]
        acceptableFields_profileName = data_set_data[2][2][1]
        spreadsheet_name = data_set_data[2][3][1]
        speadsheet_id = data_set_data[2][4][1]
        sheet_name = data_set_data[2][5][1]
        sheet_cell_xy_sets = []
        rows = data_set_data[3]
        for row in rows:
            temp1 = row[0] + "," + row[1]
            sheet_cell_xy_sets.append(temp1)
        configData.append(scopes)
        configData.append(tokenPath)
        configData.append(acceptableFields_profileName)
        configData.append(spreadsheet_name)
        configData.append(speadsheet_id)
        configData.append(sheet_name)
        configData.append(sheet_cell_xy_sets)

    if data_set_type == "app2":
        # Get Config Data and do stuff to break out the configData p1 through p7 of the correct profile
        scopes = data_set_data[4][0][1]
        tokenPath = data_set_data[4][1][1]
        acceptableFields_profileName = data_set_data[4][2][1]
        spreadsheet_name = data_set_data[4][3][1]
        speadsheet_id = data_set_data[4][4][1]
        sheet_name = data_set_data[4][5][1]
        sheet_cell_xy_sets = []
        rows = data_set_data[5]
        for row in rows:
            temp1 = row[0] + "," + row[1]
            sheet_cell_xy_sets.append(temp1)
        configData.append(scopes)
        configData.append(tokenPath)
        configData.append(acceptableFields_profileName)
        configData.append(spreadsheet_name)
        configData.append(speadsheet_id)
        configData.append(sheet_name)
        configData.append(sheet_cell_xy_sets)

    if data_set_type == "app3":
        # Get Config Data and do stuff to break out the configData p1 through p7 of the correct profile
        scopes = data_set_data[6][0][1]
        tokenPath = data_set_data[6][1][1]
        acceptableFields_profileName = data_set_data[6][2][1]
        spreadsheet_name = data_set_data[6][3][1]
        speadsheet_id = data_set_data[6][4][1]
        sheet_name = data_set_data[6][5][1]
        sheet_cell_xy_sets = []
        rows = data_set_data[7]
        for row in rows:
            temp1 = row[0] + "," + row[1]
            sheet_cell_xy_sets.append(temp1)
        configData.append(scopes)
        configData.append(tokenPath)
        configData.append(acceptableFields_profileName)
        configData.append(spreadsheet_name)
        configData.append(speadsheet_id)
        configData.append(sheet_name)
        configData.append(sheet_cell_xy_sets)

    # Set current Config Data Params
    p1=configData[0]
    p2=configData[1]
    p3=configData[2]
    p4=configData[3]
    p5=configData[4]
    p6=configData[5]
    p7=configData[6]
    """
    configData[0] = scopes
    configData[1] = tokenPath
    configData[2] = acceptableFields_profileName
    configData[3] = spreadsheet_name
    configData[4] = spreadsheet_id
    configData[5] = sheet_name
    configData[6] = sheet_cell_xy_sets
    """
    # Acquire List of Acceptable Fields (Areas in Google Sheets to grab data from)
    listOfAcceptableFields = bll.gsheets_api_connector.getAcceptableFields(p3, p4, p5, p6, p7)

    # Acquire Set of Google Sheet Data
    dataSet = bll.gsheets_api_connector.getDataSet(p1, p2, listOfAcceptableFields)
    return dataSet






# TODO
# TODO
def writeGoogleSheetDataSet(data_set_type, data_set_data):
    print("\n")
    print("-------------- Start getGoogleSheetDataSet " + data_set_type + " Script ------------------")
    print("-------------- Write Sheet Area Info & Retrieve Written Sheet Data  -----------------")
    print("\n")
    configData = []
    if data_set_type == "config":
        # Get Config Data
        configData = bll.gsheets_api_connector.readConfigFile()

    if data_set_type == "app":
        # Get Config Data and do stuff to break out the configData p1 through p7 of the correct profile
        scopes = data_set_data[2][0][1]
        tokenPath = data_set_data[2][1][1]
        acceptableFields_profileName = data_set_data[2][2][1]
        spreadsheet_name = data_set_data[2][3][1]
        speadsheet_id = data_set_data[2][4][1]
        sheet_name = data_set_data[2][5][1]
        sheet_cell_xy_sets = []
        rows = data_set_data[3]
        for row in rows:
            temp1 = row[0] + "," + row[1]
            sheet_cell_xy_sets.append(temp1)
        configData.append(scopes)
        configData.append(tokenPath)
        configData.append(acceptableFields_profileName)
        configData.append(spreadsheet_name)
        configData.append(speadsheet_id)
        configData.append(sheet_name)
        configData.append(sheet_cell_xy_sets)

    if data_set_type == "app2":
        # Get Config Data and do stuff to break out the configData p1 through p7 of the correct profile
        scopes = data_set_data[4][0][1]
        tokenPath = data_set_data[4][1][1]
        acceptableFields_profileName = data_set_data[4][2][1]
        spreadsheet_name = data_set_data[4][3][1]
        speadsheet_id = data_set_data[4][4][1]
        sheet_name = data_set_data[4][5][1]
        sheet_cell_xy_sets = []
        rows = data_set_data[5]
        for row in rows:
            temp1 = row[0] + "," + row[1]
            sheet_cell_xy_sets.append(temp1)
        configData.append(scopes)
        configData.append(tokenPath)
        configData.append(acceptableFields_profileName)
        configData.append(spreadsheet_name)
        configData.append(speadsheet_id)
        configData.append(sheet_name)
        configData.append(sheet_cell_xy_sets)

    if data_set_type == "app3":
        # Get Config Data and do stuff to break out the configData p1 through p7 of the correct profile
        scopes = data_set_data[6][0][1]
        tokenPath = data_set_data[6][1][1]
        acceptableFields_profileName = data_set_data[6][2][1]
        spreadsheet_name = data_set_data[6][3][1]
        speadsheet_id = data_set_data[6][4][1]
        sheet_name = data_set_data[6][5][1]
        sheet_cell_xy_sets = []
        rows = data_set_data[7]
        for row in rows:
            temp1 = row[0] + "," + row[1]
            sheet_cell_xy_sets.append(temp1)
        configData.append(scopes)
        configData.append(tokenPath)
        configData.append(acceptableFields_profileName)
        configData.append(spreadsheet_name)
        configData.append(speadsheet_id)
        configData.append(sheet_name)
        configData.append(sheet_cell_xy_sets)

    if data_set_type == "app4":
        # Get Config Data and do stuff to break out the configData p1 through p7 of the correct profile
        scopes = data_set_data[6][0][1]
        tokenPath = data_set_data[6][1][1]
        acceptableFields_profileName = data_set_data[6][2][1]
        spreadsheet_name = data_set_data[6][3][1]
        speadsheet_id = data_set_data[6][4][1]
        sheet_name = data_set_data[6][5][1]
        sheet_cell_xy_sets = []
        rows = data_set_data[7]
        for row in rows:
            temp1 = row[0] + "," + row[1]
            sheet_cell_xy_sets.append(temp1)
        configData.append(scopes)
        configData.append(tokenPath)
        configData.append(acceptableFields_profileName)
        configData.append(spreadsheet_name)
        configData.append(speadsheet_id)
        configData.append(sheet_name)
        configData.append(sheet_cell_xy_sets)


    # Set current Config Data Params
    p1=configData[0]
    p2=configData[1]
    p3=configData[2]
    p4=configData[3]
    p5=configData[4]
    p6=configData[5]
    p7=configData[6]
    """
    configData[0] = scopes
    configData[1] = tokenPath
    configData[2] = acceptableFields_profileName
    configData[3] = spreadsheet_name
    configData[4] = spreadsheet_id
    configData[5] = sheet_name
    configData[6] = sheet_cell_xy_sets
    """
    # Acquire List of Acceptable Fields (Areas in Google Sheets to grab data from)
    listOfAcceptableFields = bll.gsheets_api_connector.getAcceptableFields(p3, p4, p5, p6, p7)

    # Acquire Set of Google Sheet Data
    dataSet = bll.gsheets_api_connector.writeDataSet(p1, p2, listOfAcceptableFields, bodyData)
    return dataSet