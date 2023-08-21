"""
This type stub file was generated by pyright.
"""

from typing import Optional
from openbb_terminal.decorators import check_api_key, log_start_end

"""Coinbase view"""
__docformat__ = ...
logger = ...
@log_start_end(log=logger)
@check_api_key(["API_COINBASE_KEY", "API_COINBASE_SECRET", "API_COINBASE_PASS_PHRASE"])
def display_account(currency: str = ..., export: str = ..., sheet_name: Optional[str] = ...) -> None:
    """Display list of all your trading accounts. [Source: Coinbase]

    Parameters
    ----------
    currency: str
        Currency to show current value in, default 'USD'
    export : str
        Export dataframe data to csv,json,xlsx file
    """
    ...

@log_start_end(log=logger)
@check_api_key(["API_COINBASE_KEY", "API_COINBASE_SECRET", "API_COINBASE_PASS_PHRASE"])
def display_history(account: str, export: str = ..., sheet_name: Optional[str] = ..., limit: int = ...) -> None:
    """Display account history. [Source: Coinbase]

    Parameters
    ----------
    account: str
        Symbol or account id
    limit: int
        For all accounts display only top n
    export : str
        Export dataframe data to csv,json,xlsx file
    """
    ...

@log_start_end(log=logger)
@check_api_key(["API_COINBASE_KEY", "API_COINBASE_SECRET", "API_COINBASE_PASS_PHRASE"])
def display_orders(limit: int = ..., sortby: str = ..., descend: bool = ..., export: str = ..., sheet_name: Optional[str] = ...) -> None:
    """List your current open orders [Source: Coinbase]

    Parameters
    ----------
    limit: int
        Last `limit` of trades. Maximum is 1000.
    sortby: str
        Key to sort by
    descend: bool
        Flag to sort descending
    export : str
        Export dataframe data to csv,json,xlsx file
    """
    ...

@log_start_end(log=logger)
@check_api_key(["API_COINBASE_KEY", "API_COINBASE_SECRET", "API_COINBASE_PASS_PHRASE"])
def display_deposits(limit: int = ..., sortby: str = ..., deposit_type: str = ..., descend: bool = ..., export: str = ..., sheet_name: Optional[str] = ...) -> None:
    """Display deposits into account [Source: Coinbase]

    Parameters
    ----------
    limit: int
        Last `limit` of trades. Maximum is 1000.
    sortby: str
        Key to sort by
    descend: bool
        Flag to sort descending
    deposit_type: str
        internal_deposits (transfer between portfolios) or deposit
    export : str
        Export dataframe data to csv,json,xlsx file
    """
    ...
