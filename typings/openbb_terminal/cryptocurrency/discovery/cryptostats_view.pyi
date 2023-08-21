"""
This type stub file was generated by pyright.
"""

from typing import Optional
from openbb_terminal.decorators import log_start_end

"""CryptoStats view"""
__docformat__ = ...
logger = ...
@log_start_end(log=logger)
def display_fees(marketcap: bool, tvl: bool, date: str, limit: int = ..., sortby: str = ..., ascend: bool = ..., sheet_name: Optional[str] = ..., export: str = ...) -> None:
    """Display crypto with most fees paid [Source: CryptoStats]

    Parameters
    ----------
    marketcap: bool
        Flag to include marketcap
    date: str
        Date to get data from (YYYY-MM-DD)
    limit: int
        Number of records to display
    sortby: str
        Key to sort data.
    ascend: bool
        Flag to sort data ascending
    export : str
        Export dataframe data to csv,json,xlsx file
    """
    ...

