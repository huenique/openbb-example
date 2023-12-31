"""
This type stub file was generated by pyright.
"""

from typing import Optional, Union
from openbb_terminal import OpenBBFigure
from openbb_terminal.decorators import check_api_key, log_start_end

"""SentimentInvestor View"""
__docformat__ = ...
logger = ...
@log_start_end(log=logger)
@check_api_key(["API_SMARTSTAKE_KEY", "API_SMARTSTAKE_TOKEN"])
def display_luna_circ_supply_change(days: int = ..., export: str = ..., sheet_name: Optional[str] = ..., supply_type: str = ..., limit: int = ..., external_axes: bool = ...) -> Union[OpenBBFigure, None]:
    """Plots and prints table showing Luna circulating supply stats

    Parameters
    ----------
    days: int
        Number of days
    supply_type: str
        Supply type to unpack json
    sheet_name: str
        Optionally specify the name of the sheet the data is exported to.
    export: str
        Export type
    limit: int
        Number of results display on the terminal
        Default: 5
    external_axes : bool, optional
        Whether to return the figure object or not, by default False
    """
    ...

