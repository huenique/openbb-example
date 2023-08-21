"""
This type stub file was generated by pyright.
"""

import pandas as pd
from typing import List
from openbb_terminal.decorators import log_start_end

"""Token Terminal Model"""
logger = ...
token_terminal = ...
PROJECTS_DATA = ...
TIMELINES = ...
CATEGORIES = ...
METRICS = ...
@log_start_end(log=logger)
def get_possible_timelines() -> List[str]:
    """This function returns the available timelines.

    Returns
    -------
    List[str]
        A list with the available timelines values.
    """
    ...

@log_start_end(log=logger)
def get_possible_categories() -> List[str]:
    """This function returns the available categories.

    Returns
    -------
    List[str]
        A list with the available categories values.
    """
    ...

@log_start_end(log=logger)
def get_possible_metrics() -> List[str]:
    """This function returns the available metrics.

    Returns
    -------
    List[str]
        A list with the available metrics values.
    """
    ...

@log_start_end(log=logger)
def get_fundamental_metrics(metric: str, category: str = ..., timeline: str = ..., ascend: bool = ...) -> pd.Series:
    """Get fundamental metrics [Source: Token Terminal]

    Parameters
    ----------
    metric : str
        The metric of interest. See `get_possible_metrics()` for available metrics.
    category : str
        The category of interest. See `get_possible_categories()` for available categories.
        The default value is an empty string which means that all categories are considered.
    timeline : str
        The category of interest. See `get_possible_timelines()` for available timelines.
    ascend : bool
        Direction of the sort. If True, the data is sorted in ascending order.

    Returns
    -------
    pd.Series
        Project, Metric value
    """
    ...

