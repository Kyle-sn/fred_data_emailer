#!/bin/sh

DATEVAR="date +%Y%m%d"

# S&P 500 Index
/usr/bin/python3 $HOME/fred_data_emailer/python/get_fred_data.py --symbol=sp500 --file_name=$($DATEVAR)_sp500.csv --start_date=$($DATEVAR) --end_date=$($DATEVAR) > /tmp/cron_logs/get_fred_data_$($DATEVAR)_sp500.log 2>&1
