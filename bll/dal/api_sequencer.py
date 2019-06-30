import bll.ebay_api_connector
import bll.dal.api_local_file_accessor






# callSequence reads in a sequence file and returns an array of call names and call data
def callSequence(callSequenceFile, api_call_filename_list, api_calls_dir):
    # get list of call names from file
    call_sequence = tuple(open(callSequenceFile, 'r'))
    # get all call data at once
    call_data_array = bll.dal.api_local_file_accessor.load_api_calls(api_calls_dir, api_call_filename_list)
    # create array for fileinfo
    call_sequence_set_fileinfo = []
    # create array for data of files in sequence set
    call_sequence_set_filedata = []

    # loop for each api call in the api call sequence
    for call_identifier in call_sequence:
        # select the index from the file name array and match it to the index of the data array
        s_call_identifer = call_identifier.split("\n")
        # select what call from pool of calls that match the current call in the sequence
        selected_call_fileinfo = bll.dal.api_local_file_accessor.apiCallSelector(api_call_filename_list, s_call_identifer[0])
        # add the filename and index of current selected call to filename array
        call_sequence_set_fileinfo.append(selected_call_fileinfo)
        call_sequence_set_filedata.append(call_data_array[selected_call_fileinfo['index']])

    # create array of filepaths and filedata
    call_sequence_set = []
    call_sequence_set.append(call_sequence_set_fileinfo)
    call_sequence_set.append(call_sequence_set_filedata)
    call_sequence_with_dir = {}
    call_sequence_with_dir['call_sequence_set'] = call_sequence_set
    call_sequence_with_dir['api_calls_dir'] = api_calls_dir

    return call_sequence_with_dir


# executeCallSequenceFile takes the prepared call_sequence_with_dir and executes each call against the API and
#   returns an array of api responses
def executeCallSequenceFile(call_sequence_with_dir):
    print('test')
    # For each call in call sequence,
    # identify appropriate function based on call name,
    #   (potentially need to build a table that maps the file call name to API call name if they are to differ)
    # execute the function to get that api's response,
    # and add the whole response to an array of responses
    #   (will need to then parse the response in another function and use that data based on call success or error)
    print('test')



# parseExecutedCallSequence takes the executed_call_sequence and takes action based on each call's response
def parseExecutedCallSequence(executed_call_sequence):
    print('test')
    # AA
    # AA
    print('test')