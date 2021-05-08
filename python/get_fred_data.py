#!/usr/bin/python3

from helper_functions import fred_data_path
import pandas_datareader.fred as pdr
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--symbol', type=str, required=True, help='The FRED symbol you want data for')
parser.add_argument('--file_name', type=str, required=True, help='The name of the file')
parser.add_argument('--start_date', type=str, required=True, help='The first day of data you want')
parser.add_argument('--end_date', type=str, required=True, help='The last day of data you want (inclusive)')
args = parser.parse_args()

os.chdir(os.path.expanduser('~/data/fred_data'))

def get_fred_data(symbol, file_name, start_date, end_date):
    
    data = pdr.FredReader(symbol, start_date, end_date).read()
    if start_date == end_date:
        print(f'Downloading {symbol} FRED data for date {end_date}')
    
    data.to_csv(file_name)
    print(f'Saving data  to ~/data/fred_data/{file_name}')

get_fred_data(args.symbol, args.file_name, args.start_date, args.end_date)  