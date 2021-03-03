# Fred Data Emailer
The scripts included in this repo coupled with cron jobs will allow the user to progromatically send routine summary emails of data provided by FRED to themselves. The end result is a table line the one seen below.
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

## Motivation (WIP)
Although I work in the finance industry, I am not always able to follow the markets and economy as closely as I would like and so I created this collection of scripts to keep myself updated with various data points provided by FRED.

## Assumptions & Setup (WIP)
The shell scripts assume the user is storing the repo in their home directory on a linux host.

Before using amazon_ses.py, the user needs to enter the sender's email address, the receiver's email address, and the AWS region the user is using for Amazon SES.

various scripts assume the data being used is located in /data/fred_data/ located in the user's home directory

## Workflow (WIP)
