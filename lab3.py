import string
import re

text = """homEwork:
  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""


# Normalization of text
def normalize_case(txt):
    normalized_text = txt.lower()
    return normalized_text


# Counting the number of whitespaces
def count_whitespaces(txt):
    return len([i for i in txt if i in string.whitespace])


# Creating a new sentence from the last words.
def create_new_sentence_from_last_words(txt):
    splitted_text = re.split(r"[.!?]", txt)
    # print(splitted_text)
    last_words = [sentence.split()[-1] for sentence in splitted_text if
                  len(sentence) != 0 and sentence not in string.whitespace]
    new_line = ' '.join(last_words)
    return new_line


def replace_words(replace_from, replace_to, txt):
    pattern = r"\b%s\b" % replace_from
    upd_txt = re.sub(pattern, replace_to, txt)
    return upd_txt


def add_new_sentence_after_smth(what_add, after_what_add, txt):
    x = re.search(after_what_add, txt)  # find the word in text
    return txt[:x.span()[1]+1] + what_add + txt[x.span()[1]+1:]


norm_text = normalize_case(text)
# print(f"Normalized text:\n{norm_text}")

whitespace_count = count_whitespaces(norm_text)
print(f"Number of whitespaces in this text is {whitespace_count}")

new_sentence = create_new_sentence_from_last_words(norm_text)
# Sentence with last words of each existing sentence
print(f"Sentence with last words of each existing sentence: {new_sentence}.")

# Replacing iz with is
replaced_text = replace_words(' iz ', ' is ', norm_text)
# print(replaced_text)

updated_text = add_new_sentence_after_smth(new_sentence, 'paragraph.', replaced_text)
print(updated_text)

