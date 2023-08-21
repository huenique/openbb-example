"""
This type stub file was generated by pyright.
"""

import pandas as pd
from typing import Any, Optional
from openbb_terminal.decorators import log_start_end

"""CoinPaprika model"""
__docformat__ = ...
logger = ...
CATEGORIES = ...
FILTERS = ...
@log_start_end(log=logger)
def get_search_results(query: str, category: Optional[Any] = ..., modifier: Optional[Any] = ..., sortby: str = ..., ascend: bool = ...) -> pd.DataFrame:
    """Search CoinPaprika. [Source: CoinPaprika]

    Parameters
    ----------
    query:  str
        phrase for search
    category:  Optional[Any]
        one or more categories (comma separated) to search.
        Available options: currencies|exchanges|icos|people|tags
        Default: currencies,exchanges,icos,people,tags
    modifier: Optional[Any]
        set modifier for search results. Available options: symbol_search -
        search only by symbol (works for currencies only)
    sortby: str
        Key to sort data. The table can be sorted by every of its columns. Refer to
        API documentation (see https://api.coinpaprika.com/docs#tag/Tools/paths/~1search/get)
    ascend: bool
        Flag to sort data descending

    Returns
    -------
    pd.DataFrame
        Search Results
        Columns: Metric, Value
    """
    ...
