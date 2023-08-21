"""
This type stub file was generated by pyright.
"""

import pandas as pd
from typing import List, Optional
from openbb_terminal.decorators import log_start_end

"""Yahoo Finance model"""
__docformat__ = ...
logger = ...
FUTURES_DATA = ...
MONTHS = ...
class HiddenPrints:
    def __enter__(self): # -> None:
        ...
    
    def __exit__(self, exc_type, exc_val, exc_tb): # -> None:
        ...
    


@log_start_end(log=logger)
def get_search_futures(category: str = ..., exchange: str = ..., description: str = ...): # -> DataFrame:
    """Get search futures [Source: Yahoo Finance]

    Parameters
    ----------
    category: str
        Select the category where the future exists
    exchange: str
        Select the exchange where the future exists
    description: str
        Select the description where the future exists
    """
    ...

@log_start_end(log=logger)
def get_historical_futures(symbols: List[str], expiry: str = ..., start_date: Optional[str] = ..., end_date: Optional[str] = ...) -> pd.DataFrame:
    """Get historical futures [Source: Yahoo Finance]

    Parameters
    ----------
    symbols: List[str]
        List of future timeseries symbols to display
    expiry: str
        Future expiry date with format YYYY-MM
    start_date: Optional[str]
        Start date of the historical data with format YYYY-MM-DD
    end_date: Optional[str]
        End date of the historical data with format YYYY-MM-DD

    Returns
    -------
    pd.DataFrame
        Historical futures data
    """
    ...

@log_start_end(log=logger)
def get_curve_futures(symbol: str = ..., date: Optional[str] = ...) -> pd.DataFrame:
    """Get curve futures [Source: Yahoo Finance]

    Parameters
    ----------
    symbol: str
        symbol to get forward curve
    date: str
        optionally include historical price for each contract

    Returns
    -------
    pd.DataFrame
        Dictionary with sector weightings allocation
    """
    ...
