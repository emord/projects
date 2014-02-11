#!/usr/bin/python
"""
A program which can go out and check the current value of stocks for a list
of symbols entered by the user. The user can set how often the stocks are
checked. For CLI, show whether the stock has moved up or down.
"""

import urllib.request

def request_from_yahoo(stocks):
    """
    Request list of stocks (comma-separated string) from yahoo's api
    """
    url = 'http://finance.yahoo.com/d/quotes.csv?s='
    url += stocks
    url += '&f=snl1c1'
    return urllib.request.urlopen(url).read()

def main():
    """
    Asks for comma-separated list of stocks. Prints stock info
    """
    stocks = input("List of stocks (comma-separated): ")
    csv_string = request_from_yahoo(stocks)
    csv_array = csv_string.decode('utf-8').strip().split('\r\n')
    print('Format: Stock Symbol, Stock Name, Last Trade Price, Change')
    for row in csv_array:
        print(row)

if __name__ == '__main__':
    main()
