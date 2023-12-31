"""
This type stub file was generated by pyright.
"""

import pandas as pd
from openbb_terminal.decorators import log_start_end

"""Stocks Trading Hours Model."""
logger = ...
@log_start_end(log=logger)
def get_bursa(symbol: str) -> pd.DataFrame:
    """Get current exchange open hours.

    Parameters
    ----------
    symbol : str
        Exchange symbol

    Returns
    -------
    pd.DataFrame
        Exchange info
    """
    ...

@log_start_end(log=logger)
def get_open() -> pd.DataFrame:
    """Get open exchanges.

    Parameters
    ----------

    Returns
    -------
    pd.DataFrame
        Currently open exchanges
    """
    ...

@log_start_end(log=logger)
def get_closed() -> pd.DataFrame:
    """Get closed exchanges.

    Parameters
    ----------

    Returns
    -------
    pd.DataFrame
        Currently closed exchanges
    """
    ...

@log_start_end(log=logger)
def get_all() -> pd.DataFrame:
    """Get all exchanges.

    Parameters
    ----------

    Returns
    -------
    pd.DataFrame
        All available exchanges
    """
    ...

@log_start_end(log=logger)
def get_all_exchange_short_names() -> pd.DataFrame:
    """Get all exchanges short names.

    Parameters
    ----------

    Returns
    -------
    pd.DataFrame
        All available exchanges short names
    """
    ...

@log_start_end(log=logger)
def all_bursa(): # -> DataFrame:
    """Get all exchanges from dictionary

    Parameters
    __________

    Returns
    _______
    pd.DataFrame
        All exchanges
    """
    ...

def check_if_open(bursa: pd.DataFrame, exchange: str) -> bool:
    """Check if market open helper function

    Parameters
    __________
    bursa : pd.DataFrame
        pd.DataFrame of all exchanges
    exchange : str
        bursa pd.DataFrame index value for exchange

    Returns
    _______
    bool
        If market is open
    """
    ...

