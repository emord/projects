#!/usr/bin/python
"""
Enter a string and the program counts the number of vowels in the text. For
added complexity have it report a sum of each vowel found.
"""

def count_vowels_basic(string):
    """
    Returns number of vowels in string
    """
    result = 0

    for letter in string:
        if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
            result += 1

    return result

def count_vowels_complex(string):
    """
    Returns dictionary of vowels and counts of vowels in string
    """
    result = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}

    for letter in string:
        if letter.lower() in result.keys():
            result[letter.lower()] += 1

    return result

def main():
    """
    Asks user for string to count vowels in
    """
    string = input("Count vowels in this: ")
    print(count_vowels_basic(string))
    print(count_vowels_complex(string))

if __name__ == '__main__':
    main()
