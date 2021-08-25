import pandas as pd 
import os
import argparse
import tabulate

parser = argparse.ArgumentParser()
parser.add_argument('--symbol', type=str, required=True, help='The symbol to be summarized')
args = parser.parse_args()

os.chdir(os.path.expanduser('~/data/fred_data'))

def calculation(symbol):
    data = pd.read_csv(f'{symbol}.csv')

    # Trade date
    t_date = data['DATE'].iloc[-1]
    print(f'Trade date: {t_date}')

    # Trade date closing value
    t_date_close = data[symbol].iloc[-1]
    print(f'{t_date} value: {t_date_close}')

    # Trade date notional change
    t_date_notional_change = t_date_close - data[symbol].iloc[-2]
    t_date_notional_change = round(t_date_notional_change, 2)
    print(f'{t_date} notional change: {t_date_notional_change}')

    # Trade date percentage change
    t_date_pct_change = (t_date_notional_change / data[symbol].iloc[-2]) * 100
    t_date_pct_change = round(t_date_pct_change, 2)
    print(f'{t_date} percentage change: {t_date_pct_change}')
    
    file = open(f'{symbol}_summary.txt', 'w')
    file.write(f'''
Field,Value
Date,{t_date}
Closing value,{t_date_close}
Notional change,{t_date_notional_change}
Percent change,{t_date_pct_change} 
        ''')
    file.close()
    print(f'Writing data to ~/data/fred_data/{symbol}_summary.txt')

def tabulate_dict(symbol):
    tabulate.PRESERVE_WHITESPACE = True
    data = pd.read_csv(f'{symbol}_summary.txt')
    data.set_index('Field', inplace=True, drop=True)

    table = tabulate.tabulate(data,tablefmt='fancy_grid', stralign='left')
    
    file = open(f'{symbol}_table.txt', 'w')
    file.write(table)
    file.close()
    print(f'Writing the summary data to ~/data/fred_data/{symbol}_table.txt')

def main():
    calculation(args.symbol)
    tabulate_dict(args.symbol)
