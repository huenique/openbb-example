"""
This type stub file was generated by pyright.
"""

from typing import Optional
from openbb_terminal.decorators import log_start_end

""" Seeking Alpha View """
__docformat__ = ...
logger = ...
@log_start_end(log=logger)
def display_eps_estimates(symbol: str, export: str = ..., sheet_name: Optional[str] = ...): # -> None:
    """Display eps Estimates

    Parameters
    ----------
    symbol: str
        ticker of company
    """
    ...

@log_start_end(log=logger)
def display_rev_estimates(symbol: str, export: str = ..., sheet_name: Optional[str] = ...): # -> None:
    """Display rev Estimates

    Parameters
    ----------
    symbol: str
        ticker of company
    """
    ...
