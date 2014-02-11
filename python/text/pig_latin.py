#!/usr/bin/python
"""
Pig Latin is a game of alterations played on the English language game. To
create the Pig Latin form of an English word the initial consonant sound is
transposed to the end of the word and an ay is affixed (Ex.: "banana" would
yield anana-bay). Read Wikipedia for more information on rules.
"""

def pig_latin_translation(string):
    """
    Translate string into pig latin version
    """
    vowels = ['a', 'e', 'i', 'o', 'u']

    if string[0] in vowels:
        return string + 'way'

    i = 0
    while string[i].lower() not in vowels:
        i += 1

    return string[i:] + string[:i] + 'ay'

def main():
    """
    Asks user for word to translate to pig latin
    """
    string = input("Convert this word into pig latin: ")
    print(pig_latin_translation(string))

if __name__ == '__main__':
    main()
