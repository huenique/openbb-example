"""
This type stub file was generated by pyright.
"""

import pandas as pd

"""Crypto OV SDK Helper Functions."""
__docformat__ = ...
def globe(source: str = ...) -> pd.DataFrame:
    """Get global crypto market data.

    Parameters
    ----------
    source : str, optional
        Source of data, by default "CoinGecko"

    Returns
    -------
    pd.DataFrame
        DataFrame with global crypto market data

    Examples
    --------
    >>> from openbb_terminal.sdk import openbb
    >>> global_market_data = openbb.crypto.ov.globe()

    To get data from CoinPaprika, use the source parameter:
    >>> global_market_data = openbb.crypto.ov.globe(source="coinpaprika")

    """
    ...

def exchanges(source: str = ...) -> pd.DataFrame:
    """Show top crypto exchanges.

    Parameters
    ----------
    source : str, optional
        Source to get exchanges, by default "CoinGecko"

    Returns
    -------
    pd.DataFrame
        DataFrame with top crypto exchanges

    Examples
    --------
    >>> from openbb_terminal.sdk import openbb
    >>> exchanges = openbb.crypto.ov.exchanges()
    """
    ...
