"""
This type stub file was generated by pyright.
"""

from typing import List, Optional
from openbb_terminal.decorators import log_start_end
from openbb_terminal.parent_classes import BaseController

"""Cryptocurrency Overview Controller"""
__docformat__ = ...
logger = ...
class OverviewController(BaseController):
    """Overview Controller class"""
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
    def call_hm(self, other_args): # -> None:
        """Process hm command"""
        ...
    
    @log_start_end(log=logger)
    def call_fun(self, other_args): # -> None:
        """Process fun command"""
        ...
    
    @log_start_end(log=logger)
    def call_ch(self, other_args): # -> None:
        """Process ch command"""
        ...
    
    @log_start_end(log=logger)
    def call_btcrb(self, other_args: List[str]): # -> None:
        """Process btcrb command"""
        ...
    
    @log_start_end(log=logger)
    def call_altindex(self, other_args: List[str]): # -> None:
        """Process altindex command"""
        ...
    
    @log_start_end(log=logger)
    def call_wf(self, other_args: List[str]): # -> None:
        """Process wf command"""
        ...
    
    @log_start_end(log=logger)
    def call_ewf(self, other_args: List[str]): # -> None:
        """Process ewf command"""
        ...
    
    @log_start_end(log=logger)
    def call_wfpe(self, other_args: List[str]): # -> None:
        """Process wfpe command"""
        ...
    
    @log_start_end(log=logger)
    def call_hold(self, other_args): # -> None:
        """Process hold command"""
        ...
    
    @log_start_end(log=logger)
    def call_categories(self, other_args): # -> None:
        """Process top_categories command"""
        ...
    
    @log_start_end(log=logger)
    def call_stables(self, other_args): # -> None:
        """Process stables command"""
        ...
    
    @log_start_end(log=logger)
    def call_cr(self, other_args): # -> None:
        """Process cr command"""
        ...
    
    @log_start_end(log=logger)
    def call_exchanges(self, other_args): # -> None:
        """Process exchanges command"""
        ...
    
    @log_start_end(log=logger)
    def call_exrates(self, other_args): # -> None:
        """Process exchange_rates command"""
        ...
    
    @log_start_end(log=logger)
    def call_indexes(self, other_args): # -> None:
        """Process indexes command"""
        ...
    
    @log_start_end(log=logger)
    def call_derivatives(self, other_args): # -> None:
        """Process derivatives command"""
        ...
    
    @log_start_end(log=logger)
    def call_global(self, other_args): # -> None:
        """Process global command"""
        ...
    
    @log_start_end(log=logger)
    def call_defi(self, other_args): # -> None:
        """Process defi command"""
        ...
    
    @log_start_end(log=logger)
    def call_markets(self, other_args): # -> None:
        """Process markets command"""
        ...
    
    @log_start_end(log=logger)
    def call_exmarkets(self, other_args): # -> None:
        """Process exmarkets command"""
        ...
    
    @log_start_end(log=logger)
    def call_info(self, other_args): # -> None:
        """Process info command"""
        ...
    
    @log_start_end(log=logger)
    def call_platforms(self, other_args): # -> None:
        """Process platforms command"""
        ...
    
    @log_start_end(log=logger)
    def call_contracts(self, other_args): # -> None:
        """Process contracts command"""
        ...
    
    @log_start_end(log=logger)
    def call_pairs(self, other_args): # -> None:
        """Process pairs command"""
        ...
    
    @log_start_end(log=logger)
    def call_news(self, other_args): # -> None:
        """Process news command"""
        ...
    

