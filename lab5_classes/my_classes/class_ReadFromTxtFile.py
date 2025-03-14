from datetime import datetime
import re


# The structure of the txt file should be the next
# news
# "some
# text" "city"
#
# private ad
# "text" "2025/12/30"
class ReadFromTxtFile:
    def __init__(self, path):
        self.path = path

    @staticmethod
    def validate_date(date):
        if datetime.strptime(date, "%Y/%m/%d"):
            return date
        else:
            return datetime.strptime(date, "%Y/%m/%d")

    @staticmethod
    def extract_text_and_city(section_content):
        try:
            text, city = re.findall(r'"(.*?)"', ' '.join(section_content))

        except ValueError as e:
            print("The error happened when the text and city were separated from the content")

        return text, city

    @staticmethod
    def extract_text_and_date(section_content):
        try:
            text, date = re.findall(r'"(.*?)"', ' '.join(section_content))

        except ValueError as e:
            print("The error happened when the text and date were separated from the content")

        return text, date

    def process_section(self, section_name, section_content):

        section_data = {}

        if section_name == 'news':
            text, city = self.extract_text_and_city(section_content)
            section_data = {'text': text, 'city': city}

        if section_name == 'private ad':
            text, date = self.extract_text_and_date(section_content)
            section_data = {'text': text, 'date': self.validate_date(date)}

        return section_data

    def remove_file(self):
        import os
        if os.path.exists(self.path):
            os.remove(self.path)
            print(f"File {self.path} removed successfully.")
        else:
            print(f"File {self.path} not found.")

    def parse_file(self):
        sections = []
        section_name = ''
        section_content = []

        try:
            with open(self.path, 'r') as infile:
                lines = infile.readlines()

            for line in lines:

                line = line.strip()

                if line.lower() in ['news', 'private ad']:

                    if section_name:
                        # Process the previous section before switching to a new one
                        sections.append(
                            {section_name: self.process_section(section_name, section_content)})

                    section_name = line.lower()
                    section_content = []

                else:
                    section_content.append(line)

            # Process the last section after finishing the loop
            if section_name:
                sections.append(
                    {section_name: self.process_section(section_name, section_content)})

            self.remove_file()
            return sections

        except Exception as e:
            print(f"Some file processing error happened: {e}")