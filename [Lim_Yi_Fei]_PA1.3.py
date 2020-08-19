'''
13.5 + 6

Very clean and simple code. Unfortunately, two flaws: the list was not sorted alphabetically, and every word in the list - including duplicates - was iterated through.
'''

import string

sentence = input("Enter sentence: ")

# splits words by space, strips them of punctuations, and converts them to lower case
s_list = [w.strip(string.punctuation).lower() for w in sentence.split()]

# prints word count for each word in entry
for word in s_list:
    number = s_list.count(word)
    print(word + ":" + str(number))

