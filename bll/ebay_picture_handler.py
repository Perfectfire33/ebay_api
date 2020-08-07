import json
import os
import bll.ebay_object_headers

# This file handles ebay pictures


# creates folders with the box_name from stage2 in ebay_item_inventory in the pictures directory in ebay-config-data
def createPictureFolders(configDataSet, appDataSet2):
    print("createPictureFolders")
    headers2 = bll.ebay_object_headers.get_headers_data_ii()
    # Import config Picture Folder
    picture_folder = configDataSet[0][8][2]
    print("picture_folder")
    print(picture_folder)
    # Import JSON header-data matched object
    vjson = bll.ebay_object_receiver.loadJsonData(appDataSet2, headers2)
    k = 0
    while k < len(vjson[0]):
        os.mkdir(picture_folder + vjson[0][k]['box_name'])
        print(vjson[0][k]['box_name'])
        k = k + 1


#def getPictureFilepaths():

#1|create picture folders
#2|put pictures in folders
#3|get picture filepaths for each folder where folderName = box_name
#3.5| host pictures on webserver so we can get a public url with the image
#3.7| generate list of http:\\ locations of each image for each box_name
def get_picture_folder_dirs(configDataSet):
    print("get_picture_folder_dirs")
    folders = []
    picture_folder = configDataSet[0][8][2]
    #picture_folder = r'C:\Users\Public\EBAY\EBAY_PICTURES\pictures'
    for folder in os.listdir(picture_folder):
        folders.append(folder)

    return folders

def get_picture_folder_and_filepath(configDataSet):
    folders = get_picture_folder_dirs(configDataSet)
    folder_list = []
    #picture_dir = r'C:\Users\Public\EBAY\EBAY_PICTURES\pictures'
    picture_dir = configDataSet[0][8][2]
    #img_dict = {}
    for current_folder in folders:
        #print("picture_dir current_folder")
        #print(picture_dir + "\\" + current_folder)
        #print(len(os.listdir(picture_dir + "\\" + current_folder)))
        img_array = []
        img_dict = {}
        for img in os.listdir(picture_dir + "\\" + current_folder):
            if img != 'Thumbs.db':
                img_array.append(img)
        img_dict['folder_name']=current_folder
        img_dict['folder_data']=img_array
        folder_list.append(img_dict)

    return folder_list

#folder_list = get_path()
#print("folder_list")
#print(folder_list)

def create_url(configDataSet):
    img_dict = get_picture_folder_and_filepath(configDataSet)
    img_dict_dump = json.dumps(img_dict)
    img_dict_json = json.loads(img_dict_dump)
    i = 0
    #base_url = r'http://127.0.0.1:5000/pictures/'
    base_url = configDataSet[8][10][1]

    #print("len(img_dict_json)")
    #print(len(img_dict_json))
    #print(img_dict_json)

    folders_and_urls = []
    while i < len(img_dict_json):
        j = 0
        picture_url_list_all = {}
        picture_url_list = []
        folder_url = img_dict_json[i]['folder_name']
        #print("folder_url")
        #print(folder_url)
        while j < len(img_dict_json[i]['folder_data']):
            folder_data = img_dict_json[i]['folder_data'][j]
            #print("folder_data")
            #print(folder_data)
            folder_data_url = "/" + folder_data
            #print("complete_url")
            #print(base_url + folder_url + folder_data_url)
            complete_url = base_url + folder_url + folder_data_url
            picture_url_list.append(complete_url)
            j = j + 1
        picture_url_list_all['url_list'] = picture_url_list
        picture_url_list_all['item_folder'] = folder_url
        folders_and_urls.append(picture_url_list_all)
        i = i + 1

    return folders_and_urls

#4|in createOrReplaceInventoryItem, add list of picture urls for each item