# report.py
#
# Exercise 2.4: A list of tuples
import csv
import fileparse

def read_portfolio(filename):
    '''
    Read a stock portfolio into a list of dictionaries with keys
    name, shares, and prices.
    '''
    with open(filename, 'rt') as file:
        return fileparse.parse_csv(file, select=['name', 'shares', 'price'], types=[str, int, float])

def read_prices(filename):
    '''
    Read a stock current price into a list of dictionaries with keys
    name, price
    '''
    with open(filename, 'rt') as lines:
        return dict(fileparse.parse_csv(lines, types=[str, float], has_headers=False))

# Exercison 2.7: Compute the currrent value of the porofolip along with the gain/loss
def make_report(portfolio, prices):
    report = []
    for row in portfolio:
        current_price = prices[row['name']]
        change = current_price - row['price']
        stocks = (row['name'], row['shares'], current_price, change)
        report.append(stocks)

    return report

# Exercise 3.1: Structuring a program as a collection of functions
# A function that prints out the report
def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))

    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')

# Exercise 3.2: Creating a top-level function for program execution
def portfolio_report(portfoliofile, pricesfile):
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricesfile)
    report = make_report(portfolio, prices)
    print_report(report)

def main(argv):
    if len(argv) != 3:
        raise SystemExit('Usage: %s portfile pricefile' %argv[0])
    portfolio_report(argv[1], argv[2]) 

if __name__ == '__main__':
    import sys
    main(sys.argv)
