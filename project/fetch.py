"""
This file is used to load training data into the program.

Originally created by Reece Turner, 22036698.
"""

import os
import sys

from datetime import datetime

import yfinance as yf
import pandas as pd

current_directory = os.path.dirname(os.path.abspath(__file__))
current_directory += "/"

ERROR_COMMAND_MESSAGE = "Invalid Command. " + \
    "Use 'python data/fetch_data.py <TICKER> [START_DATE] [END_DATE]'."
ERROR_FETCHING_DATA_MESSAGE = "An exception occured trying to download " + \
    "data from https://finance.yahoo.com/."

FETCH_MESSAGE = "Fetching the requested data from https://finance.yahoo.com/"
COMPLETED_MESSAGE = "Requested data has been downloaded. " + \
    "Go to the '.csv' to view it."

DEFAULT_START_DATE = "2020-03-08"
DEFAULT_INTERVAL = "1d"


def get_market_data(args: sys.argv) -> pd.DataFrame:
    """
    Get publicly available market data from Yahoo Finance.
    """

    ticker = args[0]
    if len(args) > 1:
        start_date = args[1]
        end_date = args[2]

        # If an interval is specified use this, otherwise default is used
        if args[3]:
            interval = args[3]
        else:
            interval = DEFAULT_INTERVAL

        # Retrieve data from custom starting date to todays date
        if ticker and start_date and end_date:
            constraint_data = yf.download(
                tickers=ticker,
                start=start_date,
                end=end_date,
                interval=interval
            )
            return constraint_data

    if len(args) == 1:
        default_data = yf.download(
            tickers=ticker,
            start=DEFAULT_START_DATE,
            end=f"{datetime.now().strftime('%Y-%m-%d')}",
            interval=DEFAULT_INTERVAL
        )
    return default_data


if __name__ == "__main__":
    arguments = sys.argv[1:]
    print(FETCH_MESSAGE)
    if len(arguments) < 1:
        print(ERROR_COMMAND_MESSAGE)
    else:
        data = get_market_data(arguments)
        data.to_csv(current_directory + "raw_data/" + f"{arguments[0]}.csv")
