#!/usr/bin/python
"""
The Factorial of a positive integer, n, is defined as the product of the 
sequence n, n-1, n-2, ...1 and the factorial of zero, 0, is defined as being 
1. Solve this using both loops and recursion.
"""

def factorial_iteration(num):
    """
    Returns num! through iteration
    """
    res = 1
    
    for i in range(2, num+1):
        res *= i
    
    return res

def factorial_recursion(num):
    """
    Returns num! through recursion
    """
    if num == 0:
        return 1
    else:
        return num * factorial_recursion(num-1)

def main():
    """
    Asks for a number and performs factorial computation both iteratively and
    recursively
    """
    fact = int(input("Number to perform factorial on: "))
    print("Recursion: {0}".format(factorial_recursion(fact)))
    print("Iteration: {0}".format(factorial_iteration(fact)))

if __name__ == '__main__':
    main()
