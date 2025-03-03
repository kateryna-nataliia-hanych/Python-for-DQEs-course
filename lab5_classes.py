from datetime import datetime


class NewsFeed:

    @staticmethod
    def save_to_file(content):
        # Open the file in append mode, so we don't overwrite existing content
        with open("news_feed.txt", "a") as file:
            file.write(content + "\n")
            file.write(' ' * 30 + "\n")


class News(NewsFeed):
    def __init__(self, text, city):
        self.text = text
        self.city = city
        self.date = self.calculate_date()

    def __str__(self):
        return f"News-----\n{self.text}, \n{self.city}, {self.date}"

    @staticmethod
    def input_data():
        text = input("Please write the news text \n")
        city = input("Please write the city \n")
        return News(text, city)

    @staticmethod
    def calculate_date():
        date = datetime.now().date()
        return date


class PrivateAd(NewsFeed):
    def __init__(self, text, exp_date):
        self.text = text
        self.exp_date = exp_date

    def __str__(self):
        return f"Private Ad-----\n{self.text}, \n{self.exp_date}, {self.calculate_difference()} days left"

    @staticmethod
    def input_data():
        text = input("Please write the ad text \n")
        while True:
            exp_date = input("Please write the date when ad should be published in format YY/mm/dd\n")
            try:
                # Try to parse the date
                exp_date_object = datetime.strptime(exp_date, "%Y/%m/%d").date()

                # Check if the expiration date is greater than or equal to today
                if exp_date_object >= datetime.now().date():
                    break  # Valid date, exit loop
                else:
                    print("Expiration date must be today or in the future. Please try again.")
            except ValueError:
                print("You entered the wrong format of date. Please enter in YY/mm/dd format.")

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


type_feed = input("What category would you like to add? news(1), private ad(2) or search job(3)? Type the number \n")
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
