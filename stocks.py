import sys
import configparser

import numpy as np
import quandl

SOURCE = 'WIKI'
DAYS = 5

CFG_PATH = 'stocks.cfg'
CSV_PATH = 'stocks.csv'

def read_csv(path):
    try:
        with open(path, 'r') as csv:
            fileDat = [x.split(',') for x in csv.readlines()]
    except OSError as e:
        print('Failed to read csv.')
        return None

    return fileDat

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) != 1:
        print('Requires 1 argument.')
    else:
        config = configparser.ConfigParser()
        config.read(CFG_PATH)
        quandl.ApiConfig.api_key = config['api']['api key']
        csv_stocks = read_csv(CSV_PATH)
        total_dollars = float(args[0])
        ratio_total = sum([int(x[1]) for x in csv_stocks])

        invest_names = []
        invest_dollars = []
        invest_shares = []

        for stock, ratio in csv_stocks:
            _, _, hi, lo, _, _, _, _, _, _, _, _, _ = zip(*quandl.get('%s/%s' % (SOURCE, stock), rows=DAYS, returns='numpy'))
            mean_price = np.mean(hi + lo)
            dollars = total_dollars * int(ratio) / ratio_total
            print('%s averaged $%0.2f per share over the last %d %s.' % (stock, mean_price, DAYS, 'day' if DAYS == 1 else 'days'))
            invest_names.append(stock)
            invest_dollars.append(dollars)
            invest_shares.append(dollars / mean_price)

        print('\nDollar Cost Averaging Advice:')

        for name in invest_names:
            print(name, end='\t\t')

        print()

        for dollars in invest_dollars:
            print('$%0.2f' % dollars, end='\t')

        print()

        for shares in invest_shares:
            print('%0.2f shares' % shares, end='\t')

        print()