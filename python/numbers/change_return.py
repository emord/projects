#!/usr/bin/python
"""
The user enters a cost and then the amount of money given. The program will
figure out the change and the number of quarters, dimes, nickels, pennies
needed for the change.
"""

from functools import partial
from math import floor

def calculate_change_coin(coin, cents):
    """
    Calculates how many coins can go into amount, and returns amount left over
    """
    num_coin = floor(cents / coin)
    return [num_coin, cents - num_coin * coin]

calculate_dollars = partial(calculate_change_coin, 100)
calculate_quarters = partial(calculate_change_coin, 25)
calculate_dimes = partial(calculate_change_coin, 10)
calculate_nickels = partial(calculate_change_coin, 5)
calculate_pennies = partial(calculate_change_coin, 1)

def calculate_change(cents):
    """
    Calculates least change for amount
    """
    change = dict()

    change['dollars'], cents = calculate_dollars(cents)
    change['quarters'], cents = calculate_quarters(cents)
    change['dimes'], cents = calculate_dimes(cents)
    change['nickels'], cents = calculate_nickels(cents)
    change['pennies'], cents = calculate_pennies(cents)

    return change

def main():
    """
    Returns change
    """
    given = float(input("Amount of money given: "))
    cost = float(input("Cost: "))

    print(calculate_change(int(100*round(given - cost, 2))))

if __name__ == '__main__':
    main()
