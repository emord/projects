#!/usr/bin/python

def cc_encode(letter, key):
    result = letter

    if result.isalpha():
        a = letter.upper()
        result = ord(a) + key

        if result > ord('Z'):
            result -= 26 

    return chr(result)

def main():
    key = int(input("Cipher key (1 to 25): "))
    s = input("Encrypt this: ")

    result = ""
    for letter in s:
        result += cc_encode(letter, key)
    
    print(result)

if __name__ == '__main__':
    main()
