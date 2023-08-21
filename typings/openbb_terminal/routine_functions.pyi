"""
This type stub file was generated by pyright.
"""

from typing import List, Optional, Tuple

MONTHS_VALUE = ...
WEEKDAY_VALUE = ...
def is_reset(command: str) -> bool:
    """Test whether a command is a reset command

    Parameters
    ----------
    command : str
        The command to test

    Returns
    -------
    answer : bool
        Whether the command is a reset command
    """
    ...

def match_and_return_openbb_keyword_date(keyword: str) -> str:
    """Return OpenBB keyword into date

    Parameters
    ----------
    keyword : str
        String with potential OpenBB keyword (e.g. 1MONTHAGO,LASTFRIDAY,3YEARSFROMNOW,NEXTTUESDAY)

    Returns
    ----------
        str: Date with format YYYY-MM-DD
    """
    ...

def parse_openbb_script(raw_lines: List[str], script_inputs: Optional[List[str]] = ...) -> Tuple[str, str]:
    """
    Parse .openbb script

    Parameters
    ----------
    raw_lines : List[str]
        Lines from .openbb script
    script_inputs: str, optional
        Inputs to the script that come externally

    Returns
    -------
    str
        Error that occurred - if empty means no error
    str
        Processed string from .openbb script that can be run by the OpenBB Terminal
    """
    ...
