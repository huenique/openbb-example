"""
This type stub file was generated by pyright.
"""

from typing import Optional
from openbb_terminal.decorators import log_start_end

"""Substack View"""
__docformat__ = ...
logger = ...
@log_start_end(log=logger)
def display_newsletters(limit: int = ..., export: str = ..., sheet_name: Optional[str] = ...) -> None:
    """Prints table showing DeFi related substack newsletters.
    [Source: substack.com]

    Parameters
    ----------
    limit: int
        Number of records to display
    export : str
        Export dataframe data to csv,json,xlsx file
    """
    ...

