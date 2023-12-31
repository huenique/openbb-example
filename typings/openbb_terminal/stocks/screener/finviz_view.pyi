"""
This type stub file was generated by pyright.
"""

from typing import List, Optional
from openbb_terminal.decorators import log_start_end

""" Finviz View """
__docformat__ = ...
logger = ...
d_cols_to_sort = ...
@log_start_end(log=logger)
def screener(loaded_preset: str = ..., data_type: str = ..., limit: int = ..., ascend: bool = ..., sortby: str = ..., export: str = ..., sheet_name: Optional[str] = ...) -> List[str]:
    """Screener one of the following: overview, valuation, financial, ownership, performance, technical.

    Parameters
    ----------
    loaded_preset: str
        Preset loaded to filter for tickers
    data_type : str
        Data type string between: overview, valuation, financial, ownership, performance, technical
    limit : int
        Limit of stocks to display
    ascend : bool
        Order of table to ascend or descend
    sortby: str
        Column to sort table by
    export : str
        Export dataframe data to csv,json,xlsx file

    Returns
    -------
    List[str]
        List of stocks that meet preset criteria
    """
    ...

