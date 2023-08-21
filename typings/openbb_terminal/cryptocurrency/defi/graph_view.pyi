"""
This type stub file was generated by pyright.
"""

from typing import Optional
from openbb_terminal.decorators import log_start_end

"""The Graph view"""
__docformat__ = ...
logger = ...
@log_start_end(log=logger)
def display_uni_tokens(skip: int = ..., limit: int = ..., sortby: str = ..., ascend: bool = ..., export: str = ..., sheet_name: Optional[str] = ...) -> None:
    """Prints table showing tokens trade-able on Uniswap DEX.
    [Source: https://thegraph.com/en/]

    Parameters
    ----------
    skip: int
        Number of records to skip
    limit: int
        Number of records to display
    sortby: str
        Key by which to sort data
    ascend: bool
        Flag to sort data descending
    export : str
        Export dataframe data to csv,json,xlsx file
    """
    ...

@log_start_end(log=logger)
def display_uni_stats(export: str = ..., sheet_name: Optional[str] = ...) -> None:
    """Prints table showing base statistics about Uniswap DEX. [Source: https://thegraph.com/en/]
    [Source: https://thegraph.com/en/]

    Parameters
    ----------

    export : str
        Export dataframe data to csv,json,xlsx file
    """
    ...

@log_start_end(log=logger)
def display_recently_added(limit: int = ..., days: int = ..., min_volume: int = ..., min_liquidity: int = ..., min_tx: int = ..., sortby: str = ..., ascend: bool = ..., export: str = ..., sheet_name: Optional[str] = ...) -> None:
    """Prints table showing Lastly added pairs on Uniswap DEX.
    [Source: https://thegraph.com/en/]

    Parameters
    ----------
    limit: int
        Number of records to display
    days: int
        Number of days the pair has been active,
    min_volume: int
        Minimum trading volume,
    min_liquidity: int
        Minimum liquidity
    min_tx: int
        Minimum number of transactions
    sortby: str
        Key by which to sort data
    ascend: bool
        Flag to sort data descending
    export : str
        Export dataframe data to csv,json,xlsx file
    """
    ...

@log_start_end(log=logger)
def display_uni_pools(limit: int = ..., sortby: str = ..., ascend: bool = ..., export: str = ..., sheet_name: Optional[str] = ...) -> None:
    """Prints table showing uniswap pools by volume.
    [Source: https://thegraph.com/en/]

    Parameters
    ----------
    limit: int
        Number of records to display
    sortby: str
        Key by which to sort data. The table can be sorted by every of its columns
        (see https://bit.ly/3ORagr1 then press ctrl-enter or execute the query).
    ascend: bool
        Flag to sort data descending
    export : str
        Export dataframe data to csv,json,xlsx file
    """
    ...

@log_start_end(log=logger)
def display_last_uni_swaps(limit: int = ..., sortby: str = ..., ascend: bool = ..., export: str = ..., sheet_name: Optional[str] = ...) -> None:
    """Prints table showing last swaps done on Uniswap
    [Source: https://thegraph.com/en/]

    Parameters
    ----------
    limit: int
        Number of records to display
    sortby: str
        Key by which to sort data. The table can be sorted by every of its columns
        (see https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2).
    ascend: bool
        Flag to sort data descending
    export : str
        Export dataframe data to csv,json,xlsx file
    """
    ...

