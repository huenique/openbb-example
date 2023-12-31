"""
This type stub file was generated by pyright.
"""

import pandas as pd
from typing import Optional, Union
from openbb_terminal import OpenBBFigure
from openbb_terminal.decorators import log_start_end

"""Chartexchange view"""
__docformat__ = ...
logger = ...
@log_start_end(log=logger)
def plot_chart(df: pd.DataFrame, option_type: str, symbol: str, price: float) -> OpenBBFigure:
    """Plot Candlestick chart

    Parameters
    ----------
    df : pd.DataFrame
        Dataframe with OHLC data
    option_type : str
        Type of option (call or put)
    symbol : str
        Ticker symbol

    Returns
    -------
    OpenBBFigure
        Plotly figure object
    """
    ...

@log_start_end(log=logger)
def display_raw(symbol: str = ..., expiry: str = ..., call: bool = ..., price: float = ..., limit: int = ..., chain_id: Optional[str] = ..., raw: bool = ..., export: str = ..., sheet_name: Optional[str] = ..., external_axes: bool = ...) -> Union[OpenBBFigure, None]:
    """Return raw stock data[chartexchange]

    Parameters
    ----------
    symbol : str
        Ticker symbol for the given option
    expiry : str
        The expiry of expiration, format "YYYY-MM-DD", i.e. 2010-12-31.
    call : bool
        Whether the underlying asset should be a call or a put
    price : float
        The strike of the expiration
    limit : int
        Number of rows to show
    chain_id: str
        Optional chain id instead of ticker and expiry and strike
    export : str
        Export data as CSV, JSON, XLSX
    external_axes : bool, optional
        Whether to return the figure object or not, by default False
    """
    ...

