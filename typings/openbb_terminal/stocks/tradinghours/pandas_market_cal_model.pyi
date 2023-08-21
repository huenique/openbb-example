"""
This type stub file was generated by pyright.
"""

import pandas as pd
from openbb_terminal.decorators import log_start_end

logger = ...
@log_start_end(log=logger)
def get_all_holiday_exchange_short_names() -> pd.DataFrame:
    """Get all holiday exchanges short names.

    Returns
    -------
    pd.DataFrame
        All available exchanges with holiday data (short names)
    """
    ...

@log_start_end(log=logger)
def get_exchange_holidays(exchange_symbol: str, year: int) -> pd.DataFrame:
    """Get all short name of each exchange that we hold holiday calendar for.

    Parameters
    ----------
    symbol : str
        Exchange symbol
    year : int
        Calendar year

    Returns
    -------
    pd.DataFrame
        All available exchanges with holiday data (short names)
    """
    ...

