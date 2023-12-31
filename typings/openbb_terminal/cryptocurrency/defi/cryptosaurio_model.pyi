"""
This type stub file was generated by pyright.
"""

import pandas as pd
from typing import Tuple
from openbb_terminal.decorators import log_start_end

"""Cryptosaurio model"""
__docformat__ = ...
logger = ...
api_url = ...
@log_start_end(log=logger)
def get_anchor_data(address: str = ...) -> Tuple[pd.DataFrame, pd.DataFrame, str]:
    """Returns anchor protocol earnings data of a certain terra address
    [Source: https://cryptosaurio.com/]

    Parameters
    ----------
    address : str
        Terra address. Valid terra addresses start with 'terra'

    Returns
    -------
    Tuple[pd.DataFrame, pd.DataFrame, str]
        - pd.DataFrame: Earnings over time in UST
        - pd.DataFrame: History of transactions
        - str:              Overall statistics
    """
    ...

