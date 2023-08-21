"""
This type stub file was generated by pyright.
"""

import pandas as pd
from openbb_terminal.decorators import log_start_end

"""Coinbase model"""
__docformat__ = ...
logger = ...
@log_start_end(log=logger)
def get_accounts(add_current_price: bool = ..., currency: str = ...) -> pd.DataFrame:
    """Get list of all your trading accounts. [Source: Coinbase]

    Single account information:

    .. code-block:: json

        {
            "id": "71452118-efc7-4cc4-8780-a5e22d4baa53",
            "currency": "BTC",
            "balance": "0.0000000000000000",
            "available": "0.0000000000000000",
            "hold": "0.0000000000000000",
            "profile_id": "75da88c5-05bf-4f54-bc85-5c775bd68254"
        }

    .

    Parameters
    ----------
    add_current_price: bool
        Boolean to query coinbase for current price
    currency: str
        Currency to convert to, defaults to 'USD'

    Returns
    -------
    pd.DataFrame
        DataFrame with all your trading accounts.
    """
    ...

@log_start_end(log=logger)
def get_account_history(account: str) -> pd.DataFrame:
    """Get your account history. Account activity either increases or decreases your account balance. [Source: Coinbase]

    Example api response:

    .. code-block:: json

        {
            "id": "100",
            "created_at": "2014-11-07T08:19:27.028459Z",
            "amount": "0.001",
            "balance": "239.669",
            "type": "fee",
            "details": {
                "order_id": "d50ec984-77a8-460a-b958-66f114b0de9b",
                "trade_id": "74",
                "product_id": "BTC-USD"
            }
        }

    .

    Parameters
    ----------
    account: str
        id ("71452118-efc7-4cc4-8780-a5e22d4baa53") or currency (BTC)
    Returns
    -------
    pd.DataFrame
        DataFrame with account history.
    """
    ...

@log_start_end(log=logger)
def get_orders(limit: int = ..., sortby: str = ..., descend: bool = ...) -> pd.DataFrame:
    """List your current open orders. Only open or un-settled orders are returned. [Source: Coinbase]

    Example response from API:

    .. code-block:: json

        {
            "id": "d0c5340b-6d6c-49d9-b567-48c4bfca13d2",
            "price": "0.10000000",
            "size": "0.01000000",
            "product_id": "BTC-USD",
            "side": "buy",
            "stp": "dc",
            "type": "limit",
            "time_in_force": "GTC",
            "post_only": false,
            "created_at": "2016-12-08T20:02:28.53864Z",
            "fill_fees": "0.0000000000000000",
            "filled_size": "0.00000000",
            "executed_value": "0.0000000000000000",
            "status": "open",
            "settled": false
        }

    .
    Parameters
    ----------
    limit: int
        Last `limit` of trades. Maximum is 1000.
    sortby: str
        Key to sort by
    descend: bool
        Flag to sort descending

    Returns
    -------
    pd.DataFrame
        Open orders in your account
    """
    ...

@log_start_end(log=logger)
def get_deposits(limit: int = ..., sortby: str = ..., deposit_type: str = ..., descend: bool = ...) -> pd.DataFrame:
    """Get a list of deposits for your account. [Source: Coinbase]

    Parameters
    ----------
    deposit_type: str
        internal_deposits (transfer between portfolios) or deposit

    Returns
    -------
    pd.DataFrame
        List of deposits
    """
    ...

