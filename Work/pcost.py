# pcost.py
#
# Exercise 1.27
import os
from csv import reader

total = 0
with open('Data/portfolio.csv', 'r') as f:
   csv_reader = reader(f)
   header = next(csv_reader)

   if header != None:
       for row in csv_reader:
            share = int(row[1])
            price = float(row[2])
            total += share * price

print('Total cost', total)
