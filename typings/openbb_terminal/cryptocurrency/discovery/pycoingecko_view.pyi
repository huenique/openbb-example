"""
This type stub file was generated by pyright.
"""

from typing import Optional
from openbb_terminal.decorators import log_start_end

"""CoinGecko view"""
__docformat__ = ...
logger = ...
COINS_COLUMNS = ...
@log_start_end(log=logger)
def display_coins(category: str, limit: int = ..., sortby: str = ..., export: str = ..., sheet_name: Optional[str] = ..., ascend: bool = ...) -> None:
    """Prints table showing top coins [Source: CoinGecko]

    Parameters
    ----------
    category: str
        If no category is passed it will search for all coins. (E.g., smart-contract-platform)
    limit: int
        Number of records to display
    sortby: str
        Key to sort data
    export : str
        Export dataframe data to csv,json,xlsx file
    ascend: bool
        Sort data in ascending order
    """
    ...

@log_start_end(log=logger)
def display_gainers(interval: str = ..., limit: int = ..., sortby: str = ..., ascend: bool = ..., export: str = ..., sheet_name: Optional[str] = ...) -> None:
    """Prints table showing Largest Gainers - coins which gain the most in given period. [Source: CoinGecko]

    Parameters
    ----------
    interval: str
        Time period by which data is displayed. One from [1h, 24h, 7d, 14d, 30d, 60d, 1y]
    limit: int
        Number of records to display
    sortby: str
        Key to sort data. The table can be sorted by every of its columns. Refer to
        API documentation (see /coins/markets in https://www.coingecko.com/en/api/documentation)
    ascend: bool
        Sort data in ascending order
    export : str
        Export dataframe data to csv,json,xlsx file
    """
    ...

@log_start_end(log=logger)
def display_losers(interval: str = ..., limit: int = ..., export: str = ..., sheet_name: Optional[str] = ..., sortby: str = ..., ascend: bool = ...) -> None:
    """Prints table showing Largest Losers - coins which lost the most in given period of time. [Source: CoinGecko]

    Parameters
    ----------
    interval: str
        Time period by which data is displayed. One from [1h, 24h, 7d, 14d, 30d, 60d, 1y]
    limit: int
        Number of records to display
    sortby: str
        Key to sort data. The table can be sorted by every of its columns. Refer to
        API documentation (see /coins/markets in https://www.coingecko.com/en/api/documentation)
    ascend: bool
        Sort data in ascending order
    export : str
        Export dataframe data to csv,json,xlsx file
    """
    ...

@log_start_end(log=logger)
def display_trending(export: str = ..., sheet_name: Optional[str] = ...) -> None:
    """Prints table showing trending coins [Source: CoinGecko]

    Parameters
    ----------
    export : str
        Export dataframe data to csv,json,xlsx file
    """
    ...
