"""
This type stub file was generated by pyright.
"""

from typing import List
from openbb_terminal.decorators import log_start_end

logger = ...
@log_start_end(log=logger)
def get_fd_equities_list() -> List:
    """Load FD list of equity symbols."""
    ...

@log_start_end(log=logger)
def get_exchanges_short_names() -> List:
    """Load FD list of equity symbols."""
    ...

