"""
This type stub file was generated by pyright.
"""

import pandas as pd
from typing import Tuple

"""CBOE Model Functions"""
__docformat__ = ...
def get_top_of_book(symbol: str, exchange: str = ...) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Get top of book bid and ask for ticker on exchange [CBOE.com]

    Parameters
    ----------
    symbol: str
        Ticker to get
    exchange: str
        Exchange to look at.  Can be `BZX`,`EDGX`, `BYX`, `EDGA`

    Returns
    -------
    pd.DatatFrame
        Dataframe of Bids
    pd.DataFrame
        Dataframe of asks

    """
    ...
