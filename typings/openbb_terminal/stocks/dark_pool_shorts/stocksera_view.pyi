"""
This type stub file was generated by pyright.
"""

import pandas as pd
from typing import Optional, Union
from openbb_terminal import OpenBBFigure
from openbb_terminal.decorators import check_api_key, log_start_end

""" Stocksera View """
__docformat__ = ...
logger = ...
@log_start_end(log=logger)
def plot_cost_to_borrow(symbol: str, data: pd.DataFrame, external_axes: bool = ...): # -> OpenBBFigure | None:
    """Plot the cost to borrow of a stock. [Source: Stocksera]

    Parameters
    ----------
    symbol : str
        ticker to get cost to borrow from
    data: pd.DataFrame
        Cost to borrow dataframe
    external_axes : bool, optional
        Whether to return the figure object or not, by default False
    """
    ...

@log_start_end(log=logger)
@check_api_key(["API_STOCKSERA_KEY"])
def cost_to_borrow(symbol: str, limit: int = ..., raw: bool = ..., export: str = ..., sheet_name: Optional[str] = ..., external_axes: bool = ...) -> Union[None, OpenBBFigure]:
    """Plot the short interest of a stock. This corresponds to the
    number of shares that have been sold short but have not yet been
    covered or closed out. Either NASDAQ or NYSE [Source: Quandl]
    Parameters
    ----------
    symbol : str
        ticker to get cost to borrow from
    limit: int
        Number of historical cost to borrow data to show
    raw : bool
        Flag to print raw data instead
    export : str
        Export dataframe data to csv,json,xlsx file
    external_axes : bool, optional
        Whether to return the figure object or not, by default False
    """
    ...
