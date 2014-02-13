#!/usr/bin/python
"""
An [Inverted Index](http://en.wikipedia.org/wiki/Inverted_index) is a data
structure used to create full text search. Given a set of text files,
implement a program to create an inverted index. Also create a user interface
to do a search using that inverted index which returns a list of files that
contain the query term / terms. The search index can be in memory.
"""

import re

def string_words(string):
    """
    Returns string split into words, with non alphanumeric characters removed
    """
    return re.sub(r'[^a-zA-Z0-9\s]+', ' ', string).split()

def add_set_to_dict(set_, member, value):
    """
    Adds a set to a dict safely
    """
    if member in set_:
        set_[member].add(value)
    else:
        set_[member] = set([value])

def create_basic_inverted_index(indices, strings):
    """
    Creates inverted index that returns what string a word might be in.

    Format: { word: {indicies of strings that contains word} }
    """
    res = dict()

    for index, string in zip(indices, strings):
        words = set(string_words(string))
        for word in words:
            add_set_to_dict(res, word, index)

    return res

def create_full_inverted_index(indices, strings):
    """
    Creates inverted index that returns what string a word might be in, and
    where it is in the string

    Format: { word: {(index of string, position of word)} }
    """
    res = dict()

    for index, string in zip(indices, strings):
        words = string_words(string)
        for word_index, word in enumerate(words):
            add_set_to_dict(res, word, (index, word_index))

    return res

def full_inverted_index_from_files(files):
    """
    Takes a list of files and creates a full inverted index
    """
    texts = []

    for file_ in files:
        texts.append(open(file_).read())

    return create_full_inverted_index(files, texts)

def main():
    """
    Asks user for files, then provides search interface
    """
    files = []
    file_name = input("First file to include: ").strip()

    while file_name != "":
        files.append(file_name)
        file_name = input("Next file to include (blank line to stop): ")

    search_db = full_inverted_index_from_files(files)

    search_term = input("Term to search for: ")

    while search_term != "":
        if search_term in search_db:
            print(search_db[search_term])
        else:
            print("Term not found")

        search_term = input("Term to search for (blank line to stop): ")

if __name__ == '__main__':
    main()
