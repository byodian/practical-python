# fileparse.py
#
# Exercise 3.3
import csv
def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=None):
    '''
    Parse a CSV file into a list of recorsa
    '''
    with open(filename) as file:
        rows = csv.reader(file, delimiter=delimiter)

        if has_headers:
            # Read the file headers
            headers = next(rows)

        # If a column selector was given, find indices of the specified columns
        # Also narrow the set of headers used for resulting dicrionaies
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:       # Skip rows with no data
                continue
            # Filter row if the specified columns were selected
            if indices:
                row = [row[index] for index in indices]

            # Type conversion
            if types:
                row = [ func(val) for func, val in zip(types, row)]

            if has_headers:
                # Make a dictionary
                record = dict(zip(headers, row))
                records.append(record)
            else:
                # Make a list
                records.append(tuple(row))
        return records
