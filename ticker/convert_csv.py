import csv
import json

with open('ticker.json') as infile:
    j_tickers = json.loads(infile.read())

with open('tickers.csv', 'w', newline='') as outfile:
    f = csv.writer(outfile)
    f.writerow(['Ticker'])
    for ticker in j_tickers:
        for stock in ticker.values():
            f.writerow(stock)