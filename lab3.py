text = """homEwork:
  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

# Normalization of text
text = text.lower()
# print("Normalized text:\n", text)

# Counting the number of whitespaces
import string

whitespace_count = len([i for i in text if i in string.whitespace])
print(f"Number of whitespaces in this text is {whitespace_count}")

# Creating a new sentence from the last words.
splitted_text = text.split('.')
# print(splitted_text)
last_words = [sentence.split()[-1] for sentence in splitted_text if len(sentence) != 0 and sentence not in string.whitespace]
new_line = ' '.join(last_words)
# Sentence with last words of each existing sentence
print(f"Sentence with last words of each existing sentence: {new_line}.")

# Replacing iz with is
import re
text = re.sub(r"\b iz \b", " is ", text)

x = re.search("paragraph.", text)  # find the word in text
updated_text = text[:x.span()[1]+1] + new_line + text[x.span()[1]+1:]
print(updated_text)


