"""
This type stub file was generated by pyright.
"""

import pandas as pd
from openbb_terminal.decorators import log_start_end

"""CryptoStats model"""
__docformat__ = ...
logger = ...
@log_start_end(log=logger)
def get_fees(marketcap: bool, tvl: bool, date) -> pd.DataFrame:
    """Show cryptos with most fees. [Source: CryptoStats]

    Parameters
    ----------
    marketcap: bool
        Whether to show marketcap or not
    tvl: bool
        Whether to show tvl or not
    date: datetime
        Date to get data from (YYYY-MM-DD)

    Returns
    -------
    pd.DataFrame
        Top coins with most fees
    """
    ...

