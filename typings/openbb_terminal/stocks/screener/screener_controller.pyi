"""
This type stub file was generated by pyright.
"""

from pathlib import Path
from typing import Dict, List, Optional, Union
from openbb_terminal.decorators import log_start_end
from openbb_terminal.parent_classes import BaseController

""" Screener Controller Module """
__docformat__ = ...
logger = ...
class ScreenerController(BaseController):
    """Screener Controller class"""
    CHOICES_MENUS = ...
    CHOICES_COMMANDS = ...
    PRESETS_PATH = ...
    PRESETS_PATH_DEFAULT = ...
    preset_choices: Dict[str, Union[str, Path]] = ...
    if PRESETS_PATH.exists():
        ...
    if PRESETS_PATH_DEFAULT.exists():
        ...
    historical_candle_choices = ...
    PATH = ...
    CHOICES_GENERATION = ...
    def __init__(self, queue: Optional[List[str]] = ...) -> None:
        """Constructor"""
        ...
    
    def parse_input(self, an_input: str) -> List:
        """Parse controller input

        Overrides the parent class function to handle github org/repo path convention.
        See `BaseController.parse_input()` for details.
        """
        ...
    
    def print_help(self): # -> None:
        """Print help"""
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
    def call_overview(self, other_args: List[str]): # -> None:
        """Process overview command"""
        ...
    
    @log_start_end(log=logger)
    def call_valuation(self, other_args: List[str]): # -> None:
        """Process valuation command"""
        ...
    
    @log_start_end(log=logger)
    def call_financial(self, other_args: List[str]): # -> None:
        """Process financial command"""
        ...
    
    @log_start_end(log=logger)
    def call_ownership(self, other_args: List[str]): # -> None:
        """Process ownership command"""
        ...
    
    @log_start_end(log=logger)
    def call_performance(self, other_args: List[str]): # -> None:
        """Process performance command"""
        ...
    
    @log_start_end(log=logger)
    def call_technical(self, other_args: List[str]): # -> None:
        """Process technical command"""
        ...
    
    @log_start_end(log=logger)
    def call_ca(self, _): # -> None:
        """Call the comparison analysis menu with selected tickers"""
        ...
    


