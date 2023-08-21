"""
This type stub file was generated by pyright.
"""

import pandas as pd
from typing import Any, Dict, List
from openbb_terminal.decorators import log_start_end

"""Finviz Model"""
__docformat__ = ...
logger = ...
@log_start_end(log=logger)
def get_data(symbol: str) -> pd.DataFrame:
    """Get fundamental data from finviz

    Parameters
    ----------
    symbol : str
        Stock ticker symbol

    Returns
    -------
    pd.DataFrame
        DataFrame of fundamental data

    Examples
    --------
    >>> from openbb_terminal.sdk import openbb
    >>> openbb.stocks.fa.data("IWV")
    """
    ...

@log_start_end(log=logger)
def get_analyst_data(symbol: str) -> pd.DataFrame:
    """Get analyst data. [Source: Finviz]

    Parameters
    ----------
    symbol : str
        Stock ticker symbol

    Returns
    -------
    df_fa: DataFrame
        Analyst price targets
    """
    ...

def get_analyst_price_targets_workaround(ticker: str, last_ratings: int = ...) -> List[Dict]:
    """Patch the analyst price targets function from finviz

    Parameters
    ----------
    ticker: str
        Ticker symbol
    last_ratings: int
        Number to get

    """
    ...

@log_start_end(log=logger)
def get_news(symbol: str) -> List[Any]:
    """Get news from Finviz

    Parameters
    ----------
    symbol : str
        Stock ticker symbol

    Returns
    -------
    List[Any]
        News
    """
    ...

