#!/usr/bin/python3

def reverse_string(s):
    return s[::-1]

def main():
    s = input("String to reverse: ")
    print(reverse_string(s))

if __name__ == '__main__':
    main()
