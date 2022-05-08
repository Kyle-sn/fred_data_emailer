# Fred Data Emailer
The scripts included in this repo coupled with cron jobs will allow the user to progromatically send routine summary emails of data provided by [FRED](https://fred.stlouisfed.org/) to themselves. The end result is a table like the one seen below.
```
╒═════════════════╤════════════╕
│ Date            │ 2021-03-01 │
├─────────────────┼────────────┤
│ Closing value   │ 3901.82    │
├─────────────────┼────────────┤
│ Notional change │ 90.67      │
├─────────────────┼────────────┤
│ Percent change  │ 2.38       │
╘═════════════════╧════════════╛
```

## Motivation
Although I work in the finance industry, I am not always able to follow the markets and economy as closely as I would like and so I created this collection of scripts to keep myself updated with various data points provided by FRED. Regardless of what occupies my time during the day, I will be able to stay up to date with whatever data points I decide to setup using this library.

## Assumptions
- An AWS server is hosting the repo and emails are being sent using Amazon SES. 
- The shell scripts assume the user is storing the repo in their home directory on a linux host.
- Before using amazon_ses.py, the user needs to enter the sender's email address, the receiver's email address, and the AWS region the user is using for Amazon SES.
- Data is assumed to be located in /data/fred_data/ located in the user's home directory on a linux host.

## Workflow
### Initial Setup
The first script that needs to be ran is `get_fred_data.py`, and it should be ran with a timeframe that returns at least two data points so that notional and percentage changes can be calculated downstream. Argument explanations:
- `symbol`: the symbol that FRED uses to identify the data point the user is trying to download (i.e. `sp500` is the identifier for the [S&P 500 Index](https://fred.stlouisfed.org/series/SP500) and `DGS10` is the identifier for [10-Year Treasury Constant Maturity Rate](https://fred.stlouisfed.org/series/DGS10)).
- `file_name`: should be `<symbol>.csv` 
- `start_date`: first day of data to be returned. Formatted as `YYYYMMDD`.
- `end_date`: last day of data to be returned. Formatted as `YYYYMMDD`.

An example command:`get_fred_data.py --symbol=sp500 --file_name=sp500.csv --start_date=20210101 --end_date=20210301`

Once the starting data is now saved, the user will need to run `replace_null.py`, which replaces any null values with the value from the previous day. This is needed because FRED does not return a data point on holidays. Argument explanations:
- `symbol`: the symbol the user downloaded data for.
- `file_name`: the name of the file that the downloaded data is stored as.

An example command: `replace_null.py --symbol=sp500 --file_name=sp500.csv`

### Scheduled Routines
Now the user has clean data that can be used for scheduled routines. The user now needs to add the below cronjobs. Once these are in place, the user will then be able to start receiving daily summaries sent to their email that look like the table found at the top of this document.
```
# Download data from https://fred.stlouisfed.org/
5 19 * * 1-5 sh /home/<username>/get_fred_data/shell/get_fred_data.sh

# Append downloaded data to the consolidated data file
6 19 * * 1-5 sh /home/<username>/get_fred_data/shell/append_csv.sh

# Remove null values in case there was a trading holiday
7 19 * * 1-5 sh /home/<username>/get_fred_data/shell/replace_null.sh

# Calculate summary data
8 19 * * 1-5 sh /home/<username>/get_fred_data/shell/summary_calc.sh
```

## Future Scope
- Add holiday logic so emails are not sent on days where it is expected to be missing data.
- Create a tool to determine when certain data points are usually available on FRED.
- Create cleanup scripts to cleanup old logs and summary files.
