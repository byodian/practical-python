# pcost.py
#
# Exercise 1.27
import os
from csv import reader

def protfolio_cost(filename):
    total = 0
    with open(filename, 'r') as f:
       csv_reader = reader(f)
       header = next(csv_reader)

       if header != None:
           for row in csv_reader:
               try:
                    share = int(row[1])
                    price = float(row[2])
                    total += share * price
               except ValueError:
                    print('ValueError')
    return total

cost1 = protfolio_cost('Data/portfolio.csv')
print('Total cost', cost1)

cost2 = protfolio_cost('Data/missing.csv')
print('Total cost', cost2)
