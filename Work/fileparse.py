# fileparse.py
#
# Exercise 3.3
import csv
def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of recorsa
    '''
    if not isinstance(lines, str):

        rows = csv.reader(lines)

        if has_headers:
            # Read the file headers
            headers = next(rows)

        # If a column selector was given, find indices of the specified columns
        # Also narrow the set of headers used for resulting dicrionaies
        if select and has_headers:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []
        for i, row in enumerate(rows, start=1):
            if not row:       # Skip rows with no data
                continue
            # Filter row if the specified columns were selected
            if indices:
                row = [row[index] for index in indices]

            # Type conversion
            if types:
                try:
                    row = [ func(val) for func, val in zip(types, row)]
                except Exception as e:
                    if not silence_errors:
                        print('Row {}: Could\'t convert {}'.format(i,row))
                        print('Row %i:' %i, e)
                    continue

            if has_headers:
                # Make a dictionary
                record = dict(zip(headers, row))
                records.append(record)
            else:
                # Make a list
                records.append(tuple(row))
        return records
