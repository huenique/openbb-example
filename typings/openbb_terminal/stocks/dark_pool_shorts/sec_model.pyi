"""
This type stub file was generated by pyright.
"""

import pandas as pd
from typing import Optional
from openbb_terminal.decorators import log_start_end

""" SEC Model """
__docformat__ = ...
logger = ...
@log_start_end(log=logger)
def catching_diff_url_formats(ftd_urls: list) -> list:
    """Catches if URL for SEC data is one of the few URLS that are not in the
    standard format. Catches are for either specific date ranges that have a different
    format or singular URLs that have a different format.

    Parameters
    ----------
    ftd_urls : list
        list of urls of sec data

    Returns
    -------
    list
        list of ftd urls
    """
    ...

@log_start_end(log=logger)
def get_fails_to_deliver(symbol: str, start_date: Optional[str] = ..., end_date: Optional[str] = ..., limit: int = ...) -> pd.DataFrame:
    """Display fails-to-deliver data for a given ticker. [Source: SEC]

    Parameters
    ----------
    symbol : str
        Stock ticker
    start_date : Optional[str]
        Start of data, in YYYY-MM-DD format
    end_date : Optional[str]
        End of data, in YYYY-MM-DD format
    limit : int
        Number of latest fails-to-deliver being printed

    Returns
    -------
    pd.DataFrame
        Fail to deliver data
    """
    ...
