"""
This type stub file was generated by pyright.
"""

from typing import List, Optional
from openbb_terminal.decorators import log_start_end

"""Finviz Comparison View"""
__docformat__ = ...
logger = ...
@log_start_end(log=logger)
def screener(similar: List[str], data_type: str = ..., export: str = ..., sheet_name: Optional[str] = ...): # -> None:
    """Screener.

    Parameters
    ----------
    similar : List[str]
        Similar companies to compare income with.
        Comparable companies can be accessed through
        finnhub_peers(), finviz_peers(), polygon_peers().
    data_type : str
        Screener to use.  One of {overview, valuation, financial, ownership, performance, technical}
    export : str
        Format to export data
    """
    ...
