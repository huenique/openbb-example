"""
This type stub file was generated by pyright.
"""

from pandas.core.frame import DataFrame
from openbb_terminal.decorators import log_start_end

""" Short Interest View """
__docformat__ = ...
logger = ...
@log_start_end(log=logger)
def get_high_short_interest() -> DataFrame:
    """Returns a high short interest DataFrame

    Returns
    -------
    DataFrame
        High short interest Dataframe with the following columns:
        Ticker, Company, Exchange, ShortInt, Float, Outstd, Industry
    """
    ...
