"""
This type stub file was generated by pyright.
"""

from typing import List, Optional
from openbb_terminal.decorators import log_start_end
from openbb_terminal.parent_classes import CryptoBaseController

"""Cryptocurrency Context Controller"""
__docformat__ = ...
logger = ...
FIND_KEYS = ...
CRYPTO_SOURCES = ...
class CryptoController(CryptoBaseController):
    """Crypto Controller"""
    CHOICES_COMMANDS = ...
    CHOICES_MENUS = ...
    DD_VIEWS_MAPPING = ...
    PATH = ...
    FILE_PATH = ...
    CHOICES_GENERATION = ...
    def __init__(self, queue: Optional[List[str]] = ...) -> None:
        """Constructor"""
        ...
    
    def print_help(self): # -> None:
        """Print help"""
        ...
    
    @log_start_end(log=logger)
    def call_prt(self, other_args): # -> None:
        """Process prt command"""
        ...
    
    @log_start_end(log=logger)
    def call_price(self, other_args): # -> None:
        """Process price command"""
        ...
    
    @log_start_end(log=logger)
    def call_candle(self, other_args): # -> None:
        """Process candle command"""
        ...
    
    @log_start_end(log=logger)
    def call_ta(self, _): # -> None:
        """Process ta command"""
        ...
    
    @log_start_end(log=logger)
    def call_tools(self, _): # -> None:
        """Process tools command"""
        ...
    
    @log_start_end(log=logger)
    def call_disc(self, _): # -> None:
        """Process disc command"""
        ...
    
    @log_start_end(log=logger)
    def call_ov(self, _): # -> None:
        """Process ov command"""
        ...
    
    @log_start_end(log=logger)
    def call_defi(self, _): # -> None:
        """Process defi command"""
        ...
    
    @log_start_end(log=logger)
    def call_headlines(self, other_args): # -> None:
        """Process sentiment command"""
        ...
    
    @log_start_end(log=logger)
    def call_dd(self, _): # -> None:
        """Process dd command"""
        ...
    
    @log_start_end(log=logger)
    def call_qa(self, _): # -> None:
        """Process qa command"""
        ...
    
    @log_start_end(log=logger)
    def call_onchain(self, _): # -> None:
        """Process onchain command"""
        ...
    
    @log_start_end(log=logger)
    def call_nft(self, _): # -> None:
        """Process nft command"""
        ...
    
    @log_start_end(log=logger)
    def call_find(self, other_args): # -> None:
        """Process find command"""
        ...
    
    @log_start_end(log=logger)
    def call_forecast(self, _): # -> None:
        """Process forecast command"""
        ...
    


