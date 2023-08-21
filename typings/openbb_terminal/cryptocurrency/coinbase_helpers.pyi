"""
This type stub file was generated by pyright.
"""

from typing import Any, Optional
from requests.auth import AuthBase

"""Coinbase helpers model"""
__docformat__ = ...
logger = ...
class CoinbaseProAuth(AuthBase):
    """Authorize CoinbasePro requests. Source: https://docs.pro.coinbase.com/?python#signing-a-message"""
    def __init__(self, api_key, secret_key, passphrase) -> None:
        ...
    
    def __call__(self, request_coinbase):
        ...
    


class CoinbaseRequestException(Exception):
    """Coinbase Request Exception object"""
    def __init__(self, message: str) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class CoinbaseApiException(Exception):
    """Coinbase API Exception object"""
    def __init__(self, message: str) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


def check_validity_of_product(product_id: str) -> str:
    """Helper method that checks if provided product_id exists. It's a pair of coins in format COIN-COIN.
    If product exists it return it, in other case it raise an error. [Source: Coinbase]

    Parameters
    ----------
    product_id: str
        Trading pair of coins on Coinbase e.g ETH-USDT or UNI-ETH

    Returns
    -------
    str
        pair of coins in format COIN-COIN
    """
    ...

def make_coinbase_request(endpoint, params: Optional[dict] = ..., auth: Optional[Any] = ...) -> dict:
    """Request handler for Coinbase Pro Api. Prepare a request url, params and payload and call endpoint.
    [Source: Coinbase]

    Parameters
    ----------
    endpoint: str
        Endpoint path e.g /products
    params: dict
        Parameter dedicated for given endpoint
    auth: any
        Api credentials for purpose of using endpoints that needs authentication

    Returns
    -------
    dict
        response from Coinbase Pro Api
    """
    ...

