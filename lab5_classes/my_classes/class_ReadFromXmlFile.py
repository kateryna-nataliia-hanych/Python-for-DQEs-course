# example of xml file
# <news-feed>
#     <publication type="news">
#         <text>some text</text>
#         <city>Lviv</city>
#     </publication>
#     <publication type="private ad">
#         <text>I don't sell something</text>
#         <expiration-date>2025/06/09</expiration-date>
#     </publication>
# </news-feed>

import xml.etree.ElementTree as ET
from .class_ReadFromTxtFile import ReadFromTxtFile


class ReadFromXmlFile(ReadFromTxtFile):
    def __init__(self, path):
        super().__init__(path),
        self.path = path

    @staticmethod
    def parse_section(section_data):
        section = {}

        try:
            type = str(section_data.get('type')).lower()

            if type == 'news':
                section[type] = {'text': section_data.find('text').text, 'city': section_data.find('city').text}
            elif type == 'private ad':
                section[type] = {'text': section_data.find('text').text, 'date': section_data.find('expiration-date').text}
            return section

        except Exception as e:
            print(f"Some item processing error happened: {e} for the next item \n {ET.dump(section_data)}")

    def parse_file(self):
        sections = []
        try:
            xml_file = ET.parse(self.path)
            root = xml_file.getroot()

            for section in root.iter('publication'):

                sections.append(self.parse_section(section))

            ReadFromTxtFile.remove_file(self)

            return sections

        except Exception as e:
            print(f"Some file processing error happened: {e}")


