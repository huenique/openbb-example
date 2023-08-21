"""
This type stub file was generated by pyright.
"""

from typing import List, Optional
from openbb_terminal.decorators import log_start_end
from openbb_terminal.parent_classes import BaseController

__docformat__ = ...
logger = ...
class BrokersController(BaseController):
    """Brokers Controller class"""
    CHOICES_COMMANDS: List = ...
    CHOICES_MENUS = ...
    PATH = ...
    CHOICES_GENERATION = ...
    def __init__(self, queue: Optional[List[str]] = ...) -> None:
        """Constructor"""
        ...
    
    def print_help(self): # -> None:
        """Print help"""
        ...
    
    @log_start_end(log=logger)
    def call_degiro(self, _): # -> None:
        """Process degiro command."""
        ...
    
    @log_start_end(log=logger)
    def call_rh(self, _): # -> None:
        """Process rh command."""
        ...
    
    @log_start_end(log=logger)
    def call_cb(self, _): # -> None:
        """Process coinbase command."""
        ...
    


