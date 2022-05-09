import xml.etree.ElementTree as ET
from datetime import datetime
import pandas as pd

# function for parsing relevant information from those +150,000 XML files
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
    print(data_df)


parsing_words('2532889X/1946/04/23/01/presentation/2532889X_1946-04-23_01_001.xml')











'''
# reading in a single XML file
tree = ET.parse('2532889X/1946/04/23/01/presentation/2532889X_1946-04-23_01_001.xml')
root = tree.getroot()

# getting the metatdata on the publishing date and page
metadata = root[2][0].attrib.get('ID')
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
print(data_df)

# counting occurance of words while converting list into a dictionary
# it's more playing around than an approach, since the words aren't lemmatised yet
dict_of_words = dict()
for word in contents:
    dict_of_words[word] = dict_of_words.get(word, 0) + 1         # counting how often each word occures on the same page
'''

# ToDo: converting code to a function and iterate over all XML files
# ToDo: deleting missspelled words and stop words