"""
This type stub file was generated by pyright.
"""

from typing import List, Optional
from openbb_terminal.decorators import log_start_end
from openbb_terminal.parent_classes import BaseController

"""Trading Hours Controller."""
__docformat__ = ...
logger = ...
class TradingHoursController(BaseController):
    """Trading Hours Controller class."""
    CHOICES_COMMANDS = ...
    PATH = ...
    FILE_PATH = ...
    CHOICES_GENERATION = ...
    def __init__(self, ticker: str = ..., queue: Optional[List[str]] = ...) -> None:
        """Construct Data."""
        ...
    
    def print_help(self): # -> None:
        ...
    
    @log_start_end(log=logger)
    def call_symbol(self, other_args: List[str]): # -> None:
        """Process 'symbol' command."""
        ...
    
    @log_start_end(log=logger)
    def call_exchange(self, other_args: List[str]): # -> None:
        """Process 'exchange' command."""
        ...
    
    @log_start_end(log=logger)
    def call_open(self, other_args: List[str]): # -> None:
        """Process 'symbol' command."""
        ...
    
    @log_start_end(log=logger)
    def call_closed(self, other_args: List[str]): # -> None:
        """Process 'symbol' command."""
        ...
    
    @log_start_end(log=logger)
    def call_all(self, other_args: List[str]): # -> None:
        """Process 'symbol' command."""
        ...
    
    @log_start_end(log=logger)
    def call_holidays(self, other_args: List[str]): # -> None:
        """Process 'holidays' command."""
        ...
    


