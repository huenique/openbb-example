"""
This type stub file was generated by pyright.
"""

import pandas as pd

"""Insider SDK Helpers"""
__docformat__ = ...
def stats(symbol: str) -> pd.DataFrame:
    """Get OpenInsider stats for ticker

    Parameters
    ----------
    symbol : str
        Ticker to get insider stats for

    Returns
    -------
    pd.DataFrame
        DataFrame of insider stats

    Examples
    --------
    >>> from openbb_terminal.sdk import openbb
    >>> openbb.stocks.ins.stats("AAPL")
    """
    ...

def insider_filter(preset: str) -> pd.DataFrame:
    """GEt insider trades based on preset filter

    Parameters
    ----------
    preset : str
       Name of preset filter

    Returns
    -------
    pd.DataFrame
        DataFrame of filtered insider data

    Examples
    --------
    >>> from openbb_terminal.sdk import openbb

    In order to filter, we pass one of the predefined .ini filters from OpenBBUserData/presets/stocks/insider
    >>> filter = "Gold-Silver"
    >>> insider_trades = openbb.stocks.ins.filter(filter)
    """
    ...

def lcb() -> pd.DataFrame:
    """Get latest cluster buys

    Returns
    -------
    pd.DataFrame
        DataFrame of latest insider trades

    Examples
    --------
    >>> from openbb_terminal.sdk import openbb
    >>> openbb.stocks.ins.lcb()
    """
    ...

def lpsb() -> pd.DataFrame:
    """Get latest penny stock buys

    Returns
    -------
    pd.DataFrame
        DataFrame of latest insider trades

    Examples
    --------
    >>> from openbb_terminal.sdk import openbb
    >>> openbb.stocks.ins.lpsb()
    """
    ...

def lit() -> pd.DataFrame:
    """Get latest insider trades

    Returns
    -------
    pd.DataFrame
        DataFrame of latest insider trades

    Examples
    --------
    >>> from openbb_terminal.sdk import openbb
    >>> openbb.stocks.ins.lit()
    """
    ...

def lip() -> pd.DataFrame:
    """Get latest insider purchases

    Returns
    -------
    pd.DataFrame
        DataFrame of latest insider trades

    Examples
    --------
    >>> from openbb_terminal.sdk import openbb
    >>> openbb.stocks.ins.lip()
    """
    ...

def blip() -> pd.DataFrame:
    """Get latest insider purchases > 25k

    Returns
    -------
    pd.DataFrame
        DataFrame of latest insider trades

    Examples
    --------
    >>> from openbb_terminal.sdk import openbb
    >>> openbb.stocks.ins.blip()
    """
    ...

def blop() -> pd.DataFrame:
    """Get latest officer purchases > 25k

    Returns
    -------
    pd.DataFrame
        DataFrame of latest insider trades

    Examples
    --------
    >>> from openbb_terminal.sdk import openbb
    >>> openbb.stocks.ins.blop()
    """
    ...

def blcp() -> pd.DataFrame:
    """Get latest CEO/CFO purchases > 25k

    Returns
    -------
    pd.DataFrame
        DataFrame of latest insider trades

    Examples
    --------
    >>> from openbb_terminal.sdk import openbb
    >>> openbb.stocks.ins.blcp()
    """
    ...

def lis() -> pd.DataFrame:
    """Get latest insider sales

    Returns
    -------
    pd.DataFrame
        DataFrame of latest insider trades

    Examples
    --------
    >>> from openbb_terminal.sdk import openbb
    >>> openbb.stocks.ins.lis()
    """
    ...

def blis() -> pd.DataFrame:
    """Get latest insider sales > 100k

    Returns
    -------
    pd.DataFrame
        DataFrame of latest insider trades

    Examples
    --------
    >>> from openbb_terminal.sdk import openbb
    >>> openbb.stocks.ins.blis()
    """
    ...

def blos() -> pd.DataFrame:
    """Get latest officer sales > 100k

    Returns
    -------
    pd.DataFrame
        DataFrame of latest insider trades

    Examples
    --------
    >>> from openbb_terminal.sdk import openbb
    >>> openbb.stocks.ins.blos()
    """
    ...

def blcs() -> pd.DataFrame:
    """Get latest CEO/CFO sales > 100k

    Returns
    -------
    pd.DataFrame
        DataFrame of latest insider trades

    Examples
    --------
    >>> from openbb_terminal.sdk import openbb
    >>> openbb.stocks.ins.blcs()
    """
    ...

