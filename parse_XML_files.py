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
    contents = []
    for elem in root.iter():
        if elem.tag.split('}')[1] == "String":
            contents.append(elem.get('CONTENT'))

    # parsing the font size from the tags named "String", which contain "STYLEREFS" as an attribute
    fontsize = []
    for elem in root.iter():
        if elem.tag.split('}')[1] == "String":
            fontsize.append(elem.get('STYLEREFS'))

    # putting things together in a dataframe
    data_df = pd.DataFrame(list(zip(contents, fontsize)), columns =['single_word', 'fontsize'])

    # writing df into a csv-file containing the metadata as part of the file name
    data_df.to_csv('data/parsed_data/' + str(metadata_date) + '_' + str(metadata_page) +'.csv', index=None)


# making a list of all file paths that lead to XML files (except for the METS files)

all_paths = []
for root, directory_names,file_names in os.walk('data/2532889X'):
    for file in file_names:
        ismetsfile = re.search('.*mets\.xml', file)
        if not ismetsfile:
            all_paths.append(os.path.join(root, file))


# calling the parsing_words function on each element of all_paths
# this will result in creating a csv file for each page from each issue within the hidden folder "data/parsed_data"

didNotWork =[]

for path_to_file in all_paths:
    try:
        parsing_words(path_to_file)
    except:
        didNotWork.append(path_to_file)
