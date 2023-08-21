"""
This type stub file was generated by pyright.
"""

import pandas as pd
from datetime import datetime
from typing import List, Optional, Union
from openbb_terminal import OpenBBFigure
from openbb_terminal.decorators import log_start_end

"""TA Overlap View"""
__docformat__ = ...
logger = ...
@log_start_end(log=logger)
def view_ma(data: pd.Series, window: Optional[List[int]] = ..., offset: int = ..., ma_type: str = ..., symbol: str = ..., export: str = ..., sheet_name: Optional[str] = ..., external_axes: bool = ...) -> Union[OpenBBFigure, None]:
    """Plots MA technical indicator

    Parameters
    ----------
    data: pd.Series
        Series of prices
    window: List[int]
        Length of EMA window
    offset: int
        Offset variable
    ma_type: str
        Type of moving average.  Either "EMA" "ZLMA" or "SMA"
    symbol: str
        Ticker
    sheet_name: str
        Optionally specify the name of the sheet the data is exported to.
    export: str
        Format to export data
    external_axes : bool, optional
        Whether to return the figure object or not, by default False

    Examples
    --------
    >>> from openbb_terminal.sdk import openbb
    >>> df = openbb.stocks.load("AAPL")
    >>> openbb.ta.ma_chart(data=df["Adj Close"], symbol="AAPL", ma_type="EMA", window=[20, 50, 100])


    >>> from openbb_terminal.sdk import openbb
    >>> spuk_index = openbb.economy.index(indices = ["^SPUK"])
    >>> openbb.ta.ma_chart(data = spuk_index["^SPUK"], symbol = "S&P UK Index", ma_type = "EMA", window = [20, 50, 100])
    """
    ...

@log_start_end(log=logger)
def view_vwap(data: pd.DataFrame, symbol: str = ..., start_date: Optional[datetime] = ..., end_date: Optional[datetime] = ..., offset: int = ..., interval: str = ..., export: str = ..., sheet_name: Optional[str] = ..., external_axes: bool = ...) -> Union[OpenBBFigure, None]:
    """Plots VWMA technical indicator

    Parameters
    ----------
    data : pd.DataFrame
        Dataframe of OHLC prices
    symbol : str
        Ticker
    offset : int
        Offset variable
    start_date: Optional[str]
        Initial date, format YYYY-MM-DD
    end_date: Optional[str]
        Final date, format YYYY-MM-DD
    interval : str
        Interval of data
    export : str
        Format to export data
    external_axes : bool, optional
        Whether to return the figure object or not, by default False
    """
    ...

