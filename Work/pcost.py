# pcost.py
#
# Exercise 1.27
import csv
import fileparse
import sys

def portfolio_cost(filename):
    total_cost = 0.0

    with open(filename, 'rt') as f:
        rows = fileparse.parse_csv(f, select=['name', 'shares', 'price'],  types=[str, int, float])

        for i, row in enumerate(rows, start = 1):
            try:
                total_cost += row['shares'] * row['price']
            except ValueError:
                print('Row {}: Couldn\'t convert: {}'.format(i, row))
        return total_cost

# Exercise 1.33: Reading from the command line
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost', cost)
