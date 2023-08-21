"""
This type stub file was generated by pyright.
"""

from typing import List, Optional
from openbb_terminal.decorators import log_start_end
from openbb_terminal.parent_classes import BaseController

logger = ...
class DegiroController(BaseController):
    """Degiro Controller class"""
    CHOICES_COMMANDS = ...
    PATH = ...
    def __init__(self, queue: Optional[List[str]] = ...) -> None:
        """Constructor"""
        ...
    
    def print_help(self): # -> None:
        """Print help."""
        ...
    
    @log_start_end(log=logger)
    def call_cancel(self, other_args: List[str]): # -> None:
        """Cancel an order using the `id`."""
        ...
    
    @log_start_end(log=logger)
    def call_companynews(self, other_args: List[str]): # -> None:
        """Display news related to a company using its ISIN."""
        ...
    
    @log_start_end(log=logger)
    def call_create(self, other_args: List[str]): # -> None:
        """Create an order."""
        ...
    
    @log_start_end(log=logger)
    def call_hold(self, other_args): # -> None:
        """Display held products."""
        ...
    
    @log_start_end(log=logger)
    def call_lastnews(self, other_args: List[str]): # -> None:
        """Display latest news."""
        ...
    
    @log_start_end(log=logger)
    def call_login(self, other_args: List[str]): # -> None:
        """Connect to Degiro's API."""
        ...
    
    @log_start_end(log=logger)
    def call_logout(self, other_args: List[str]): # -> None:
        """Log out from Degiro's API."""
        ...
    
    @log_start_end(log=logger)
    def call_lookup(self, other_args: List[str]): # -> None:
        """Search for products by their name."""
        ...
    
    @log_start_end(log=logger)
    def call_pending(self, other_args: List[str]): # -> None:
        """Display pending orders."""
        ...
    
    @log_start_end(log=logger)
    def call_topnews(self, other_args: List[str]): # -> None:
        """Display top news."""
        ...
    
    @log_start_end(log=logger)
    def call_update(self, other_args: List[str]): # -> None:
        """Update an order."""
        ...
    
    @log_start_end(log=logger)
    def call_paexport(self, other_args: List[str]): # -> None:
        """Export transactions for Portfolio menu into csv format. The transactions
        file is exported to the portfolio/holdings folder and can be loaded directly
        in the Portfolio menu."""
        ...
    

