import xml.etree.ElementTree as ET
from datetime import datetime
import pandas as pd
import os
import re

# function for parsing relevant information from each of those 119,956 XML files
def parsing_words(path):

    # reading in a single XML file
    tree = ET.parse(path)
    root = tree.getroot()

    # getting the metatdata on the publishing date and page
    metadata_date = datetime.strptime(root[2][0].attrib.get('ID').split('_')[3], '%Y-%m-%d').date()
    metadata_page = int(root[2][0].attrib.get('ID').split('_')[4])

    # parsing the single words from the tags named "String", which contain "CONTENT" as an attribute
    contents = []                                                    # initiating a list to store the words in
    for elem in root.iter():
        if elem.tag.split('}')[1] == "String":
            contents.append(elem.get('CONTENT'))                     #--> grows a list containing all the single words from the page of the newspaper

    # putting things together in a dataframe
    data_df = pd.DataFrame(contents, columns =['single_word'])
    data_df['date'] = metadata_date 
    data_df['page'] = metadata_page
    
    # writing df into a csv-file containing the metadata as part of the file name
    data_df.to_csv('parsed_data/' + str(metadata_date) + '_' + str(metadata_page) +'data.csv', index=None)

# making a list of all file paths that lead to XML files (except for the METS files)
all_paths = []
for root, directory_names,file_names in os.walk('2532889X'):
    for file in file_names:
        ismetsfile = re.search('.*mets\.xml', file)
        if not ismetsfile:
            all_paths.append(os.path.join(root, file))

# calling the parsing_words function on each element of all_paths
# this will result in creating a csv file for each page from each issue within the hidden folder "parsed_data"
didNotWork =[]

for path_to_file in all_paths:
    try:
        parsing_words(path_to_file)
    except:
        didNotWork.append(path_to_file)