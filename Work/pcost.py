# pcost.py
#
# Exercise 1.27
import sys
import csv

def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)

        header = next(rows)
        for i, row in enumerate(rows, start = 1):
            record = dict(zip(header, row))
            try:
                shares = int(record['shares'])
                price = float(record['price'])
                total_cost += shares * price
            except ValueError:
                print('Row {}: Couldn\'t convert: {}'.format(i, row))
        return total_cost

# Exercise 1.33: Reading from the command line
if len(sys.argv) ==2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost', cost)

# Exercise 1.32: Using a library function
from csv import reader

total_cost = 0.0
with open('Data/portfolio.csv', 'rt') as f:
    rows = reader(f)
    header = next(rows)

    for row in rows:
        shares = int(row[1])
        price = float(row[2])
        total_cost += shares * price
    print(total_cost)
