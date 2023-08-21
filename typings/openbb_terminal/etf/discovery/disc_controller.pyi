"""
This type stub file was generated by pyright.
"""

from typing import List, Optional
from openbb_terminal.decorators import log_start_end
from openbb_terminal.parent_classes import BaseController

"""Discovery Controller Module"""
__docformat__ = ...
logger = ...
class DiscoveryController(BaseController):
    """Discovery Controller class"""
    CHOICES_COMMANDS = ...
    PATH = ...
    CHOICES_GENERATION = ...
    def __init__(self, queue: Optional[List[str]] = ...) -> None:
        """Constructor"""
        ...
    
    def print_help(self): # -> None:
        """Print help"""
        ...
    
    @log_start_end(log=logger)
    def call_gainers(self, other_args): # -> None:
        """Process gainers command"""
        ...
    
    @log_start_end(log=logger)
    def call_decliners(self, other_args): # -> None:
        """Process decliners command"""
        ...
    
    @log_start_end(log=logger)
    def call_active(self, other_args): # -> None:
        """Process gainers command"""
        ...
    


