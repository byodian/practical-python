# pcost.py
#
# Exercise 1.27
import sys
import csv

def portfolio_cost(filename):
    total = 0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)

        header = next(rows)
        for i, row in enumerate(rows, start = 1):
            try:
                shares = int(row[1])
                price = float(row[2])
                total += shares * price
            except ValueError:
                print('Row {}: Couldn\'t convert: {}'.format(i, row))
        return total

# Exercise 1.33: Reading from the command line
if len(sys.argv) ==2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost', cost)

# Exercise 1.32: Using a library function
from csv import reader

total = 0
with open('Data/portfolio.csv', 'rt') as f:
    rows = reader(f)
    header = next(rows)

    for row in rows:
        shares = int(row[1])
        price = float(row[2])
        total += shares * price
    print(total)
