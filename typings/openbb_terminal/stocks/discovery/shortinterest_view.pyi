"""
This type stub file was generated by pyright.
"""

from typing import Optional
from openbb_terminal.decorators import log_start_end

""" Short Interest View """
__docformat__ = ...
logger = ...
@log_start_end(log=logger)
def low_float(limit: int = ..., export: str = ..., sheet_name: Optional[str] = ...): # -> None:
    """Prints top N low float stocks from https://www.lowfloat.com

    Parameters
    ----------
    limit: int
        Number of stocks to display
    export : str
        Export dataframe data to csv,json,xlsx file
    """
    ...

@log_start_end(log=logger)
def hot_penny_stocks(limit: int = ..., export: str = ..., sheet_name: Optional[str] = ..., source: str = ...): # -> None:
    """Prints top N hot penny stocks from https://www.pennystockflow.com
    Parameters
    ----------
    limit: int
        Number of stocks to display
    export : str
        Export dataframe data to csv,json,xlsx file
    source : str
        Where to get the data from. Choose from - YahooFinance or Shortinterest
    """
    ...

