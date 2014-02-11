#!/usr/bin/python

def isPalindrome(s):
    return s == s[::-1]

def main():
    s = input("This is a palindrome: ")
    print(isPalindrome(s))

if __name__ == '__main__':
    main()
