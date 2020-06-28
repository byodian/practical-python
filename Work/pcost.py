# pcost.py
#
# Exercise 1.27
import sys

def protfolio_cost(filename):
    total = 0
    with open(filename, 'rt') as f:
        header = next(f)
        for line in f:
            try:
                line_list = line.split(',')
                shares = int(line_list[1])
                price = float(line_list[2])
                total += shares * price
            except ValueError:
                print('ValueError')
        return total
# Exercise 1.33: Reading from the command line
if len(sys.argv) ==2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = protfolio_cost(filename)
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
