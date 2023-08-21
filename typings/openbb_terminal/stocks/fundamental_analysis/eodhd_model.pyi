"""
This type stub file was generated by pyright.
"""

import pandas as pd
from openbb_terminal.decorators import check_api_key, log_start_end

"""eodhd Model"""
__docformat__ = ...
logger = ...
@log_start_end(log=logger)
@check_api_key(["API_EODHD_KEY"])
def get_financials(symbol: str, statement: str, quarterly: bool = ..., ratios: bool = ...) -> pd.DataFrame:
    """Get ticker financial statements from eodhd

    Parameters
    ----------
    symbol: str
        Stock ticker symbol
    statement: str
        Financial statement data to retrieve, can be balance, income or cash
    quarterly:bool
        Flag to get quarterly reports, by default False
    ratios: bool
        Shows percentage change, by default False

    Returns
    -------
    pd.DataFrame
        Balance Sheets or Income Statements or cashflow
    """
    ...

