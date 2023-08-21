"""
This type stub file was generated by pyright.
"""

import pandas as pd
from typing import List, Tuple
from openbb_terminal.decorators import log_start_end

"""Stockanalysis.com/etf Model"""
__docformat__ = ...
logger = ...
csv_path = ...
@log_start_end(log=logger)
def get_all_names_symbols() -> Tuple[List[str], List[str]]:
    """Gets all etf names and symbols

    Returns
    -------
    Tuple[List[str], List[str]]
        List of all available etf symbols, List of all available etf names
    """
    ...

@log_start_end(log=logger)
def get_etf_overview(symbol: str) -> pd.DataFrame:
    """Get overview data for selected etf

    Parameters
    ----------
    etf_symbol : str
        Etf symbol to get overview for

    Returns
    -------
    df : pd.DataFrame
        Dataframe of stock overview data

    Examples
    --------
    >>> from openbb_terminal.sdk import openbb
    >>> openbb.etf.overview("SPY")
    """
    ...

@log_start_end(log=logger)
def get_etf_holdings(symbol: str) -> pd.DataFrame:
    """Get ETF holdings

    Parameters
    ----------
    symbol: str
        Symbol to get holdings for

    Returns
    -------
    df: pd.DataFrame
        Dataframe of holdings

    Examples
    --------
    >>> from openbb_terminal.sdk import openbb
    >>> openbb.etf.holdings("SPY")
    """
    ...

@log_start_end(log=logger)
def compare_etfs(symbols: List[str]) -> pd.DataFrame:
    """Compare selected ETFs

    Parameters
    ----------
    symbols : List[str]
        ETF symbols to compare

    Returns
    -------
    df_compare : pd.DataFrame
        Dataframe of etf comparisons

    Examples
    --------
    >>> from openbb_terminal.sdk import openbb
    >>> compare_etfs = openbb.etf.compare(["SPY", "QQQ", "IWM"])
    """
    ...

@log_start_end(log=logger)
def get_etfs_by_name(name_to_search: str) -> pd.DataFrame:
    """Get an ETF symbol and name based on ETF string to search. [Source: StockAnalysis]

    Parameters
    ----------
    name_to_search: str
        ETF name to match

    Returns
    -------
    df: pd.Dataframe
        Dataframe with symbols and names
    """
    ...
