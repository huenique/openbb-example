"""
This type stub file was generated by pyright.
"""

import pandas as pd
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union
from openpyxl import worksheet
from openbb_terminal.decorators import log_start_end

""" DCF Model """
__docformat__ = ...
logger = ...
CURRENCIES = ...
def string_float(string: str) -> float:
    """Convert a string to a float

    Parameters
    ----------
    string : str
        String to be converted

    Returns
    -------
    number : float
        Analysis of filings text
    """
    ...

def insert_row(name: str, index: str, df: pd.DataFrame, row_v: List[str]) -> pd.DataFrame:
    """Allows a row to be added given an index and name

    Parameters
    ----------
    name : str
        Name to be added to df
    index : str
        The row the new item will go after
    df : pd.DataFrame
        The dataframe to be modified
    row_v : List[str]
        The items to be added to the row

    Returns
    -------
    new_df : pd.DataFrame
        The new dataframe
    """
    ...

def set_cell(ws: worksheet, cell: str, text: Optional[Union[int, str, float]] = ..., font: Optional[str] = ..., border: Optional[str] = ..., fill: Optional[str] = ..., alignment: Optional[str] = ..., num_form: Optional[str] = ...): # -> None:
    """Set the value for a cell

    Parameters
    ----------
    ws : worksheet
        The worksheet to be modified
    cell : str
        The cell that will be modified
    text : Union[int, str, float]
        The new value of the cell
    font : str
        The type of font
    border : str
        The type of border
    fill : str
        The type of fill
    alignment : str
        The type of alignment
    num_form : str
        The format for numbers
    """
    ...

@log_start_end(log=logger)
def get_fama_raw() -> pd.DataFrame:
    """Get Fama French data

    Returns
    -------
    df : pd.DataFrame
        Fama French data
    """
    ...

@log_start_end(log=logger)
def get_historical_5(symbol: str) -> pd.DataFrame:
    """Get 5 year monthly historical performance for a ticker with dividends filtered

    Parameters
    ----------
    symbol: str
        The ticker symbol to be analyzed

    Returns
    -------
    df: pd.DataFrame
        Historical data
    """
    ...

@log_start_end(log=logger)
def get_fama_coe(symbol: str) -> float:
    """Use Fama and French to get the cost of equity for a company

    Parameters
    ----------
    symbol : str
        The ticker symbol to be analyzed

    Returns
    -------
    coef : float
        The stock's Fama French coefficient
    """
    ...

@log_start_end(log=logger)
def others_in_sector(symbol: str, sector: str, industry_group: str, industry: str, no_filter: bool = ...) -> List[str]:
    """Get other stocks in a ticker's sector

    Parameters
    ----------
    symbol: str
        The ticker symbol to be excluded
    sector: str
        The sector to pull from
    industry: str
        The industry to pull from
    no_filter: bool
        True means that we do not filter based on market cap

    Returns
    -------
    List[str]
        List of symbols in the same sector
    """
    ...

def create_dataframe(symbol: str, statement: str, period: str = ...): # -> tuple[DataFrame, None, None] | tuple[Unknown | DataFrame, Literal[1000, 1000000, 1000000000], str]:
    """
    Creates a df financial statement for a given ticker

    Parameters
    ----------
    symbol : str
        The ticker symbol to create a dataframe for
    statement : str
        The financial statement dataframe to create
    period : str
        Whether to look at annual, quarterly, or trailing

    Returns
    -------
    statement : pd.DataFrame
        The financial statement requested
    rounding : int
        The amount of rounding to use
    statement_currency: str
        The currency the financial statements are reported in
    """
    ...

@log_start_end(log=logger)
def get_similar_dfs(symbol: str, info: Dict[str, Any], n: int, no_filter: bool = ...): # -> list[Unknown]:
    """
    Get dataframes for similar companies

    Parameters
    ----------
    symbol : str
        The ticker symbol to create a dataframe for
    into : Dict[str,Any]
        The dictionary based on info collected from fd.Equities()
    n : int
        The number of similar companies to produce
    no_filter : bool
        True means that we do not filter based on market cap

    Returns
    -------
    new_list : List[str, pd.DataFrame]
        A list of similar companies
    """
    ...

@log_start_end(log=logger)
def clean_dataframes(*args) -> List[pd.DataFrame]:
    """
    All dataframes in the list take on the length of the shortest dataframe

    Parameters
    ----------
    *args : List[pd.DataFrame]
        List of dataframes to clean

    Returns
    -------
    dfs : List[pd.DataFrame]
        Cleaned list of dataframes
    """
    ...

@log_start_end(log=logger)
def get_value(df: pd.DataFrame, row: str, column: int) -> Tuple[float, float]:
    """
    Gets a specific value from the dataframe

    Parameters
    ----------
    df : pd.DataFrame
        The dataframe to get the information from
    row : str
        The row to get the information from
    column : int
        The column to get the information from

    Returns
    -------
    value : List[float]
        The information in float format
    """
    ...

def frac(num: float, denom: float) -> Union[str, float]:
    """
    Converts a numerator and a denominator in a fraction, checking for invalid denominators

    Parameters
    ----------
    num : float
        The numerator
    denom : float
        The denominator

    Returns
    -------
    value : Union[str, float]
        The fraction
    """
    ...

@log_start_end(log=logger)
def generate_path(n: int, file_name: str) -> Path:
    """
    Create the path to save an excel file to

    Parameters
    ----------
    n: int
        The try number
    file_name: str
        The name of the file to save

    Returns
    -------
    path: Path
        The path to save a file to
    """
    ...

