#!/usr/bin/python
"""
Checks if the string entered by the user is a palindrome. That is that it
reads the same forwards as backwards like racecar
"""

def is_palindrome(string):
    """
    Returns True if string is palindrome
    """
    return string == string[::-1]

def main():
    """
    Asks user for string to query if it's a palindrome
    """
    string = input("This is a palindrome: ")
    print(is_palindrome(string))

if __name__ == '__main__':
    main()
