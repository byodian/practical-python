# fileparse.py
#
# Exercise 3.3
import csv
def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of recorsa
    '''
    if select and not has_headers:
        raise RuntimeError('select require column headers')

    if not isinstance(lines, str):

        rows = csv.reader(lines, delimiter=delimiter)

        # Read the file headers (if any)
        headers = next(rows) if has_headers else []

        # If a column selector was given, find indices of the specified columns
        # Also narrow the set of headers used for resulting dicrionaies
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select

        records = []
        for i, row in enumerate(rows, start=1):
            if not row:       # Skip rows with no data
                continue

            # Filter row if the specified columns were selected
            if select:
                row = [row[index] for index in indices]

            # Type conversion
            if types:
                try:
                    row = [ func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    if not silence_errors:
                        print('Row {}: Could\'t convert {}'.format(i,row))
                        print('Row %i:' %i, e)
                    continue

            # Make a dictionary or a tuple
            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

        return records
