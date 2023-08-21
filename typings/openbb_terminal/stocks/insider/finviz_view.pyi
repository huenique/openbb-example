"""
This type stub file was generated by pyright.
"""

from typing import Optional
from openbb_terminal.decorators import log_start_end

""" Finviz View """
__docformat__ = ...
logger = ...
@log_start_end(log=logger)
def last_insider_activity(symbol: str, limit: int = ..., export: str = ..., sheet_name: Optional[str] = ...): # -> None:
    """Display insider activity for a given stock ticker. [Source: Finviz]

    Parameters
    ----------
    symbol : str
        Stock ticker symbol
    limit : int
        Number of latest insider activity to display
    export : str
        Export dataframe data to csv,json,xlsx file
    """
    ...
