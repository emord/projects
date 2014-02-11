#!/usr/bin/python
"""
Calculate the monthly payments of a fixed term mortgage over given Nth terms
at a given interest rate. Also figure out how long it will take the user to
pay back the loan.
"""

def monthly_payments(principal, interest, num_terms):
    """
    Returns monthly payment of mortgage
    """
    interim = (1 + interest) ** num_terms
    return principal * interest * interim / (interim - 1)

def main():
    """
    Prints monthly payments of a mortgage
    """
    principal = float(input("Principal: "))
    interest = float(input("Interest rate (per payment): "))
    terms = int(input("Number of terms: "))
    monthly_payment = monthly_payments(principal, interest, terms)
    print("{0:.2f}".format(monthly_payment))

if __name__ == '__main__':
    main()
