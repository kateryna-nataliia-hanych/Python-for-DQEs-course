from my_classes.class_CSVUpdater import CSVUpdater


class NewsFeed:

    @staticmethod
    def save_to_file(content):
        # Open the file in append mode, so we don't overwrite existing content
        with open("news_feed.txt", "a") as file:
            file.write(content + "\n")
            file.write(' ' * 30 + "\n")

        # Call the update_csvs method after saving content to the file
        CSVUpdater.update_csvs("news_feed.txt")