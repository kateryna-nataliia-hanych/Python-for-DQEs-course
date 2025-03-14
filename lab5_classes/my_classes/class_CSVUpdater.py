import re
import csv


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