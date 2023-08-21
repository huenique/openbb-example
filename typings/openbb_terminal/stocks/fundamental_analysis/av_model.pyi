"""
This type stub file was generated by pyright.
"""

import pandas as pd
from typing import Dict, List
from openbb_terminal.decorators import log_start_end

"""Alpha Vantage Model"""
__docformat__ = ...
logger = ...
def check_premium_key(json_response: Dict) -> bool:
    """Checks if the response is the premium endpoint"""
    ...

@log_start_end(log=logger)
def get_overview(symbol: str) -> pd.DataFrame:
    """Get alpha vantage company overview

    Parameters
    ----------
    symbol : str
        Stock ticker symbol

    Returns
    -------
    pd.DataFrame
        Dataframe of fundamentals
    """
    ...

@log_start_end(log=logger)
def get_key_metrics(symbol: str) -> pd.DataFrame:
    """Get key metrics from overview

    Parameters
    ----------
    symbol : str
        Stock ticker symbol

    Returns
    -------
    pd.DataFrame
        Dataframe of key metrics
    """
    ...

@log_start_end(log=logger)
def get_income_statements(symbol: str, limit: int = ..., quarterly: bool = ..., ratios: bool = ..., plot: bool = ...) -> pd.DataFrame:
    """Get income statements for company

    Parameters
    ----------
    symbol : str
        Stock ticker symbol
    limit : int
        Number of past to get
    quarterly : bool, optional
        Flag to get quarterly instead of annual, by default False
    ratios: bool
        Shows percentage change, by default False
    plot: bool
        If the data shall be formatted ready to plot

    Returns
    -------
    pd.DataFrame
        DataFrame of income statements
    """
    ...

@log_start_end(log=logger)
def get_balance_sheet(symbol: str, limit: int = ..., quarterly: bool = ..., ratios: bool = ..., plot: bool = ...) -> pd.DataFrame:
    """Get balance sheets for company

    Parameters
    ----------
    symbol : str
        Stock ticker symbol
    limit : int
        Number of past to get
    quarterly : bool, optional
        Flag to get quarterly instead of annual, by default False
    ratios: bool
        Shows percentage change, by default False
    plot: bool
        If the data shall be formatted ready to plot

    Returns
    -------
    pd.DataFrame
        DataFrame of the balance sheet
    """
    ...

@log_start_end(log=logger)
def get_cash_flow(symbol: str, limit: int = ..., quarterly: bool = ..., ratios: bool = ..., plot: bool = ...) -> pd.DataFrame:
    """Get cash flows for company

    Parameters
    ----------
    symbol : str
        Stock ticker symbol
    limit : int
        Number of past to get
    quarterly : bool, optional
        Flag to get quarterly instead of annual, by default False
    ratios: bool
        Shows percentage change, by default False
    plot: bool
        If the data shall be formatted ready to plot

    Returns
    -------
    pd.DataFrame
        Dataframe of cash flow statements
    """
    ...

@log_start_end(log=logger)
def get_earnings(symbol: str, quarterly: bool = ...) -> pd.DataFrame:
    """Get earnings calendar for ticker

    Parameters
    ----------
    symbol : str
        Stock ticker symbol
    quarterly : bool, optional
        Flag to get quarterly and not annual, by default False

    Returns
    -------
    pd.DataFrame
        Dataframe of earnings
    """
    ...

def df_values(df: pd.DataFrame, item: str, index: int = ..., length: int = ...) -> List[int]:
    """Clean the values from the df

    Parameters
    ----------
    df : pd.DataFrame
        The Dataframe to use
    item : str
        The item to select
    index : int
        The number of row to display
    length : int
        The number of rows to return

    Returns
    -------
    values : List[int]
        The values for the dataframe
    """
    ...

def replace_df(name: str, row: pd.Series) -> pd.Series:
    """Replaces text in pandas row based on color functions

    Return
    ----------
    name : str
        The name of the row
    row : pd.Series
        The original row

    Parameters
    ----------
    new_row : pd.Series
        The new formatted row
    """
    ...

def color_mscore(value: str) -> str:
    """Adds color to mscore dataframe values

    Parameters
    ----------
    value : str
        The string value

    Returns
    -------
    new_value : str
        The string formatted with rich color
    """
    ...

def color_zscore_mckee(value: str) -> str:
    """Adds color to mckee or zscore dataframe values
    Parameters
    ----------
    value : str
        The string value

    Returns
    -------
    new_value : str
        The string formatted with rich color
    """
    ...

@log_start_end(log=logger)
def get_fraud_ratios(symbol: str, detail: bool = ...) -> pd.DataFrame:
    """Get fraud ratios based on fundamentals

    Parameters
    ----------
    symbol : str
        Stock ticker symbol
    detail : bool
        Whether to provide extra m-score details

    Returns
    -------
    metrics : pd.DataFrame
        The fraud ratios
    """
    ...

@log_start_end(log=logger)
def get_dupont(symbol: str) -> pd.DataFrame:
    """Get dupont ratios

    Parameters
    ----------
    symbol : str
        Stock ticker symbol

    Returns
    -------
    dupont : pd.DataFrame
        The dupont ratio breakdown
    """
    ...
