# Analytical look into a historical newspaper

The project aims to analyse newspaper articles released over a period of more than 44 years in former [East Germany](https://en.wikipedia.org/wiki/East_Germany).

## Data
The data this project is based on, is the full text of [Neues Deutschland](https://en.wikipedia.org/wiki/Neues_Deutschland), a propagandistic daily newspaper issued by [Socialist Unity Party of Germany](https://en.wikipedia.org/wiki/Socialist_Unity_Party_of_Germany) between April 1946 and October 1990.

The full text along with downloadable PDFs of [Neues Deutschland](https://en.wikipedia.org/wiki/Neues_Deutschland) and other historical newspapers is freely accessable via the digitalisation portal [ZEFYS](https://zefys.staatsbibliothek-berlin.de/?lang=en).

This is what the first issue looks like:
<image src="images/1946-23-04_Neues_Deutschland_p1.png"/>

For my analytical project the [Berlin State Library](https://en.wikipedia.org/wiki/Berlin_State_Library)'s department "Informations- und Datenmanagement" kindly provided me with the [METS](https://en.wikipedia.org/wiki/Metadata_Encoding_and_Transmission_Standard) and [XML]() files, so I could quickly start. Many thanks to Borries Jensen, who made this possible! 

This is what the heading from the first issue looks like within the XML file (you can find the single words along with information on their position and formatting):
<image src="images/1946-23-04_XML_Header.png"/>

Not publishing the recieved data is a legal requirement, which of cause I conform to. If you want to start a similar analysis however, I would convey you to the [StabiHacks](https://github.com/elektrobohemian/StabiHacks) tool on GitHub, created by the former head of the department "Informations- und Datenmanagement" David Zellhöfer.