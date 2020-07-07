# report.py
#
# Exercise 2.4: A list of tuples
import csv
def read_portfolio_a(filename):
    '''
    Read a stock portfolio into a list of dictionaries with keys
    name, shares, and prices.
    '''
    portfolio = []

    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)

        for row in rows:
            record = dict(zip(headers, row))
            stock = {
                'name': record['name'],
                'shares': int(record['shares']),
                'price': float(record['price'])
            }
            portfolio.append(stock)

        return portfolio


# Exercise 2.5: List of Dictionaries
def read_portfolio_b(filename):
    '''
    Read a stock portfolio into a list of dictionaries with keys
    name, shares, price
    '''
    portfolio = []

    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            holding = {
                'name': row[0],
                'shares': int(row[1]),
                'price': float(row[2])
            }
            portfolio.append(holding)

        return portfolio

def read_prices(filename):
    prices = {}
    '''
    Read a stock current price into a list of dictionaries with keys
    name, price
    '''
    with open(filename) as file:
        rows = csv.reader(file)
        for row in rows:
            #try:
            #   prices[str(row[0])] = row[1]
            #except:
            #    print('Error')

            if not row:
               continue 
            prices[str(row[0])] = float(row[1])

        return prices

# Exercison 2.7: Compute the currrent value of the porofolip along with the gain/loss
def make_report(portfolio, prices):
    report = []
    for row in portfolio:
        name = row['name']
        shares = row['shares']
        initial_price = row['price']
        current_price = prices[name]
        chage = current_price - initial_price
        holding = (name, shares, current_price, chage)
        report.append(holding)

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
    portfolio = read_portfolio_a(portfoliofile)
    prices = read_prices(pricesfile)
    report = make_report(portfolio, prices)
    print_report(report)

def main(argv):
    portfolio_report(argv[1], argv[2]) 

if __name__ == '__main__':
    import sys
    main(sys.argv)
