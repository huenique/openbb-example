"""
This type stub file was generated by pyright.
"""

from typing import Any, Dict, List, Optional, Union
from openbb_terminal import OpenBBFigure
from openbb_terminal.decorators import log_start_end

"""Yfinance options view"""
__docformat__ = ...
logger = ...
def header_fmt(header: str) -> str:
    """
    Formats strings to appear as titles

    Parameters
    ----------
    header: str
        The string to be formatted

    Returns
    -------
    new_header: str
        The clean string to use as a header
    """
    ...

@log_start_end(log=logger)
def plot_plot(symbol: str, expiry: str, put: bool = ..., x: str = ..., y: str = ..., custom: str = ..., export: str = ..., sheet_name: Optional[str] = ..., external_axes: bool = ...) -> Union[OpenBBFigure, None]:
    """Generate a graph custom graph based on user input

    Parameters
    ----------
    symbol: str
        Stock ticker symbol
    expiry: str
        Option expiration
    x: str
        variable to display in x axis, choose from:
        ltd, s, lp, b, a, c, pc, v, oi, iv
    y: str
        variable to display in y axis, choose from:
        ltd, s, lp, b, a, c, pc, v, oi, iv
    custom: str
        type of plot
    put: bool
        put option instead of call
    sheet_name: str
        Optionally specify the name of the sheet the data is exported to.
    export: str
        type of data to export
    external_axes : bool, optional
        Whether to return the figure object or not, by default False
    """
    ...

@log_start_end(log=logger)
def plot_payoff(current_price: float, options: List[Dict[Any, Any]], underlying: float, symbol: str, expiry: str, external_axes: bool = ...) -> Union[OpenBBFigure, None]:
    """Generate a graph showing the option payoff diagram"""
    ...

@log_start_end(log=logger)
def plot_expected_prices(und_vals: List[List[float]], p: float, symbol: str, expiry: str, external_axes: bool = ...) -> Union[OpenBBFigure, None]:
    """Plot expected prices of the underlying asset at expiration

    Parameters
    ----------
    und_vals : List[List[float]]
        The expected underlying values at the expiration date
    p : float
        The probability of the stock price moving upward each round
    symbol : str
        The ticker symbol of the option's underlying asset
    expiry : str
        The expiration for the option
    external_axes : bool, optional
        Whether to return the figure object or not, by default False
    """
    ...

@log_start_end(log=logger)
def display_vol_surface(symbol: str, export: str = ..., sheet_name: Optional[str] = ..., z: str = ..., external_axes: bool = ...) -> Union[OpenBBFigure, None]:
    """Display vol surface

    Parameters
    ----------
    symbol : str
        Ticker symbol to get surface for
    export : str
        Format to export data
    z : str
        The variable for the Z axis
    external_axes : bool, optional
        Whether to return the figure object or not, by default False
    """
    ...

@log_start_end(log=logger)
def show_greeks(symbol: str, expiry: str, div_cont: float = ..., rf: Optional[float] = ..., opt_type: int = ..., mini: float = ..., maxi: float = ..., show_all: bool = ...) -> None:
    """
    Shows the greeks for a given option

    Parameters
    ----------
    symbol: str
        The ticker symbol value of the option
    div_cont: float
        The dividend continuous rate
    expiry: str
        The date of expiration, format "YYYY-MM-DD", i.e. 2010-12-31.
    rf: float
        The risk-free rate
    opt_type: Union[1, -1]
        The option type 1 is for call and -1 is for put
    mini: float
        The minimum strike price to include in the table
    maxi: float
        The maximum strike price to include in the table
    show_all: bool
        Whether to show all greeks
    """
    ...

