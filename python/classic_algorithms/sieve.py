#!/usr/bin/python
"""
The sieve of Eratosthenes is one of the most efficient ways to find all of the
smaller primes (below 10 million or so).
"""

def sieve(max_prime):
    """
    Outputs primes < max_prime
    """
    primes = [True] * max_prime
    result = []

    for i in range(2, max_prime):
        if primes[i]:
            for j in range(i+i, max_prime, i):
                primes[j] = False

    for i in range(2, max_prime):
        if primes[i]:
            result.append(i)

    return result

def main():
    """
    Asks user for largest prime. Outputs primes <= largest prime
    """
    max_prime = int(input("Largest prime to find: ")) + 1
    print(sieve(max_prime))

if __name__ == '__main__':
    main()
