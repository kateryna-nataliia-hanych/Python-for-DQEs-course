import sys
from datetime import datetime
from my_classes.class_ReadFromTxtFile import ReadFromTxtFile
from my_classes.class_ReadFromJsonFile import ReadFromJsonFile
from my_classes.class_ReadFromXmlFile import ReadFromXmlFile
from my_classes.class_PrivateAd import PrivateAd
from my_classes.class_News import News
from my_classes.class_DBConnection import DBConnection


# Read news feed from file
def read_news_feed(file_path):
    file_path = file_path.strip()
    if file_path.endswith('.txt'.lower()):
        read_txt_obj = ReadFromTxtFile(file_path)
        inputs = read_txt_obj.parse_file()
    elif file_path.endswith('.json'.lower()):
        read_json_obj = ReadFromJsonFile(file_path)
        inputs = read_json_obj.parse_file()
    elif file_path.endswith('.xml'.lower()):
        read_xml_obj = ReadFromXmlFile(file_path)
        inputs = read_xml_obj.parse_file()

    if inputs:
        dbc = DBConnection('news_feed.db')
        for item in inputs:
            for type, content in item.items():
                if type == 'news':

                    # save to db table news
                    dbc.create_table('news', ('id', 'INTEGER PRIMARY KEY'), ('text', 'TEXT'), ('city', 'TEXT'),
                                     ('date', 'DATE'))
                    if dbc.check_duplication('news', ['text', 'city'], text = content["text"], city = content["city"]) is False:
                        dbc.insert('news', text = content["text"], city = content["city"], date= datetime.now().strftime('%Y/%m/%d'))

                    news = News(content["text"], content["city"])
                    news.save_to_file(news.__str__())

                elif type == 'private ad':

                    # save to db table ads
                    dbc.create_table('ads', ('id', 'INTEGER PRIMARY KEY'), ('text', 'TEXT'), ('expiration_date', 'DATE'))
                    if dbc.check_duplication('ads', ['text'], text=content["text"],
                                             expiration_date=content["date"]) is False:
                        dbc.insert('ads', text=content["text"], expiration_date=content["date"])

                    ad = PrivateAd(content["text"], content["date"])
                    ad.save_to_file(ad.__str__())


def enter_from_console():
    dbc = DBConnection('news_feed.db')
    type_feed = input(
        "What category would you like to add? news(1), private ad(2) or search job(3)? Type the number \n")
    if int(type_feed) == 1:
        news = News.input_data()
        news.save_to_file(news.__str__())

        #     save data to news table in DB
        dbc.create_table('news', ('id', 'INTEGER PRIMARY KEY'), ('text', 'TEXT'), ('city', 'TEXT'),
                         ('date', 'DATE'))
        text, city, date = news.news_content_to_db()
        if dbc.check_duplication('news', ['text', 'city'], text=text, city=city) is False:
            dbc.insert('news', text=text, city=city, date=date.strftime('%Y/%m/%d'))

    elif int(type_feed) == 2:
        ad = PrivateAd.input_data()
        ad.save_to_file(ad.__str__())

        # save to db table ads
        dbc.create_table('ads', ('id', 'INTEGER PRIMARY KEY'), ('text', 'TEXT'), ('expiration_date', 'DATE'))
        text, exp_date = ad.ads_content_to_db()
        if dbc.check_duplication('ads', ['text'], text=text,
                                 expiration_date=exp_date) is False:
            dbc.insert('ads', text=text, expiration_date=exp_date)

    elif int(type_feed) == 3:
        # job_search = SearchJob.input_data()
        # print(job_search)
        print("The code is empty for this class")
    else:
        print("Please enter valid type feed")


def choice_if_no_parameter():
    type_of_input = input(
        "Do you like to enter the path file (txt/json/xml) or enter from console? (1 or 2)?\n")
    if type_of_input == '1':
        file_path = input("Please, enter the path to the file:\n")
        read_news_feed(file_path)

    elif type_of_input == '2':
        enter_from_console()
    else:
        print(
            "Your input is invalid, expect 1 or 2 (1 - enter the file path, 2 - enter from console)")


if len(sys.argv[1:]) > 0:
    type_of_input = input(
        "Do you like to process the file from parameters? (y/n)\n")
    if type_of_input.lower() == 'y':
        file_path = sys.argv[1]
        read_news_feed(file_path)

    elif type_of_input.lower() == 'n':
        choice_if_no_parameter()

    else:
        print("Your input is invalid, expect y or n")
else:
    choice_if_no_parameter()

