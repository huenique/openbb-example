"""
This type stub file was generated by pyright.
"""

from typing import List, Optional
from pandas.core.frame import DataFrame
from openbb_terminal.decorators import log_start_end
from openbb_terminal.parent_classes import StockBaseController

"""Fundamental Analysis Controller."""
__docformat__ = ...
logger = ...
no_ticker_message = ...
class FundamentalAnalysisController(StockBaseController):
    """Fundamental Analysis Controller class"""
    CHOICES_COMMANDS = ...
    PATH = ...
    SHRS_CHOICES = ...
    ESTIMATE_CHOICES = ...
    CHOICES_GENERATION = ...
    def __init__(self, ticker: str, start: str, interval: str, stock: DataFrame, suffix: str = ..., queue: Optional[List[str]] = ...) -> None:
        """Constructor"""
        ...
    
    def print_help(self): # -> None:
        """Print help."""
        ...
    
    def custom_reset(self): # -> list[str] | list[Unknown]:
        """Class specific component of reset command"""
        ...
    
    def custom_load_wrapper(self, other_args: List[str]): # -> None:
        """Class specific component of load command"""
        ...
    
    @log_start_end(log=logger)
    def call_analysis(self, other_args: List[str]): # -> None:
        """Process analysis command."""
        ...
    
    @log_start_end(log=logger)
    def call_mgmt(self, other_args: List[str]): # -> None:
        """Process mgmt command."""
        ...
    
    @log_start_end(log=logger)
    def call_overview(self, other_args: List[str]): # -> None:
        """Process overview command."""
        ...
    
    @log_start_end(log=logger)
    def call_score(self, other_args: List[str]): # -> None:
        """Process score command."""
        ...
    
    @log_start_end(log=logger)
    def call_mktcap(self, other_args: List[str]): # -> None:
        """Process enterprise command"""
        ...
    
    @log_start_end(log=logger)
    def call_metrics(self, other_args: List[str]): # -> None:
        """Process metrics command"""
        ...
    
    @log_start_end(log=logger)
    def call_ratios(self, other_args: List[str]): # -> None:
        """Process ratios command"""
        ...
    
    @log_start_end(log=logger)
    def call_growth(self, other_args: List[str]): # -> None:
        """Process growth command"""
        ...
    
    @log_start_end(log=logger)
    def call_epsfc(self, other_args: List[str]): # -> None:
        """Process eps forecast command."""
        ...
    
    @log_start_end(log=logger)
    def call_revfc(self, other_args: List[str]): # -> None:
        """Process revenue forecast command."""
        ...
    
    @log_start_end(log=logger)
    def call_splits(self, other_args: List[str]): # -> None:
        """Process splits command."""
        ...
    
    @log_start_end(log=logger)
    def call_shrs(self, other_args: List[str]): # -> None:
        """Process shrs command."""
        ...
    
    @log_start_end(log=logger)
    def call_divs(self, other_args: List[str]): # -> None:
        """Process divs command."""
        ...
    
    @log_start_end(log=logger)
    def call_income(self, other_args: List[str]): # -> None:
        """Process income command."""
        ...
    
    @log_start_end(log=logger)
    def call_balance(self, other_args: List[str]): # -> None:
        """Process balance command."""
        ...
    
    @log_start_end(log=logger)
    def call_cash(self, other_args: List[str]): # -> None:
        """Process cash command."""
        ...
    
    @log_start_end(log=logger)
    def call_earnings(self, other_args: List[str]): # -> None:
        """Process earnings command."""
        ...
    
    @log_start_end(log=logger)
    def call_fraud(self, other_args: List[str]): # -> None:
        """Process fraud command."""
        ...
    
    @log_start_end(log=logger)
    def call_dupont(self, other_args: List[str]): # -> None:
        """Process dupont command."""
        ...
    
    @log_start_end(log=logger)
    def call_dcf(self, other_args: List[str]): # -> None:
        """Process dcf command."""
        ...
    
    @log_start_end(log=logger)
    def call_dcfc(self, other_args: List[str]): # -> None:
        """Process dcfc command"""
        ...
    
    @log_start_end(log=logger)
    def call_warnings(self, other_args: List[str]): # -> None:
        """Process warnings command."""
        ...
    
    @log_start_end(log=logger)
    def key_metrics_explained(self, other_args: List[str]): # -> None:
        """Key metrics explained."""
        ...
    
    @log_start_end(log=logger)
    def call_pt(self, other_args: List[str]): # -> None:
        """Process pt command"""
        ...
    
    @log_start_end(log=logger)
    def call_est(self, other_args: List[str]): # -> None:
        """Process est command"""
        ...
    
    @log_start_end(log=logger)
    def call_rot(self, other_args: List[str]): # -> None:
        """Process rot command"""
        ...
    
    @log_start_end(log=logger)
    def call_rating(self, other_args: List[str]): # -> None:
        """Process rating command"""
        ...
    
    @log_start_end(log=logger)
    def call_sec(self, other_args: List[str]): # -> None:
        """Process sec command"""
        ...
    
    @log_start_end(log=logger)
    def call_supplier(self, other_args: List[str]): # -> None:
        """Process supplier command"""
        ...
    
    @log_start_end(log=logger)
    def call_customer(self, other_args: List[str]): # -> None:
        """Process customer command"""
        ...
    


