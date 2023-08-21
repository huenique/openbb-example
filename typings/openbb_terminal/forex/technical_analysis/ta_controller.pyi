"""
This type stub file was generated by pyright.
"""

import pandas as pd
from datetime import datetime
from typing import List, Optional
from openbb_terminal.decorators import log_start_end
from openbb_terminal.parent_classes import StockBaseController

"""Crypto Technical Analysis Controller Module"""
__docformat__ = ...
logger = ...
class TechnicalAnalysisController(StockBaseController):
    """Technical Analysis Controller class"""
    CHOICES_COMMANDS = ...
    PATH = ...
    CHOICES_GENERATION = ...
    def __init__(self, ticker: str, source: str, start: datetime, interval: str, data: pd.DataFrame, queue: Optional[List[str]] = ...) -> None:
        """Constructor"""
        ...
    
    def print_help(self): # -> None:
        """Print help"""
        ...
    
    def custom_reset(self): # -> list[str] | list[Unknown]:
        """Class specific component of reset command"""
        ...
    
    @log_start_end(log=logger)
    def call_ema(self, other_args: List[str]): # -> None:
        """Process ema command"""
        ...
    
    @log_start_end(log=logger)
    def call_sma(self, other_args: List[str]): # -> None:
        """Process sma command"""
        ...
    
    @log_start_end(log=logger)
    def call_zlma(self, other_args: List[str]): # -> None:
        """Process zlma command"""
        ...
    
    @log_start_end(log=logger)
    def call_cci(self, other_args: List[str]): # -> None:
        """Process cci command"""
        ...
    
    @log_start_end(log=logger)
    def call_macd(self, other_args: List[str]): # -> None:
        """Process macd command"""
        ...
    
    @log_start_end(log=logger)
    def call_rsi(self, other_args: List[str]): # -> None:
        """Process rsi command"""
        ...
    
    @log_start_end(log=logger)
    def call_stoch(self, other_args: List[str]): # -> None:
        """Process stoch command"""
        ...
    
    @log_start_end(log=logger)
    def call_fisher(self, other_args: List[str]): # -> None:
        """Process fisher command"""
        ...
    
    @log_start_end(log=logger)
    def call_cg(self, other_args: List[str]): # -> None:
        """Process cg command"""
        ...
    
    @log_start_end(log=logger)
    def call_adx(self, other_args: List[str]): # -> None:
        """Process adx command"""
        ...
    
    @log_start_end(log=logger)
    def call_aroon(self, other_args: List[str]): # -> None:
        """Process aroon command"""
        ...
    
    @log_start_end(log=logger)
    def call_bbands(self, other_args: List[str]): # -> None:
        """Process bbands command"""
        ...
    
    @log_start_end(log=logger)
    def call_donchian(self, other_args: List[str]): # -> None:
        """Process donchian command"""
        ...
    
    @log_start_end(log=logger)
    def call_ad(self, other_args: List[str]): # -> None:
        """Process ad command"""
        ...
    
    @log_start_end(log=logger)
    def call_obv(self, other_args: List[str]): # -> None:
        """Process obv command"""
        ...
    
    @log_start_end(log=logger)
    def call_fib(self, other_args: List[str]): # -> None:
        """Process fib command"""
        ...
    

