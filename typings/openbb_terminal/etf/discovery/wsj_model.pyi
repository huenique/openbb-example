"""
This type stub file was generated by pyright.
"""

import pandas as pd
from openbb_terminal.decorators import log_start_end

"""WSJ model"""
__docformat__ = ...
logger = ...
@log_start_end(log=logger)
def etf_movers(sort_type: str = ..., export: bool = ...) -> pd.DataFrame:
    """
    Scrape data for top etf movers.
    Parameters
    ----------
    sort_type: str
        Data to get. Can be "gainers", "decliners" or "active"

    Returns
    -------
    etfmovers: pd.DataFrame
        Datafame containing the name, price, change and the volume of the etf
    """
    ...

