"""
This type stub file was generated by pyright.
"""

import pandas as pd
from openbb_terminal.decorators import log_start_end

"""Terra Engineer model"""
__docformat__ = ...
logger = ...
api_url = ...
ASSETS = ...
@log_start_end(log=logger)
def get_history_asset_from_terra_address(asset: str = ..., address: str = ...) -> pd.DataFrame:
    """Returns historical data of an asset in a certain terra address
    [Source: https://terra.engineer/]

    Parameters
    ----------
    asset : str
        Terra asset {ust,luna,sdt}
    address : str
        Terra address. Valid terra addresses start with 'terra'

    Returns
    -------
    pd.DataFrame
        historical data
    """
    ...

@log_start_end(log=logger)
def get_anchor_yield_reserve() -> pd.DataFrame:
    """Displays the 30-day history of the Anchor Yield Reserve.
    [Source: https://terra.engineer/]

    Returns
    -------
    pd.DataFrame
        Dataframe containing historical data
    """
    ...

