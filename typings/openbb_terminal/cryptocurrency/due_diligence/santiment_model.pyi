"""
This type stub file was generated by pyright.
"""

import pandas as pd
from typing import Optional
from openbb_terminal.decorators import check_api_key, log_start_end

logger = ...
def get_slug(symbol: str) -> str:
    """
    Get Santiment slug mapping and return corresponding slug for a given coin
    """
    ...

@log_start_end(log=logger)
@check_api_key(["API_SANTIMENT_KEY"])
def get_github_activity(symbol: str, dev_activity: bool = ..., interval: str = ..., start_date: Optional[str] = ..., end_date: Optional[str] = ...) -> pd.DataFrame:
    """Returns  a list of developer activity for a given coin and time interval.

    [Source: https://santiment.net/]

    Parameters
    ----------
    symbol : str
        Crypto symbol to check github activity
    dev_activity: bool
        Whether to filter only for development activity
    interval : str
        Interval frequency (e.g., 1d)
    start_date : Optional[str]
        Initial date like string (e.g., 2021-10-01)
    end_date : Optional[str]
        End date like string (e.g., 2021-10-01)

    Returns
    -------
    pd.DataFrame
        developer activity over time
    """
    ...

