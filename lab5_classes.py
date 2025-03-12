import csv
import re
from datetime import datetime
from lab3 import normalize_case
import sys


class ReadFromFile:
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
        text, city = re.findall(r'"(.*?)"', ' '.join(section_content))
        return text, city

    @staticmethod
    def extract_text_and_date(section_content):
        text, date = re.findall(r'"(.*?)"', ' '.join(section_content))
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


class CSVUpdater:
    @staticmethod
    def process_news_feed(file_path):
        try:
            with open(file_path, 'r') as file:
                text = file.read()

            all_words = re.findall(r'\b(?!\d+\b)\w+\b', text.lower())
            words_count = {}
            for word in all_words:

                if word in words_count:
                    words_count[word] += 1

                else:
                    words_count[word] = 1

            # all letters low and upper case with duplication
            all_letters_duplicated = re.sub(r'[^a-zA-Z]', '', text)
            from collections import Counter
            counter_without_case = Counter(all_letters_duplicated.lower())
            counter_upper_case_letters = Counter(re.sub(r'[^A-Z]', '', all_letters_duplicated))
            set_of_letters = set(all_letters_duplicated.lower())

            return words_count, counter_without_case, counter_upper_case_letters, set_of_letters




        except FileNotFoundError:
            print(f"File {file_path} not found.")

    @staticmethod
    def write_to_csv_word_count(word_count, output_file="word_count.csv"):
        # Writing the word count CSV file
        list = [{'word': k, 'count': v} for k, v in word_count.items()]

        with open(output_file, 'w', newline='') as f:
            count_writer = csv.DictWriter(f, fieldnames=['word', 'count'], delimiter='-')
            count_writer.writeheader()
            count_writer.writerows(list)

    @staticmethod
    def write_to_csv_letter_count(counter_without_case, counter_upper_case_letters, set_of_letters, output_file="letter_count.csv"):
        # Writing the letter count CSV file
        with open(output_file, 'w', newline='') as f:
            writer_csv = csv.writer(f, delimiter=',', quotechar='\'', quoting=csv.QUOTE_NONE)
            writer_csv.writerow(['letter', 'cout_all', 'count_uppercase', 'percentage'])
            for letter in set_of_letters:
                writer_csv.writerow([letter, counter_without_case[letter], counter_upper_case_letters[letter.upper()],
                                     counter_upper_case_letters[letter.upper()]/counter_without_case[letter]*100])

    @staticmethod
    def update_csvs(file_path):
        words_count, counter_without_case, counter_upper_case_letters, set_of_letters = CSVUpdater.process_news_feed(file_path)

        if words_count is not None and counter_without_case is not None:
            # Recreate and write CSV files
            CSVUpdater.write_to_csv_word_count(words_count)
            CSVUpdater.write_to_csv_letter_count(counter_without_case, counter_upper_case_letters, set_of_letters)
            print("CSV files updated successfully!")
        else:
            print("Error processing the file.")


class NewsFeed:

    @staticmethod
    def save_to_file(content):
        # Open the file in append mode, so we don't overwrite existing content
        with open("news_feed.txt", "a") as file:
            file.write(content + "\n")
            file.write(' ' * 30 + "\n")

        # Call the update_csvs method after saving content to the file
        CSVUpdater.update_csvs("news_feed.txt")


class News(NewsFeed):
    def __init__(self, text, city):
        self.text = text
        self.city = city
        self.date = self.calculate_date()

    def __str__(self):
        return f"News-----\n{self.text}, \n{self.city}, {self.date}"

    @staticmethod
    def input_data():
        text = normalize_case(input("Please write the news text \n"))
        city = normalize_case(input("Please write the city \n"))
        return News(text, city)

    @staticmethod
    def calculate_date():
        return datetime.now().date()


class PrivateAd(NewsFeed):
    def __init__(self, text, exp_date):
        self.text = text
        self.exp_date = exp_date

    def __str__(self):
        return f"Private Ad-----\n{self.text}, \n{self.exp_date}, {self.calculate_difference()} days left"

    @staticmethod
    def input_data():
        text = normalize_case(input("Please write the ad text \n"))
        while True:
            exp_date = input(
                "Please write the date when ad should be published in format YY/mm/dd\n")
            try:
                # Try to parse the date
                exp_date_object = datetime.strptime(
                    exp_date, "%Y/%m/%d").date()

                # Check if the expiration date is greater than or equal to today
                if exp_date_object >= datetime.now().date():
                    break  # Valid date, exit loop
                else:
                    print(
                        "Expiration date must be today or in the future. Please try again.")
            except ValueError:
                print(
                    "You entered the wrong format of date. Please enter in YY/mm/dd format.")

        return PrivateAd(text, exp_date)

    def calculate_difference(self):
        now = datetime.now().date()
        exp_date_object = datetime.strptime(self.exp_date, "%Y/%m/%d")
        now_date_object = datetime.strptime(str(now), "%Y-%m-%d")
        return (exp_date_object - now_date_object).days


class SearchJob(NewsFeed):
    @staticmethod
    def input_data():
        pass


# Read news feed from file
def read_news_feed(file_path):
    rff = ReadFromFile(file_path)

    inputs = rff.parse_file()

    if inputs:
        for item in inputs:
            for type, content in item.items():
                if type == 'news':
                    news = News(content["text"], content["city"])
                    news.save_to_file(news.__str__())
                elif type == 'private ad':
                    ad = PrivateAd(content["text"], content["date"])
                    ad.save_to_file(ad.__str__())


def enter_from_console():
    type_feed = input(
        "What category would you like to add? news(1), private ad(2) or search job(3)? Type the number \n")
    if int(type_feed) == 1:
        news = News.input_data()
        news.save_to_file(news.__str__())
    elif int(type_feed) == 2:
        ad = PrivateAd.input_data()
        ad.save_to_file(ad.__str__())
    elif int(type_feed) == 3:
        # job_search = SearchJob.input_data()
        # print(job_search)
        print("The code is empty for this class")
    else:
        print("Please enter valid type feed")


if len(sys.argv[1:]) > 0:
    type_of_input = input(
        "Do you like to process the file from parameters? (y/n)\n")
    if type_of_input.lower() == 'y':
        file_path = sys.argv[1]
        read_news_feed(file_path)

    elif type_of_input.lower() == 'n':
        type_of_input = input(
            "Do you like to enter the path file or enter from console? (1 or 2)?\n")
        if type_of_input == '1':
            file_path = input("Please, enter the path to the file:\n")
            read_news_feed(file_path)

        elif type_of_input == '2':
            enter_from_console()
        else:
            print(
                "Your input is invalid, expect 1 or 2 (1 - enter the file path, 2 - enter from console)")

    else:
        print("Your input is invalid, expect y or n")
else:
    type_of_input = input(
        "Do you like to enter the path file or enter from console? (1 or 2)?\n")
    if type_of_input == '1':
        file_path = input("Please, enter the path to the file:\n")
        read_news_feed(file_path)

    elif type_of_input == '2':
        enter_from_console()


