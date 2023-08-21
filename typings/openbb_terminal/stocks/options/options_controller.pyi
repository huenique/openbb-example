"""
This type stub file was generated by pyright.
"""

from typing import List, Optional
from openbb_terminal.decorators import log_start_end
from openbb_terminal.parent_classes import BaseController

""" Options Controller Module """
__docformat__ = ...
logger = ...
class OptionsController(BaseController):
    """Options Controller class"""
    CHOICES_COMMANDS = ...
    CHOICES_MENUS = ...
    grhist_greeks_choices = ...
    unu_sortby_choices = ...
    pcr_length_choices = ...
    plot_vars_choices = ...
    plot_custom_choices = ...
    PATH = ...
    CHOICES_GENERATION = ...
    def __init__(self, ticker: str, queue: Optional[List[str]] = ..., expiration: Optional[str] = ...) -> None:
        """Constructor"""
        ...
    
    def parse_input(self, an_input: str) -> List:
        """Parse controller input

        Overrides the parent class function to handle github org/repo path convention.
        See `BaseController.parse_input()` for details.
        """
        ...
    
    def set_option_chain(self): # -> None:
        ...
    
    def set_current_price(self): # -> None:
        ...
    
    def set_expiry_dates(self): # -> None:
        ...
    
    def update_runtime_choices(self): # -> None:
        """Update runtime choices"""
        ...
    
    def print_help(self): # -> None:
        """Print help."""
        ...
    
    def custom_reset(self): # -> list[str] | list[Unknown]:
        """Class specific component of reset command"""
        ...
    
    @log_start_end(log=logger)
    def call_calc(self, other_args: List[str]): # -> None:
        """Process calc command"""
        ...
    
    @log_start_end(log=logger)
    def call_unu(self, other_args: List[str]): # -> None:
        """Process unu command"""
        ...
    
    @log_start_end(log=logger)
    def call_pcr(self, other_args: List[str]): # -> None:
        ...
    
    @log_start_end(log=logger)
    def call_info(self, other_args: List[str]): # -> None:
        """Process info command"""
        ...
    
    @log_start_end(log=logger)
    def call_grhist(self, other_args: List[str]): # -> None:
        """Process grhist command"""
        ...
    
    @log_start_end(log=logger)
    def call_load(self, other_args: List[str]): # -> None:
        """Process load command"""
        ...
    
    @log_start_end(log=logger)
    def call_exp(self, other_args: List[str]): # -> None:
        """Process exp command"""
        ...
    
    @log_start_end(log=logger)
    def call_hist(self, other_args: List[str]): # -> None:
        """Process hist command"""
        ...
    
    @log_start_end(log=logger)
    def call_chains(self, other_args: List[str]): # -> None:
        """Process chains command"""
        ...
    
    @log_start_end(log=logger)
    def call_vol(self, other_args: List[str]): # -> None:
        """Process vol command"""
        ...
    
    @log_start_end(log=logger)
    def call_voi(self, other_args: List[str]): # -> None:
        """Process voi command"""
        ...
    
    @log_start_end(log=logger)
    def call_oi(self, other_args: List[str]): # -> None:
        """Process oi command"""
        ...
    
    @log_start_end(log=logger)
    def call_plot(self, other_args: List[str]): # -> None:
        """Process plot command"""
        ...
    
    @log_start_end(log=logger)
    def call_vsurf(self, other_args: List[str]): # -> None:
        """Process vsurf command"""
        ...
    
    @log_start_end(log=logger)
    def call_greeks(self, other_args: List[str]): # -> None:
        """Process greeks command"""
        ...
    
    @log_start_end(log=logger)
    def call_hedge(self, _): # -> None:
        """Process hedge command"""
        ...
    
    @log_start_end(log=logger)
    def call_eodchain(self, other_args: List[str]): # -> None:
        """Process greeks command"""
        ...
    


