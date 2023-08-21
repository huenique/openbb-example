"""
This type stub file was generated by pyright.
"""

import pandas as pd
from typing import Tuple
from openbb_terminal.stocks.options.op_helpers import Options

"""Model for retrieving public options data from the CBOE."""
__docformat__ = ...
TICKER_EXCEPTIONS: list[str] = ...
def get_cboe_directory() -> pd.DataFrame:
    """Gets the US Listings Directory for the CBOE.

    Returns
    -------
    pd.DataFrame: CBOE_DIRECTORY
        DataFrame of the CBOE listings directory

    Examples
    -------
    >>> from openbb_terminal.stocks.options import cboe_model
    >>> CBOE_DIRECTORY = cboe_model.get_cboe_directory()
    """
    ...

def get_cboe_index_directory() -> pd.DataFrame:
    """Gets the US Listings Directory for the CBOE

    Returns
    -------
    pd.DataFrame: CBOE_INDEXES

    Examples
    -------
    >>> from openb_terminal.stocks.options import cboe_model
    >>> CBOE_INDEXES = cboe_model.get_cboe_index_directory()
    """
    ...

INDEXES = ...
SYMBOLS = ...
def get_ticker_info(symbol: str) -> Tuple[pd.DataFrame, list[str]]:
    """Gets basic info for the symbol and expiration dates

    Parameters
    ----------
    symbol: str
        The ticker to lookup

    Returns
    -------
    Tuple: [pd.DataFrame, pd.Series]
        ticker_details
        ticker_expirations

    Examples
    --------
    >>> from openbb_terminal.stocks.options import cboe_model
    >>> ticker_details,ticker_expirations = cboe_model.get_ticker_info('AAPL')
    >>> vix_details,vix_expirations = cboe_model.get_ticker_info('VIX')
    """
    ...

def get_ticker_iv(symbol: str) -> pd.DataFrame:
    """Gets annualized high/low historical and implied volatility over 30/60/90 day windows.

    Parameters
    ----------
    symbol: str
        The loaded ticker

    Returns
    -------
    pd.DataFrame: ticker_iv

    Examples
    --------
    >>> from openbb_terminal.stocks.options import cboe_model
    >>> ticker_iv = cboe_model.get_ticker_iv('AAPL')
    >>> ndx_iv = cboe_model.get_ticker_iv('NDX')
    """
    ...

def get_quotes(symbol: str) -> pd.DataFrame:
    """Gets the complete options chains for a ticker.

    Parameters
    ----------
    symbol: str
        The ticker get options data for

    Returns
    -------
    pd.DataFrame
        DataFrame with all active options contracts for the underlying symbol.

    Examples
    --------
    >>> from openbb_terminal.stocks.options import cboe_model
    >>> xsp = cboe_model.OptionsChains().get_chains('XSP')
    >>> xsp_chains = xsp.chains
    """
    ...

def load_options(symbol: str, pydantic: bool = ...) -> Options:
    """OptionsChains data object for CBOE.

    Parameters
    ----------
    symbol: str
        The ticker symbol to load.
    pydantic: bool
        Whether to return the object as a Pydantic Model or a subscriptable Pandas Object.  Default is False.

    Returns
    -------
    object: OptionsChains
        chains: dict
            The complete options chain for the ticker. Returns as a Pandas DataFrame if pydantic is False.
        expirations: list[str]
            List of unique expiration dates. (YYYY-MM-DD)
        strikes: list[float]
            List of unique strike prices.
        last_price: float
            The last price of the underlying asset.
        underlying_name: str
            The name of the underlying asset.
        underlying_price: dict
            The price and recent performance of the underlying asset. Returns as a Pandas Series if pydantic is False.
        hasIV: bool
            Returns implied volatility.
        hasGreeks: bool
            Returns greeks data.
        symbol: str
            The symbol entered by the user.
        source: str
            The source of the data, "CBOE".
        SYMBOLS: dict
            The CBOE symbol directory. Returns as a Pandas DataFrame if pydantic is False.

    Examples
    --------
    Get current options chains for AAPL.
    >>> from openbb_terminal.stocks.options.cboe_model import load_options
    >>> data = load_options("AAPL")
    >>> chains = data.chains

    Return the object as a Pydantic Model.
    >>> from openbb_terminal.stocks.options.cboe_model import load_options
    >>> data = load_options("AAPL", pydantic=True)
    """
    ...
