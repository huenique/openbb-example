"""
This type stub file was generated by pyright.
"""

import pandas as pd
from typing import Optional
from openbb_terminal.decorators import log_start_end

"""Blockchain Center Model"""
logger = ...
DAYS = ...
@log_start_end(log=logger)
def get_altcoin_index(period: int = ..., start_date: str = ..., end_date: Optional[str] = ...) -> pd.DataFrame:
    """Get altcoin index overtime
    [Source: https://blockchaincenter.net]

    Parameters
    ----------
    period: int
        Number of days {30,90,365} to check performance of coins and calculate the altcoin index.
        E.g., 365 checks yearly performance, 90 will check seasonal performance (90 days),
        30 will check monthly performance (30 days).
    start_date : str
        Initial date, format YYYY-MM-DD
    end_date : Optional[str]
        Final date, format YYYY-MM-DD

    Returns
    -------
    pd.DataFrame
        Date, Value (Altcoin Index)
    """
    ...

