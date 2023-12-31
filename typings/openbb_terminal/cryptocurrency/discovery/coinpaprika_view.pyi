"""
This type stub file was generated by pyright.
"""

from typing import Optional
from openbb_terminal.decorators import log_start_end

"""CoinPaprika view"""
__docformat__ = ...
logger = ...
@log_start_end(log=logger)
def display_search_results(query: str, category: str = ..., limit: int = ..., sortby: str = ..., ascend: bool = ..., export: str = ..., sheet_name: Optional[str] = ...) -> None:
    """Prints table showing Search over CoinPaprika. [Source: CoinPaprika]

    Parameters
    ----------
    query: str
        Search query
    category: str
        Categories to search: currencies|exchanges|icos|people|tags|all. Default: all
    limit: int
        Number of records to display
    sortby: str
        Key to sort data. The table can be sorted by every of its columns. Refer to
        API documentation (see https://api.coinpaprika.com/docs#tag/Tools/paths/~1search/get)
    ascend: bool
        Flag to sort data descending
    export : str
        Export dataframe data to csv,json,xlsx file
    """
    ...

