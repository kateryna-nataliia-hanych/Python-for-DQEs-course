# Python-for-DQEs-course
The repo for Python for Data Quality Engineers course on learn.epam.com

### lab1
- create list of 100 random numbers from 0 to 1000
- sort list from min to max (without using sort())
- calculate average for even and odd numbers
- print both average result in console


### lab2
1. create a list of random number of dicts (from 2 to 10)
dict's random numbers of keys should be letter,
dict's values should be a number (0-100),
example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
2. get previously generated list of dicts and create one common dict:
if dicts have same key, we will take max value, and rename key with dict number with max value
if key is only in one dict - take it as is,
example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}

### lab3

"homEwork:
  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."


### lab5_classes

Create a tool, which will do user generated news feed:

1. User select what data type he wants to add
2. Provide record type required data
3. Record is published on text file in special format

You need to implement:
1. News – text and city as input. Date is calculated during publishing. 
2. Private ad – text and expiration date as input. Day left is calculated during publishing.

Expand with additional classses, which allow to provide records by text file and JSON file:
1. Define your input format (one or many records)
2. Default folder or user provided file path
3. Remove file if it was successfully processed
4. Apply case normalization functionality from lab3


Calculate number of words and letters from previous output test file(news_feed.txt).

Create two csv:
1. word-count (all words are preprocessed in lowercase)
2. letter, cout_all, count_uppercase, percentage (add header, spacecharacters are not included)

CSVs should be recreated each time new record added.






