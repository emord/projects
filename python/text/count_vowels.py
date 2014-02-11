#!/usr/bin/python

def count_vowels_basic(s):
    result = 0

    for letter in s:
        if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
            result += 1

    return result

def count_vowels_complex(s):
    result = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}

    for letter in s:
        if letter.lower() in result.keys():
            result[letter.lower()] += 1
    
    return result

def main():
    s = input("Count vowels in this: ")
    print(count_vowels_basic(s))
    print(count_vowels_complex(s))

if __name__ == '__main__':
    main()
