"""
This type stub file was generated by pyright.
"""

from typing import Optional
from openbb_terminal.decorators import log_start_end

"""Keys view"""
__docformat__ = ...
logger = ...
@log_start_end(log=logger)
def display_keys(show: bool = ..., export: str = ..., sheet_name: Optional[str] = ...): # -> None:
    """Display currently set API keys.

    Parameters
    ----------
        show: bool
            Flag to choose whether to show actual keys or not.
            By default, False.
        export : str
            Export dataframe data to csv,json,xlsx file
    """
    ...

