"""
This type stub file was generated by pyright.
"""

from typing import List, Optional
from openbb_terminal.decorators import log_start_end
from openbb_terminal.parent_classes import BaseController

"""Alternative Data Controller Module"""
__docformat__ = ...
logger = ...
class AlternativeDataController(BaseController):
    """Alternative Controller class"""
    CHOICES_COMMANDS: List[str] = ...
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
    def call_covid(self, _): # -> None:
        """Process covid command"""
        ...
    
    @log_start_end(log=logger)
    def call_oss(self, _): # -> None:
        """Process oss command."""
        ...
    
    @log_start_end(log=logger)
    def call_hn(self, other_args: List[str]): # -> None:
        """Process hn command."""
        ...
    
    @log_start_end(log=logger)
    def call_realestate(self, _): # -> None:
        """Process realestate command."""
        ...
    


