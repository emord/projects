#!/usr/bin/python

def pig_latin_translation(s):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if s[0] in vowels:
        return s + 'way'

    i = 0
    while s[i].lower() not in vowels:
        i += 1

    return s[i:] + s[:i] + 'ay'

def main():
    s = input("Convert this word into pig latin: ")
    print(pig_latin_translation(s))

if __name__ == '__main__':
    main()
