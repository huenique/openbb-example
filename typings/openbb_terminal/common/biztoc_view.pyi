"""
This type stub file was generated by pyright.
"""

from typing import Optional
from openbb_terminal.decorators import check_api_key, log_start_end

""" BizToc View """
__docformat__ = ...
logger = ...
@check_api_key(["API_BIZTOC_TOKEN"])
@log_start_end(log=logger)
def display_news(term: str = ..., tag: str = ..., source: str = ..., limit: int = ..., export: str = ..., sheet_name: Optional[str] = ..., sort: str = ...): # -> None:
    """Plots news for a given term and source. [Source: Feedparser]

    Parameters
    ----------
    term : str
        term to search on the news articles
    tag : str
        display news articles for an individual tag
    source : str
        source to exclusively show news from
    limit : int
        number of articles to display
    export : str
        Export dataframe data to csv,json,xlsx file
    sort: str
        the column to sort by
    """
    ...

@check_api_key(["API_BIZTOC_TOKEN"])
def display_sources(export: str = ..., sheet_name: Optional[str] = ...): # -> None:
    """Plots available sources for news."""
    ...

@check_api_key(["API_BIZTOC_TOKEN"])
def display_tags(export: str = ..., sheet_name: Optional[str] = ...): # -> None:
    """Plots currently trending tags."""
    ...

