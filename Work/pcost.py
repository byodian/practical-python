# pcost.py
#
# Exercise 1.27
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

cost = protfolio_cost('Data/portfolio.csv')
print('Total cost', cost)

cost1 = protfolio_cost('Data/missing.csv')
print('Total cost', cost1)
