#!/usr/bin/python
"""
Implement a Caesar cipher, both encoding and decoding. The key is an integer
from 1 to 25. This cipher rotates the letters of the alphabet (A to Z). The
encoding replaces each letter with the 1st to 25th next letter in the alphabet
(wrapping Z to A). So key 2 encrypts "HI" to "JK", but key 20 encrypts "HI" to
"BC". This simple "monoalphabetic substitution cipher" provides almost no
security, because an attacker who has the encoded message can either use
frequency analysis to guess the key, or just try all 25 keys.
"""

def cc_encode(letter, key):
    """
    Takes a letter and key and returns the upper case letter + key. Wraps around
    from 'Z' to 'A'
    """
    result = letter

    if result.isalpha():
        upper_letter = letter.upper()
        result = ord(upper_letter) + key

        if result > ord('Z'):
            result -= 26

    return chr(result)

def main():
    """
    Asks user for key and string to encrypt
    """
    key = int(input("Cipher key (1 to 25): "))
    string = input("Encrypt this: ")

    result = ""
    for letter in string:
        result += cc_encode(letter, key)

    print(result)

if __name__ == '__main__':
    main()
