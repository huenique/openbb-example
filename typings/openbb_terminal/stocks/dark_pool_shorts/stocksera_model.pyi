"""
This type stub file was generated by pyright.
"""

import pandas as pd
from openbb_terminal.decorators import log_start_end

"""Stocksera model"""
__docformat__ = ...
logger = ...
@log_start_end(log=logger)
def get_cost_to_borrow(symbol: str) -> pd.DataFrame:
    """Get cost to borrow of stocks [Source: Stocksera]

    Parameters
    ----------
    symbol : str
        ticker to get cost to borrow from

    Returns
    -------
    pd.DataFrame
        Cost to borrow
    """
    ...
