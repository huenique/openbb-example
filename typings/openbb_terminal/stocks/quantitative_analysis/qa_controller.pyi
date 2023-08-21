"""
This type stub file was generated by pyright.
"""

import pandas as pd
from datetime import datetime
from typing import List, Optional
from openbb_terminal.decorators import log_start_end
from openbb_terminal.parent_classes import StockBaseController

"""Quantitative Analysis Controller Module"""
__docformat__ = ...
logger = ...
def no_data_message(): # -> None:
    """Print message when no ticker is loaded"""
    ...

class QaController(StockBaseController):
    """Quantitative Analysis Controller class"""
    CHOICES_COMMANDS = ...
    stock_interval = ...
    stock_sources = ...
    distributions = ...
    FULLER_REG = ...
    KPS_REG = ...
    VALID_DISTRIBUTIONS = ...
    PATH = ...
    CHOICES_GENERATION = ...
    def __init__(self, ticker: str, start: datetime, interval: str, stock: pd.DataFrame, queue: Optional[List[str]] = ...) -> None:
        """Constructor"""
        ...
    
    def print_help(self): # -> None:
        """Print help"""
        ...
    
    def custom_reset(self): # -> list[str] | list[Unknown]:
        """Class specific component of reset command"""
        ...
    
    @log_start_end(log=logger)
    def call_pick(self, other_args: List[str]): # -> None:
        """Process pick command"""
        ...
    
    @log_start_end(log=logger)
    def call_raw(self, other_args: List[str]): # -> None:
        ...
    
    @log_start_end(log=logger)
    def call_summary(self, other_args: List[str]): # -> None:
        """Process summary command"""
        ...
    
    @log_start_end(log=logger)
    def call_line(self, other_args: List[str]): # -> None:
        """Process line command"""
        ...
    
    @log_start_end(log=logger)
    def call_hist(self, other_args: List[str]): # -> None:
        """Process hist command"""
        ...
    
    @log_start_end(log=logger)
    def call_cdf(self, other_args: List[str]): # -> None:
        """Process cdf command"""
        ...
    
    @log_start_end(log=logger)
    def call_bw(self, other_args: List[str]): # -> None:
        """Process bwy command"""
        ...
    
    @log_start_end(log=logger)
    def call_decompose(self, other_args: List[str]): # -> None:
        """Process decompose command"""
        ...
    
    @log_start_end(log=logger)
    def call_cusum(self, other_args: List[str]): # -> None:
        """Process cusum command"""
        ...
    
    @log_start_end(log=logger)
    def call_acf(self, other_args: List[str]): # -> None:
        """Process acf command"""
        ...
    
    @log_start_end(log=logger)
    def call_rolling(self, other_args: List[str]): # -> None:
        """Process rolling command"""
        ...
    
    @log_start_end(log=logger)
    def call_spread(self, other_args: List[str]): # -> None:
        """Process spread command"""
        ...
    
    @log_start_end(log=logger)
    def call_quantile(self, other_args: List[str]): # -> None:
        """Process quantile command"""
        ...
    
    @log_start_end(log=logger)
    def call_skew(self, other_args: List[str]): # -> None:
        """Process skew command"""
        ...
    
    @log_start_end(log=logger)
    def call_kurtosis(self, other_args: List[str]): # -> None:
        """Process kurtosis command"""
        ...
    
    @log_start_end(log=logger)
    def call_normality(self, other_args: List[str]): # -> None:
        """Process normality command"""
        ...
    
    @log_start_end(log=logger)
    def call_qqplot(self, other_args: List[str]): # -> None:
        """Process qqplot command"""
        ...
    
    @log_start_end(log=logger)
    def call_unitroot(self, other_args: List[str]): # -> None:
        """Process unitroot command"""
        ...
    
    @log_start_end(log=logger)
    def call_capm(self, other_args: List[str]): # -> None:
        """Process capm command"""
        ...
    
    @log_start_end(log=logger)
    def call_beta(self, other_args: List[str]): # -> None:
        """Call the beta command on loaded ticker"""
        ...
    
    @log_start_end(log=logger)
    def call_var(self, other_args: List[str]): # -> None:
        """Process var command"""
        ...
    
    @log_start_end(log=logger)
    def call_es(self, other_args: List[str]): # -> None:
        """Process es command"""
        ...
    
    @log_start_end(log=logger)
    def call_sh(self, other_args: List[str]): # -> None:
        """Process sh command"""
        ...
    
    @log_start_end(log=logger)
    def call_so(self, other_args: List[str]): # -> None:
        """Process so command"""
        ...
    
    @log_start_end(log=logger)
    def call_om(self, other_args: List[str]): # -> None:
        """Process om command"""
        ...
    


