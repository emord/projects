#!/usr/bin/python
"""
Enter a number and have the program generate the Fibonacci sequence to that
number or to the Nth number.
"""

def fibonacci_recursive(num):
    """
    Returns nth fibonacci number via recursion
    """
    if num == 1 or num == 2:
        return 1
    else:
        return fibonacci_recursive(num-2) + fibonacci_recursive(num-1)

def fibonacci_iterative(num):
    """
    Returns nth fibonacci number via iteration
    """
    first, second = 1, 1

    for _ in range(2, num):
        second += first
        first = second - first

    return second

def main():
    """
    Ask for and returns nth fibonacci number
    """
    fib_num = int(input("Find nth fibonacci number (1 indexed): "))
    print(fibonacci_recursive(fib_num))
    print(fibonacci_iterative(fib_num))

if __name__ == '__main__':
    main()
