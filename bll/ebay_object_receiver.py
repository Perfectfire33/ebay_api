import json
import bll.ebay_object_matcher

def createObjectsFromDataSet(appDataSet, headers):
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
        #print("all_header_groups[" + str(i) + "]")
        #print(all_header_groups[i])
        i = i + 1

    # reset i
    i = 0

    return all_header_groups



def matchDataWithHeaders(appDataSet, headers):
    # Put appDataSet values inside of ebay objects and print API calls (use configDataSet values for config settings)
    all_header_groups = createObjectsFromDataSet(appDataSet, headers)
    # print("all_header_groups")
    # print(all_header_groups)
    # then, call the api and send body data to it
    j = 0
    itemObject = {}
    curItemData = []
    itemData = []
    # appDataSet len is
    # print("len(appDataSet)")
    # print(len(appDataSet))
    # print(appDataSet)
    # BEGIN count Area (length of appDataSet)
    while j < len(appDataSet):
        for area in appDataSet[j]:
            k = 0
            # print(area)
            while k < len(area):
                # if all_header_groups[j][k]'s value is missing, do not assign an area
                if area[k] != '':
                    itemObject[all_header_groups[j][k]] = area[k]
                k = k + 1
            curItemData.append(itemObject)
            # reset itemObject
            itemObject = {}
        # END count Area (length of appDataSet)
        j = j + 1
        itemData.append(curItemData)
        # reset curItemData
        curItemData = []

    i = 0
    j = 0
    k = 0
    # now need to merge areas for each row together
    """
    [
        [ //area1
            { }, //row1
            { } //row2
        ],
        [ //area2
            { }, //row1
            { } //row2
        ]
    ]
    
    """
    #print("itemData")
    #print(itemData)
    #print("itemData[0]")
    #print(itemData[0])


    # returning the api call
    itemDataJson = json.dumps(itemData)
    return itemDataJson


def loadJsonData(appDataSet, headers):
    jsonDataWithHeaders = matchDataWithHeaders(appDataSet, headers)
    wjson = json.loads(jsonDataWithHeaders)
    #print("wjson")
    #print(wjson)
    #print("wjson[item_id]")
    #print(wjson[0][0]['item_id'])
    return wjson


