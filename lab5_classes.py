import csv
import re
from datetime import datetime
from lab3 import normalize_case
import sys


















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


