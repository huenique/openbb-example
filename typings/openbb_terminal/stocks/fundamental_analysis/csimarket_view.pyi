"""
This type stub file was generated by pyright.
"""

from typing import Optional
from openbb_terminal.decorators import log_start_end

"""CSIMarket View"""
__docformat__ = ...
logger = ...
@log_start_end(log=logger)
def suppliers(symbol: str, export: str = ..., sheet_name: Optional[str] = ..., limit: int = ...) -> None:
    """Display suppliers from ticker provided. [Source: CSIMarket]

    Parameters
    ----------
    symbol: str
        Ticker to select suppliers from
    export : str
        Export dataframe data to csv,json,xlsx file
    limit: int
        The maximum number of rows to show
    """
    ...

@log_start_end(log=logger)
def customers(symbol: str, export: str = ..., sheet_name: Optional[str] = ...): # -> None:
    """Display customers from ticker provided. [Source: CSIMarket]

    Parameters
    ----------
    symbol: str
        Ticker to select customers from
    export : str
        Export dataframe data to csv,json,xlsx file
    """
    ...

