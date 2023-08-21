"""
This type stub file was generated by pyright.
"""

import pandas as pd
from openbb_terminal.decorators import log_start_end

"""CSIMarket Model"""
__docformat__ = ...
logger = ...
def clean_table(df: pd.DataFrame) -> pd.DataFrame:
    """Clean up the table from CSIMarket

    Parameters
    ----------
    df: pd.DataFrame
        Dataframe to clean

    Returns
    -------
    df: pd.DataFrame
        Cleaned dataframe
    """
    ...

@log_start_end(log=logger)
def get_suppliers(symbol: str) -> pd.DataFrame:
    """Get suppliers from ticker provided. [Source: CSIMarket]

    Parameters
    ----------
    symbol: str
        Ticker to select suppliers from

    Returns
    -------
    pd.DataFrame
        A dataframe of suppliers
    """
    ...

@log_start_end(log=logger)
def get_customers(symbol: str) -> pd.DataFrame:
    """Print customers from ticker provided

    Parameters
    ----------
    symbol: str
        Ticker to select customers from

    Returns
    -------
    pd.DataFrame
        A dataframe of suppliers
    """
    ...
