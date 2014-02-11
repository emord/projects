#!/usr/bin/python3
"""
Enter a string and the program will reverse it and print it out.
"""


def reverse_string(string):
    """
    Reverses string string
    """
    return string[::-1]

def main():
    """
    Asks user for string to reverse
    """
    string = input("String to reverse: ")
    print(reverse_string(string))

if __name__ == '__main__':
    main()
