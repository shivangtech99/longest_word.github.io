import re
from collections import defaultdict


file_loc = input("Please specify the input file location: ")
n = input(
    "Please specify the number of longest words to output (default 2): ")

with open(file_loc, 'r') as f:
    words_list = []
    for line in f:
        for word in line.split():
            words_list.append(word.lower())
# print(words_list)

def get_longest_n_words(word_list, n):
    # Create a defaultdict to store the words as keys and their length as values
    word_dict = defaultdict(int)
    for word in word_list:
        word_dict[word] = len(word)

    # Sort the words in descending order of length
    sorted_words = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)

    # Return the top n longest words
    return [word for word, length in sorted_words[:n]]

def count_composed_words(words_list):
    # Create a set of all words in the list
    word_set = set(words_list)

    # Create a defaultdict to store the words that are composed of other words
    composed_words = defaultdict(int)

    # Check if each word is composed of other words in the list
    for word in words_list:
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix in word_set and suffix in word_set:
                composed_words[word] = 1
                break

    # Return the total count of words that are composed of other words
    return sum(composed_words.values())

# Example usage
# words_list = ["cat", "cats", "catsdogcats", "catxdogcatrat", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]
# n = 3

print("Top", n, "longest words:", get_longest_n_words(words_list, n))
print("Total count of words composed of other words:", count_composed_words(words_list))

