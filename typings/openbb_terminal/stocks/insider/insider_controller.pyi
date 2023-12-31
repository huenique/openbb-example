"""
This type stub file was generated by pyright.
"""

import pandas as pd
from typing import List, Optional
from openbb_terminal.decorators import log_start_end
from openbb_terminal.parent_classes import StockBaseController

"""Insider Controller Module"""
__docformat__ = ...
logger = ...
class InsiderController(StockBaseController):
    """Screener Controller class"""
    CHOICES_COMMANDS = ...
    preset_choices = ...
    PATH = ...
    CHOICES_GENERATION = ...
    def __init__(self, ticker: str, start: str, interval: str, stock: pd.DataFrame, queue: Optional[List[str]] = ...) -> None:
        """Constructor"""
        ...
    
    def print_help(self): # -> None:
        """Print help"""
        ...
    
    def custom_reset(self): # -> list[str] | list[Unknown]:
        """Class specific component of reset command"""
        ...
    
    @log_start_end(log=logger)
    def call_view(self, other_args: List[str]): # -> None:
        """Process view command"""
        ...
    
    @log_start_end(log=logger)
    def call_set(self, other_args: List[str]): # -> None:
        """Process set command"""
        ...
    
    @log_start_end(log=logger)
    def call_filter(self, other_args: List[str]): # -> None:
        """Process filter command"""
        ...
    
    @log_start_end(log=logger)
    def call_stats(self, other_args: List[str]): # -> None:
        """Process stats command"""
        ...
    
    @log_start_end(log=logger)
    def call_lcb(self, other_args: List[str]): # -> None:
        """Process latest-cluster-buys"""
        ...
    
    @log_start_end(log=logger)
    def call_lpsb(self, other_args: List[str]): # -> None:
        """Process latest-penny-stock-buys"""
        ...
    
    @log_start_end(log=logger)
    def call_lit(self, other_args: List[str]): # -> None:
        """Process latest-insider-trading"""
        ...
    
    @log_start_end(log=logger)
    def call_lip(self, other_args: List[str]): # -> None:
        """Process insider-purchases"""
        ...
    
    @log_start_end(log=logger)
    def call_blip(self, other_args: List[str]): # -> None:
        """Process latest-insider-purchases-25k"""
        ...
    
    @log_start_end(log=logger)
    def call_blop(self, other_args: List[str]): # -> None:
        """Process latest-officer-purchases-25k"""
        ...
    
    @log_start_end(log=logger)
    def call_blcp(self, other_args: List[str]): # -> None:
        """Process latest-ceo-cfo-purchases-25k"""
        ...
    
    @log_start_end(log=logger)
    def call_lis(self, other_args: List[str]): # -> None:
        """Process insider-sales"""
        ...
    
    @log_start_end(log=logger)
    def call_blis(self, other_args: List[str]): # -> None:
        """Process latest-insider-sales-100k"""
        ...
    
    @log_start_end(log=logger)
    def call_blos(self, other_args: List[str]): # -> None:
        """Process latest-officer-sales-100k"""
        ...
    
    @log_start_end(log=logger)
    def call_blcs(self, other_args: List[str]): # -> None:
        """Process latest-ceo-cfo-sales-100k"""
        ...
    
    @log_start_end(log=logger)
    def call_topt(self, other_args: List[str]): # -> None:
        """Process top-officer-purchases-of-the-day"""
        ...
    
    @log_start_end(log=logger)
    def call_toppw(self, other_args: List[str]): # -> None:
        """Process top-officer-purchases-of-the-week"""
        ...
    
    @log_start_end(log=logger)
    def call_toppm(self, other_args: List[str]): # -> None:
        """Process top-officer-purchases-of-the-month"""
        ...
    
    @log_start_end(log=logger)
    def call_tipt(self, other_args: List[str]): # -> None:
        """Process top-insider-purchases-of-the-day"""
        ...
    
    @log_start_end(log=logger)
    def call_tippw(self, other_args: List[str]): # -> None:
        """Process top-insider-purchases-of-the-week"""
        ...
    
    @log_start_end(log=logger)
    def call_tippm(self, other_args: List[str]): # -> None:
        """Process top-insider-purchases-of-the-month"""
        ...
    
    @log_start_end(log=logger)
    def call_tist(self, other_args: List[str]): # -> None:
        """Process top-insider-sales-of-the-day"""
        ...
    
    @log_start_end(log=logger)
    def call_tispw(self, other_args: List[str]): # -> None:
        """Process top-insider-sales-of-the-week"""
        ...
    
    @log_start_end(log=logger)
    def call_tispm(self, other_args: List[str]): # -> None:
        """Process top-insider-sales-of-the-month"""
        ...
    
    @log_start_end(log=logger)
    def call_act(self, other_args: List[str]): # -> None:
        """Process act command"""
        ...
    
    @log_start_end(log=logger)
    def call_lins(self, other_args: List[str]): # -> None:
        """Process lins command"""
        ...
    


