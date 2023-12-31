"""
This type stub file was generated by pyright.
"""

from typing import Optional
from openbb_terminal.decorators import log_start_end

""" Interactive Broker View """
__docformat__ = ...
logger = ...
@log_start_end(log=logger)
def display_cost_to_borrow(limit: int = ..., export: str = ..., sheet_name: Optional[str] = ...): # -> None:
    """Display stocks with highest cost to borrow. [Source: Interactive Broker]

    Parameters
    ----------
    limit: int
        Number of stocks to display
    export : str
        Export dataframe data to csv,json,xlsx file
    """
    ...

