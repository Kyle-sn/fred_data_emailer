#!/bin/sh

DATEVAR="date +%Y%m%d"

# S&P 500 Index
/usr/bin/python3 $HOME/fred_data_emailer/python/append_csv.py --source_file=sp500.csv --new_file=$($DATEVAR)_sp500.csv > /tmp/cron_logs/append_csv_$($DATEVAR)_sp500.log 2>&1
