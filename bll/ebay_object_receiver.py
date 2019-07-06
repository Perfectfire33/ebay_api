
def createObjectsFromDataSet(appDataSet):
    # need to define object headers
    headers = []
    headers.append('item_id')
    headers.append('item_title')
    headers.append('item_category')
    headers.append('item_condition')
    headers.append('item_condition_description')
    headers.append('item_price')
    headers.append('item_qty')
    headers.append('packed_item_weight_lb')
    headers.append('packed_item_weight_oz')
    headers.append('packed_item_height')
    headers.append('packed_item_length')
    headers.append('packed_item_depth')

    # group of headers
    header_group_ct = []
    # groups of group of headers
    all_header_groups = []
    # switch var -- only run once for each group
    append_new_group = 0
    # for each group of columns in the incoming data set:
    for selected_columns in appDataSet:
        #print("selected_columns")
        #print(selected_columns)
        # only run once for each group -- turn on
        append_new_group = 1

        for column in selected_columns:
            # print("column")
            # print(column)
            # print("len(column)")
            # print(len(column))
            if append_new_group == 1:
                header_group_ct.append(len(column))

            # turn off after once run
            append_new_group = 0

    # print("header_group_ct")
    # print(header_group_ct)
    i_v = 0
    for set_of_headers in header_group_ct:
        # reset i_a counter
        i_a = 1
        # reset temp header holder
        header_group = []
        while i_a <= set_of_headers:
            # print("i_a: " + str(i_a) + "   " + "set_of_headers: " + str(set_of_headers))
            header_group.append(headers[i_v])
            i_v = i_v + 1
            i_a = i_a + 1
        # reset i_a
        i_a = 1
        all_header_groups.append(header_group)

    # Print all groups, then each group separately
    #print("all_header_groups")
    #print(all_header_groups)
    i = 0
    while i < all_header_groups.__len__():
        print("all_header_groups[" + str(i) + "]")
        print(all_header_groups[i])
        i = i + 1

    # reset i
    i = 0

    return all_header_groups














# set to first group of columns
# column_group_ct = 0

# ebay incoming object row
# inventory_row = {}

# get number of rows to get this header
# rows = len(dataSet[column_group_ct])

# select first column
# column = 0

# get number of columns in this group of columns
# columns = len(dataSet[column_group])

# for row in rows:
#         for header in headers:
#             inventory_row[header] = dataSet[column_group_ct][row][column]


"""
{
 column_group1 : {
    
 
 }
}

"""

"""

set header row in config file and read in headers
maybe convert to lower case and add _ in place of spaces
for generic google sheet scripts:
    make header a yes/no optional
    allow for multiple header rows (or areas within same row)

"""