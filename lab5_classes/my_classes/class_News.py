from datetime import datetime
from lab3 import normalize_case
from my_classes.class_NewsFeed import NewsFeed


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

