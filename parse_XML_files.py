import xml.etree.ElementTree as ET

# reading in a single XML file
tree = ET.parse('2532889X/1946/04/23/01/presentation/2532889X_1946-04-23_01_001.xml')
root = tree.getroot()

# parsing all the attributes from the tags named "String", because these hold the content
attributes_holding_content = []
for elem in root.iter():
    print(elem.tag.split('}')[1])
    if elem.tag.split('}')[1] == "String":
        print("contains content")
        attributes_holding_content.append(elem.attrib)    #--> it grows a list containing a dicts

print(attributes_holding_content)