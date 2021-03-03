#!/bin/sh

DATEVAR="date +%Y%m%d"

# S&P 500 Index
/usr/bin/python3 $HOME/fred_data_emailer/python/amazon_ses.py --date=$($DATEVAR) --symbol=sp500 > /tmp/cron_logs/amazon_ses_$($DATEVAR)_sp500.log 2>&1
