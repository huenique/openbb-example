"""
This type stub file was generated by pyright.
"""

from typing import Optional, Union
from pandas.core.frame import DataFrame
from openbb_terminal import OpenBBFigure
from openbb_terminal.decorators import log_start_end

""" Business Insider View """
__docformat__ = ...
logger = ...
@log_start_end(log=logger)
def display_management(symbol: str, export: str = ..., sheet_name: Optional[str] = ...): # -> None:
    """Display company's managers

    Parameters
    ----------
    symbol : str
        Stock ticker symbol
    export : str
        Format to export data
    """
    ...

@log_start_end(log=logger)
def display_price_target_from_analysts(symbol: str, data: Optional[DataFrame] = ..., start_date: Optional[str] = ..., limit: int = ..., raw: bool = ..., export: str = ..., sheet_name: Optional[str] = ..., external_axes: bool = ..., adjust_for_splits: bool = ...) -> Union[OpenBBFigure, None]:
    """Display analysts' price targets for a given stock. [Source: Business Insider]

    Parameters
    ----------
    symbol: str
        Due diligence ticker symbol
    data: Optional[DataFrame]
        Price target DataFrame
    start_date : Optional[str]
        Start date of the stock data, format YYYY-MM-DD
    limit : int
        Number of latest price targets from analysts to print
    raw: bool
        Display raw data only
    sheet_name: str
        Optionally specify the name of the sheet the data is exported to.
    export: str
        Export dataframe data to csv,json,xlsx file
    external_axes: bool, optional
        Whether to return the figure object or not, by default False
    adjust_for_splits: bool
        Whether to adjust analyst price targets for stock splits, by default True

    Examples
    --------
    >>> from openbb_terminal.sdk import openbb
    >>> openbb.stocks.fa.pt_chart(symbol="AAPL")
    """
    ...

@log_start_end(log=logger)
def display_estimates(symbol: str, estimate: str, export: str = ..., sheet_name: Optional[str] = ...): # -> None:
    """Display analysts' estimates for a given ticker. [Source: Business Insider]

    Parameters
    ----------
    symbol : str
        Ticker to get analysts' estimates
    estimate: str
        Type of estimate to get
    export : str
        Export dataframe data to csv,json,xlsx file
    """
    ...
