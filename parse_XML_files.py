import xml.etree.ElementTree as ET
from datetime import datetime

# reading in a single XML file
tree = ET.parse('2532889X/1946/04/23/01/presentation/2532889X_1946-04-23_01_001.xml')
root = tree.getroot()

# getting the metatdata on the publishing date and page
metadata = root[2][0].attrib.get('ID')
metadata_date = datetime.strptime(root[2][0].attrib.get('ID').split('_')[3], '%Y-%m-%d').date()
metadata_page = int(root[2][0].attrib.get('ID').split('_')[4])

# parsing the single words from the tags named "String", which contain "CONTENT" as an attribute
contents = []                                   # initiating a list to store the words in
for elem in root.iter():
    if elem.tag.split('}')[1] == "String":
        contents.append(elem.get('CONTENT'))    #--> grows a list containing all the single words from the page of the newspaper

