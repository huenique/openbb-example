"""
This type stub file was generated by pyright.
"""

from typing import List
from openbb_terminal.decorators import check_api_key, log_start_end

"""Polygon Model"""
__docformat__ = ...
logger = ...
@log_start_end(log=logger)
@check_api_key(["API_POLYGON_KEY"])
def get_similar_companies(symbol: str, us_only: bool = ...) -> List[str]:
    """Get similar companies from Polygon

    Parameters
    ----------
    symbol: str
        Ticker to get similar companies of
    us_only: bool
        Only stocks from the US stock exchanges

    Returns
    -------
    List[str]:
        List of similar tickers
    """
    ...
