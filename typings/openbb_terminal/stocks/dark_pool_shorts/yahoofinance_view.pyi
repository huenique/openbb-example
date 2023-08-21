"""
This type stub file was generated by pyright.
"""

from typing import Optional
from openbb_terminal.decorators import log_start_end

""" Yahoo Finance View """
__docformat__ = ...
logger = ...
@log_start_end(log=logger)
def display_most_shorted(limit: int = ..., export: str = ..., sheet_name: Optional[str] = ...): # -> None:
    """Display most shorted stocks screener. [Source: Yahoo Finance]

    Parameters
    ----------
    limit: int
        Number of stocks to display
    export : str
        Export dataframe data to csv,json,xlsx file
    """
    ...
