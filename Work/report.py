# report.py
#
# Exercise 2.4: A list of tuples
#import csv
#def read_portfolio(filename):
#    with open(filename, 'rt') as file:
#        portfolio = []
#
#        rows = csv.reader(file)
#        headers = next(rows)
#
#        for row in rows:
#           holding = (row[0], int(row[1]), float(row[2]))
#           portfolio.append(holding)
#
#        return portfolio


# Exercise 2.5: List of Dictionaries
import  csv

def read_portfolio(filename):
    with open(filename, 'rt') as file:
        portfolio = []

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
    with open(filename) as file:
        prices = {}

        rows = csv.reader(file)
        for row in rows:
            #try:
            #   prices[str(row[0])] = row[1]
            #except:
            #    print('Error')

            if not row:
               continue 
            else:
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


portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)

headers = ('name', 'shares', 'price', 'change')
print('%10s %10s %10s %10s' % headers)

s = '---------- '
gap = s * 4
print(gap.strip())

for name, shares, price, change in report:
    print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')
