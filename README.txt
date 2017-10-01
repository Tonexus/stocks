Quick Stocks Script

This script calculates what share/dollar amounts are required for dollar cost
averaging. The script is run from the command line with one argument:

    python stocks.py <arg1>

Arguments:
    arg1 - the amount in dollars you want to invest.

The script also requires 2 files:
    stocks.csv - a csv file with 2 columns: ticker symbol, proportional amount.
                 The ticker symbol is the symbol for the stock and the
                 proportional amount is the amount of stock desired relative to
                 the other stocks.
    stocks.cfg - a python config file with one section and one key. The "api"
                 section must contain the key "api key" corresponding to a
                 valid Quandl api key.