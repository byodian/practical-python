# report.py
#
# Exercise 2.4: A list of tuples
import csv
import fileparse
import tableformat

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
def print_report(reportdata, formatter):
    '''
    Print a nicely formatted table from a list of (name, shares, price, change) tuples.
    '''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])

    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)

# Exercise 3.2: Creating a top-level function for program execution
def portfolio_report(portfoliofile, pricesfile, fmt = 'txt'):
    # Read a data file
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricesfile)

    # Create a report data
    report = make_report(portfolio, prices)

    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)

def main(argv):
    if len(argv) != 3:
        raise SystemExit('Usage: %s portfile pricefile' %argv[0])
    portfolio_report(argv[1], argv[2]) 

if __name__ == '__main__':
    import sys
    main(sys.argv)
