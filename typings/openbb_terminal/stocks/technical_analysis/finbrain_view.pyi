"""
This type stub file was generated by pyright.
"""

from openbb_terminal.decorators import log_start_end

"""Finbrain view"""
__docformat__ = ...
logger = ...
@log_start_end(log=logger)
def technical_summary_report(symbol: str): # -> None:
    """Print technical summary report provided by FinBrain's API

    Parameters
    ----------
    symbol: str
        Ticker symbol to get the technical summary
    """
    ...
