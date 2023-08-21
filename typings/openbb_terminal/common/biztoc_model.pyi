"""
This type stub file was generated by pyright.
"""

import pandas as pd
from openbb_terminal.decorators import check_api_key

""" BizToc Model """
__docformat__ = ...
def get_sources() -> pd.DataFrame:
    """Get list of source ids to query for individual news articles via get_news. [Source: BizToc]

    Parameters
    ----------

    Returns
    -------
    sources: pd.DataFrame
        list of sources
    """
    ...

def get_tags() -> pd.DataFrame:
    """Get list of trending tags to query for individual news articles via get_news. [Source: BizToc]

    Parameters
    ----------

    Returns
    -------
    tags: pd.DataFrame
        list of tags
    """
    ...

@check_api_key(["API_BIZTOC_TOKEN"])
def get_news(term: str = ..., tag: str = ..., source: str = ..., sort: str = ..., limit: int = ..., display_message: bool = ...) -> pd.DataFrame:
    """Get news for a given term and source. [Source: BizToc]

    Parameters
    ----------
    term : str
        term to search on the news articles
    tag : str
        display news articles for an individual tag
    source: str
        source to exclusively show news from
    sort: str
        the column to sort by
    limit : int
        number of articles to display
    display_message: bool
        whether to display a message to the user

    Returns
    -------
    articles: pd.DataFrame
        term to search on the news articles
    """
    ...

BIZTOC_TAGS = ...