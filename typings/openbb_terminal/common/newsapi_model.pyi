"""
This type stub file was generated by pyright.
"""

import pandas as pd
from typing import Optional
from openbb_terminal.decorators import check_api_key, log_start_end

""" News Model """
__docformat__ = ...
logger = ...
@log_start_end(log=logger)
@check_api_key(["API_NEWS_TOKEN"])
def get_news(query: str, limit: int = ..., start_date: Optional[str] = ..., show_newest: bool = ..., sources: str = ...) -> pd.DataFrame:
    """Get news for a given term. [Source: NewsAPI]

    Parameters
    ----------
    query : str
        term to search on the news articles
    start_date: Optional[str]
        date to start searching articles from formatted YYYY-MM-DD
    show_newest: bool
        flag to show newest articles first
    sources: str
        sources to exclusively show news from (comma separated)

    Returns
    -------
    pd.DataFrame
        DataFrame with columns Date, Description, URL
    """
    ...

