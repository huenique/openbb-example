"""
This type stub file was generated by pyright.
"""

from typing import List, Optional
from openbb_terminal.decorators import log_start_end

"""StockAnalysis.com view functions"""
__docformat__ = ...
logger = ...
@log_start_end(log=logger)
def view_overview(symbol: str, export: str = ..., sheet_name: Optional[str] = ...): # -> None:
    """Print etf overview information

    Parameters
    ----------
    symbol:str
        ETF symbols to display overview for
    export:str
        Format to export data
    """
    ...

@log_start_end(log=logger)
def view_holdings(symbol: str, limit: int = ..., export: str = ..., sheet_name: Optional[str] = ...): # -> None:
    """

    Parameters
    ----------
    symbol: str
        ETF symbol to show holdings for
    limit: int
        Number of holdings to show
    sheet_name: str
        Optionally specify the name of the sheet the data is exported to.
    export: str
        Format to export data
    """
    ...

@log_start_end(log=logger)
def view_comparisons(symbols: List[str], export: str = ..., sheet_name: Optional[str] = ...): # -> None:
    """Show ETF comparisons

    Parameters
    ----------
    symbols: List[str]
        List of ETF symbols
    sheet_name: str
        Optionally specify the name of the sheet the data is exported to.
    export: str
        Format to export data
    """
    ...

@log_start_end(log=logger)
def display_etf_by_name(name: str, limit: int = ..., export: str = ..., sheet_name: Optional[str] = ...): # -> None:
    """Display ETFs matching search string. [Source: StockAnalysis]

    Parameters
    ----------
    name: str
        String being matched
    limit: int
        Limit of ETFs to display
    sheet_name: str
        Optionally specify the name of the sheet the data is exported to.
    export: str
        Export to given file type

    """
    ...
