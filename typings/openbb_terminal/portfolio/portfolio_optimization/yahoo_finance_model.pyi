"""
This type stub file was generated by pyright.
"""

import pandas as pd
from typing import List
from openbb_terminal.decorators import log_start_end

"""YFinance Model"""
__docformat__ = ...
logger = ...
fast_info_map = ...
yf_info_choices = ...
@log_start_end(log=logger)
def process_stocks(symbols: List[str], interval: str = ..., start_date: str = ..., end_date: str = ...) -> pd.DataFrame:
    """Get adjusted closing price for each stock in the list

    Parameters
    ----------
    symbols: List[str]
        List of tickers to get historical data for
    interval: str
        interval to get data from yfinance, personalized
    start_date: str
        If not using interval, start date string (YYYY-MM-DD)
    end_date: str
        If not using interval, end date string (YYYY-MM-DD). If empty use last
        weekday.

    Returns
    -------
    stock_closes: DataFrame
        DataFrame containing daily (adjusted) close prices for each stock in list
    """
    ...

@log_start_end(log=logger)
def process_returns(data: pd.DataFrame, log_returns: bool = ..., freq: str = ..., maxnan: float = ..., threshold: float = ..., method: str = ...) -> pd.DataFrame:
    """Process stock prices to calculate returns and delete outliers

    Parameters
    ----------
    data: pd.DataFrame
        DataFrame of stock prices
    log_returns: bool
        If True calculate log returns, else arithmetic returns. Default value
        is False
    freq: str or int
        The frequency used to calculate returns. Default value is 'D'. Possible
        values are:
            - 'D' for daily returns.
            - 'W' for weekly returns.
            - 'M' for monthly returns.

    maxnan: str or float
        Max percentage of nan values accepted per asset to be included in
        returns
    threshold: str or float
        Value used to replace outliers that are higher to threshold in daily returns.
    method: str
        Method used to fill nan values. Default value is 'time'. For more information see
        `interpolate <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.interpolate.html>`_.

    Returns
    -------
    stock_returns: DataFrame
        DataFrame containing daily (adjusted) close prices for each stock in list
    """
    ...

