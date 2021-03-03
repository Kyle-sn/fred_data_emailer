#!/usr/bin/python3

import pandas as pd  
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--symbol', type=str, required=True, help='The FRED symbol in the data')
parser.add_argument('--file_name', type=str, required=True, help='The name of the file')
args = parser.parse_args()

os.chdir(os.path.expanduser('~/data/fred_data'))

def replace_null(symbol, file_name):
    
    null_value = pd.read_csv(file_name, index_col=False)
    null_value[symbol].fillna(method ='pad', inplace=True)  
    null_value.to_csv(file_name, index=False)

replace_null(args.symbol, args.file_name) 