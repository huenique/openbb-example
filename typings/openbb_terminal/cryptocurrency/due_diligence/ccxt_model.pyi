"""
This type stub file was generated by pyright.
"""

import pandas as pd
from typing import Any, Dict, List

"""Ccxt model"""
__docformat__ = ...
def get_exchanges() -> List[str]:
    """Helper method to get all the exchanges supported by ccxt
    [Source: https://docs.ccxt.com/en/latest/manual.html]

    Parameters
    ----------

    Returns
    -------
    List[str]
        list of all the exchanges supported by ccxt
    """
    ...

def get_binance_currencies() -> List[str]:
    """Helper method to get all the currenices supported by ccxt
    [Source: https://docs.ccxt.com/en/latest/manual.html]

    Parameters
    ----------

    Returns
    -------
    List[str]
        list of all the currenices supported by ccxt
    """
    ...

def get_orderbook(exchange: str, symbol: str, to_symbol: str) -> Dict[str, Any]:
    """Returns orderbook for a coin in a given exchange
    [Source: https://docs.ccxt.com/en/latest/manual.html]

    Parameters
    ----------
    exchange : str
        exchange id
    symbol : str
        coin symbol
    to_symbol : str
        currency to compare coin against

    Returns
    -------
    Dict[str, Any]
        With bids and asks
    """
    ...

def get_trades(exchange_id: str, symbol: str, to_symbol: str) -> pd.DataFrame:
    """Returns trades for a coin in a given exchange
    [Source: https://docs.ccxt.com/en/latest/manual.html]

    Parameters
    ----------
    exchange_id : str
        exchange id
    symbol : str
        coin symbol
    to_symbol : str
        currency to compare coin against

    Returns
    -------
    pd.DataFrame
        trades for a coin in a given exchange
    """
    ...

