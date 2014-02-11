#!/usr/bin/python
"""
Counts the number of individual words in a string. For added complexity read
these strings in from a text file and generate a summary.
"""

def main():
    """
    Asks user for string to count words of
    """
    string = input("Number of words in this string: ")
    print(len(string.split()))

if __name__ == '__main__':
    main()
