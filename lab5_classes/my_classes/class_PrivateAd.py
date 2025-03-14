from datetime import datetime
from lab3 import normalize_case
from my_classes.class_NewsFeed import NewsFeed


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