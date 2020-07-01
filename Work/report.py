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
