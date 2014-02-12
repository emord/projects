#!/usr/bin/python
"""
Have the user enter a number and find all Prime Factors (if there are any) and
display them.
"""

def prime_factors_of(num):
    """
    Returns list of prime factors of num
    """
    result = [ ]
    cur_prime = 2

    while num > 1:
        if num % cur_prime == 0:
            result.append(cur_prime)
            num /= cur_prime
        else:
            cur_prime += 1

    return result

def main():
    """
    Asks for a number and computes prime factors of it
    """
    pf = int(input("Compute prime factorization of this number: "))
    print(prime_factors_of(pf))

if __name__ == '__main__':
    main()
