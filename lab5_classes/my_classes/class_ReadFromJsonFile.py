# JSON type that can be parsed
# {
#   "data":[
#     {
#       "type": "news",
#       "text": "text news",
#       "city": "city json"
#     },
#     {
#       "type": "private ad",
#       "text": "text private ad",
#       "date": "2025/06/06"
#     }
#   ]
# }
# or
# {
# "type": "private ad",
# "text": "text private ad",
# "date": "2025/06/06"
# }


import json
from .class_ReadFromTxtFile import ReadFromTxtFile


class ReadFromJsonFile(ReadFromTxtFile):
    def __init__(self, path):
        super().__init__(path)
        self.path = path

    @staticmethod
    def parse_section(section_data):
        section = {}
        try:
            if "type" in section_data:
                if section_data["type"].lower() == 'news':
                    section[section_data["type"].lower()] = {'text': section_data['text'], 'city': section_data['city']}
                elif section_data["type"].lower() == 'private ad':
                    section[section_data["type"].lower()] = {'text': section_data['text'],
                                                             'date': ReadFromTxtFile.validate_date(section_data['date'])
                                                             }
                return section
        except Exception as e:
            print(f"Some item processing error happened: {e} for the next item \n {section_data}")

    def parse_file(self):
        sections = []
        try:
            with open(self.path, 'r') as json_file:
                content = json.load(json_file)

                if "data" in content:
                    for item in content["data"]:

                        sections.append(self.parse_section(item))
                else:
                    sections.append(self.parse_section(content))

            ReadFromTxtFile.remove_file(self)

            return sections

        except Exception as e:
            print(f"Some file processing error happened: {e}")






