"""
This type stub file was generated by pyright.
"""

import pandas as pd
from openbb_terminal.decorators import log_start_end

"""HackerNews Model"""
__docformat__ = ...
logger = ...
@log_start_end(log=logger)
def get_stories(limit: int = ...) -> pd.DataFrame:
    """Get top stories from HackerNews.
    Parameters
    ----------
    limit: int
        Number of stories to return
    Returns
    -------
    pd.DataFrame
        DataFrame with stories
    """
    ...

