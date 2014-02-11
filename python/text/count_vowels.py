#!/usr/bin/python

def count_vowels_basic(s):
    result = 0

    for letter in s:
        if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
            result += 1

    return result

def main():
    s = input("Count vowels in this: ")
    print(count_vowels_basic(s))

if __name__ == '__main__':
    main()
