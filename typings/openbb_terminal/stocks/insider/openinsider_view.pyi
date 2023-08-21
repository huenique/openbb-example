"""
This type stub file was generated by pyright.
"""

from typing import List, Optional
from openbb_terminal.decorators import log_start_end

logger = ...
d_notes = ...
d_trade_types = ...
def lambda_red_highlight(values) -> List[str]:
    """Red highlight

    Parameters
    ----------
    values : List[str]
        dataframe values to color

    Returns
    -------
    List[str]
        colored dataframes values
    """
    ...

def lambda_yellow_highlight(values) -> List[str]:
    """Yellow highlight

    Parameters
    ----------
    values : List[str]
        dataframe values to color

    Returns
    -------
    List[str]
        colored dataframes values
    """
    ...

def lambda_magenta_highlight(values): # -> list[str]:
    """Magenta highlight

    Parameters
    ----------
    values : List[str]
        dataframe values to color

    Returns
    -------
    List[str]
        colored dataframes values
    """
    ...

def lambda_green_highlight(values): # -> list[str]:
    """Green highlight

    Parameters
    ----------
    values : List[str]
        dataframe values to color

    Returns
    -------
    List[str]
        colored dataframes values
    """
    ...

@log_start_end(log=logger)
def print_insider_data(type_insider: str = ..., limit: int = ..., export: str = ..., sheet_name: Optional[str] = ...): # -> None:
    """Print insider data

    Parameters
    ----------
    type_insider: str
        Insider type of data. Available types can be accessed through get_insider_types().
    limit: int
        Limit of data rows to display
    sheet_name: str
        Optionally specify the name of the sheet the data is exported to.
    export: str
        Export data format
    """
    ...

@log_start_end(log=logger)
def print_insider_filter(preset: str, symbol: str, limit: int = ..., links: bool = ..., export: str = ..., sheet_name: Optional[str] = ...) -> None:
    """Print insider filter based on loaded preset. [Source: OpenInsider]

    Parameters
    ----------
    preset : str
        Loaded preset filter
    symbol : str
        Stock ticker symbol
    limit : int
        Limit of rows of data to display
    links : bool
        Flag to show hyperlinks
    export : str
        Format to export data
    """
    ...

