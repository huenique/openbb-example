"""
This type stub file was generated by pyright.
"""

import pandas as pd
from openbb_terminal.decorators import log_start_end

"""ETH Gas Station model"""
logger = ...
@log_start_end(log=logger)
def get_gwei_fees() -> pd.DataFrame:
    """Returns the most recent Ethereum gas fees in gwei
    [Source: https://ethgasstation.info]

    Parameters
    ----------

    Returns
    -------
    pd.DataFrame
        four gas fees and durations
            (fees for slow, average, fast and
            fastest transactions in gwei and
            its average durations in seconds)
    """
    ...

