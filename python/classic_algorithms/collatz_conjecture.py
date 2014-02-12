#!/usr/bin/python
"""
Start with a number *n > 1*. Find the number of steps it takes to reach one 
using the following process: If *n* is even, divide it by 2. If *n* is odd, 
multiply it by 3 and add 1.
"""

def collatz_steps(num):
    """
    Returns number of steps in Collatz conjecture for num
    """
    steps = 0

    while num > 1:
        steps += 1
        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1

    return steps

def main():
    """
    Asks for number and performs Collatz conjecture on it
    """
    cnum = int(input("Number to perform Collatz conjecture on: "))
    print(collatz_steps(cnum))

if __name__ == '__main__':
    main()
