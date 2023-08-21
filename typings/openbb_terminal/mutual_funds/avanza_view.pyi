"""
This type stub file was generated by pyright.
"""

from openbb_terminal.decorators import log_start_end

"""Avanza View"""
__docformat__ = ...
logger = ...
sector_dict = ...
@log_start_end(log=logger)
def display_allocation(name: str, isin: str, focus: str): # -> None:
    """Displays the allocation of the selected swedish fund

    Parameters
    ----------
    name: str
        Full name of the fund
    isin: str
        ISIN of the fund
    focus: str
        The focus of the displayed allocation/exposure of the fund
    """
    ...

@log_start_end(log=logger)
def display_info(isin: str): # -> None:
    """Displays info of swedish funds

    Parameters
    ----------
    isin: str
        ISIN of the fund
    """
    ...
