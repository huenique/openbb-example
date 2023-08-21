"""
This type stub file was generated by pyright.
"""

import pandas as pd
from typing import Optional, Union
from openbb_terminal import OpenBBFigure
from openbb_terminal.decorators import log_start_end

""" EconDB View """
__docformat__ = ...
logger = ...
@log_start_end(log=logger)
def show_indices(indices: Union[list, pd.DataFrame], interval: str = ..., start_date: Optional[int] = ..., end_date: Optional[int] = ..., column: str = ..., returns: bool = ..., raw: bool = ..., external_axes: bool = ..., export: str = ..., sheet_name: Optional[str] = ..., limit: int = ...) -> Union[pd.DataFrame, OpenBBFigure]:
    """Load (and show) the selected indices over time [Source: Yahoo Finance]
    Parameters
    ----------
    indices: Union[list, pd.DataFrame]
        A list of indices to load in, or a DataFrame with indices as columns (to plot)
        Available indices can be accessed through economy.available_indices().
    interval: str
        Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        Intraday data cannot extend last 60 days
    start_date : str
        The starting date, format "YEAR-MONTH-DAY", i.e. 2010-12-31.
    end_date : str
        The end date, format "YEAR-MONTH-DAY", i.e. 2020-06-05.
    column : str
        Which column to load in, by default this is the Adjusted Close.
    returns: bool
        Flag to show cumulative returns on index
    raw : bool
        Whether to display the raw output.
    external_axes : bool, optional
        Whether to return the figure object or not, by default False
    export : str
        Export data to csv,json,xlsx or png,jpg,pdf,svg file
    Returns
    -------
    Plots the Series.
    """
    ...

@log_start_end(log=logger)
def search_indices(query: list, limit: int = ...): # -> None:
    """Load (and show) the selected indices over time [Source: Yahoo Finance]
    Parameters
    ----------
    query: list
        The keyword you wish to search for. This can include spaces.
    limit: int
        The amount of views you want to show, by default this is set to 10.
    Returns
    -------
    Shows a rich table with the available options.
    """
    ...
