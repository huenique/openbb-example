"""
This type stub file was generated by pyright.
"""

import pandas as pd
from typing import Optional
from openbb_terminal.decorators import check_api_key, log_start_end

""" Quandl View """
__docformat__ = ...
logger = ...
@log_start_end(log=logger)
@check_api_key(["API_KEY_QUANDL"])
def plot_short_interest(symbol: str, data: pd.DataFrame, nyse: bool = ..., external_axes: bool = ...): # -> OpenBBFigure | None:
    """Plot the short interest of a stock. This corresponds to the
    number of shares that have been sold short but have not yet been
    covered or closed out. Either NASDAQ or NYSE [Source: Quandl]

    Parameters
    ----------
    symbol : str
        ticker to get short interest from
    data: pd.DataFrame
        Short interest dataframe
    nyse : bool
        data from NYSE if true, otherwise NASDAQ
    external_axes : bool, optional
        Whether to return the figure object or not, by default False
    """
    ...

@log_start_end(log=logger)
@check_api_key(["API_KEY_QUANDL"])
def short_interest(symbol: str, nyse: bool = ..., limit: int = ..., raw: bool = ..., export: str = ..., sheet_name: Optional[str] = ..., external_axes: bool = ...): # -> OpenBBFigure | None:
    """Plot the short interest of a stock. This corresponds to the
    number of shares that have been sold short but have not yet been
    covered or closed out. Either NASDAQ or NYSE [Source: Quandl]

    Parameters
    ----------
    symbol : str
        ticker to get short interest from
    nyse : bool
        data from NYSE if true, otherwise NASDAQ
    limit: int
        Number of past days to show short interest
    raw : bool
        Flag to print raw data instead
    export : str
        Export dataframe data to csv,json,xlsx file
    external_axes : bool, optional
        Whether to return the figure object or not, by default False
    """
    ...
