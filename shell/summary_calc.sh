#!/bin/sh

DATEVAR="date +%Y%m%d"

# SP 500 Index
/usr/bin/python3 $HOME/fred_data_emailer/python/summary_calc.py --symbol=sp500 > /tmp/cron_logs/summary_calc_$($DATEVAR)_sp500.log 2>&1
