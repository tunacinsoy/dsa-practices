"""
Description:
    We want to find the most frequently used words in a long string of text.
    Write a function most_common_words(text) that returns an array containing words with their frequencies,
    sorted from most common to least common, with ties broken by alphabetic order.

    For greater accuracy, your solution should ignore punctuation and capitalization.

Usage:
    `python <file_name.py>`

Arguments:
    None

Date:
    2024-11-26

Version:
    1.0.0

Algorithm Implementation:
    text = 'It was the best of times, it was the worst of times.'

    [
      ('it', 2),
      ('of', 2),
      ('the', 2),
      ('times', 2),
      ('was', 2),
      ('best', 1),
      ('worst', 1)
    ]

  # 1) Use regex pattern to sanitize the string from punctuations, and apply lower()
  # 2) Split the text into words
  # 3) Create a dictionary, keys as words and values as occurrances
  # 4) sort the words in the dictionary according to alphabetical order
  # 5) sort the words according to their occurances

Complexities:
    Time: O(n * logn) -> because of sorted() functions
    Space: O(n)
"""

from typing import List, Tuple
import re


def most_common_words(inputStr: str) -> List[Tuple[str, int]]:

    if len(inputStr) == 0:
        return []
    # Sanitize text from any punctuations
    punctuation_re = r"[.,;!\"\'\(\)]"

    sanitized_text = re.sub(punctuation_re, "", inputStr).lower()
    words = sanitized_text.split(" ")

    # Eliminating cases where there are empty words in words list
    for index, word in enumerate(words):
        if len(word) == 0:
            words.pop(index)

    print(words)
    word_occurrance = {}

    for word in words:
        if word not in word_occurrance:
            word_occurrance[word] = 1
        else:
            word_occurrance[word] += 1

    #    print(word_occurrance)

    # Sort alphabetically
    words = sorted(word_occurrance.items())
    # print(words) # [('best', 1), ('it', 2), ('of', 2), ('the', 2), ('times', 2), ('was', 2), ('worst', 1)]

    # Sort according to occurrances
    words = sorted(words, reverse=True, key=lambda x: x[1])

    return words


sample_text = "It was the best of times, it was the worst of times."
print(most_common_words(sample_text))

sample_text2 = ""
print(most_common_words(sample_text2))

sample_text3 = "Hello  World ! Hello, world!"
print(most_common_words(sample_text3))
