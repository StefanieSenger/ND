# Analytical look into a historical newspaper

The project aims to analyse (and play with) newspaper articles released over a period of more than 44 years in former [East Germany](https://en.wikipedia.org/wiki/East_Germany). This setting is suitable for trying out several ideas.

## Data
The data this project is based on, are articles from [Neues Deutschland](https://en.wikipedia.org/wiki/Neues_Deutschland), a propagandistic daily newspaper issued by [Socialist Unity Party of Germany](https://en.wikipedia.org/wiki/Socialist_Unity_Party_of_Germany) between April 1946 and October 1990.

The full text along with downloadable PDFs of [Neues Deutschland](https://en.wikipedia.org/wiki/Neues_Deutschland) and other historical newspapers is freely accessable via the digitalisation portal [ZEFYS](https://zefys.staatsbibliothek-berlin.de/?lang=en).

This is what the first issue dated April 23rd 1946 looks like:
<image src="images/1946-23-04_Neues_Deutschland_p1.png"/>

The [Berlin State Library](https://en.wikipedia.org/wiki/Berlin_State_Library)'s department "Informations- und Datenmanagement" kindly provided me with the [METS](https://en.wikipedia.org/wiki/Metadata_Encoding_and_Transmission_Standard) and [XML]() files. Many thanks to Borries Jensen, who made this possible!

This is what the heading from the first issue looks like within the XML file (you can find the single words in the CONTENT="xxx" attribute along with information on their position and formatting):
<image src="images/1946-23-04_XML_Header.png"/>

The METS files hold some metadata that make +100,000 XML files, each containing information on a single page, relatable to each other.

Not publishing the received data is a legal requirement, which I signed and which of cause I conform to. If you want to start a similar project however, I would convey you to the [StabiHacks](https://github.com/elektrobohemian/StabiHacks) tool on GitHub, created by the former head of the department "Informations- und Datenmanagement" David Zellhöfer.

### Data Extraction
To process the contents, I retrieved the single words from the XML files and linked them to the corresponding metadata (publishing date, page) using Python's [Element Tree Module](https://docs.python.org/3/library/xml.etree.elementtree.html). Then, I iterated this process over all of the XML files. Walking recursively over all sub-folders is necessary, because the hierarchy of the data folder looks like this:

<image src="images/Screenshot_from_2022-05-11_23-56-46.png" width="200"/>

Then I was left with 119.425 csv files, that each contained all the words from a single newspaper page and the information about their font size. I used the font size to extract headings and assigning them to their article.
