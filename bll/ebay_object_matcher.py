import bll.dal.api_local_file_accessor

# this file matches ebay data to ebay objects
# sends objects out to api_call_sequencer file

# call_ebay_api gets api data, finds the appropriate api call set based on "script runtime" config area
# and will apply the "script runtime" to each row in the selected Google Sheet Area
# and will return an api response
def call_ebay_api(configDataSet, appDataSet):

    # Get data from "Script Runtime" Area
    print("configDataSet[1][0][1]")
    print(configDataSet[1][0][1])
    scriptRuntimeData = {}
    scriptRuntimeData[configDataSet[1][0][0]]=configDataSet[1][0][1]
    print("scriptRuntimeData")
    print(scriptRuntimeData[1][0][1])
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