class TableFormatter:
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end = ' ')
        print()
        print(('-' * 10 + ' ') * len(headers))

    def row(self, rowdata):
        for row in rowdata:
            print(f'{row:>10s}', end = ' ')
        print()


class CSVTableFormatter:
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter:
    def headings(self, headers):
        thead = ''
        for h in headers:
            thead += '<th>{}</th>'.format(str(h))

        print('<tr>{}</tr>'.format(thead)

    def row(self, rowdata):
        td = ''
        for row in rowdata:
            td += '<td>{}</td>'.format(row)
        print('<tr>{}</tr>'.format(td))
