"""
This type stub file was generated by pyright.
"""

from pathlib import Path
from typing import List, Optional, Union
from openbb_terminal.decorators import log_start_end
from openbb_terminal.parent_classes import BaseController

"""Feature Flags Controller Module"""
__docformat__ = ...
logger = ...
def set_and_save_preference(name: str, value: Union[bool, Path, str]): # -> None:
    """Set preference and write to .env

    Parameters
    ----------
    name : str
        Preference name
    value : Union[bool, Path, str]
        Preference value
    """
    ...

class FeatureFlagsController(BaseController):
    """Feature Flags Controller class"""
    CHOICES_COMMANDS: List[str] = ...
    PATH = ...
    def __init__(self, queue: Optional[List[str]] = ...) -> None:
        """Constructor"""
        ...
    
    def print_help(self): # -> None:
        """Print help"""
        ...
    
    def call_overwrite(self, _): # -> None:
        """Process overwrite command"""
        ...
    
    def call_version(self, _): # -> None:
        """Process version command"""
        ...
    
    def call_retryload(self, _): # -> None:
        """Process retryload command"""
        ...
    
    @log_start_end(log=logger)
    def call_interactive(self, _): # -> None:
        """Process interactive command"""
        ...
    
    @log_start_end(log=logger)
    def call_cls(self, _): # -> None:
        """Process cls command"""
        ...
    
    @log_start_end(log=logger)
    def call_promptkit(self, _): # -> None:
        """Process promptkit command"""
        ...
    
    @log_start_end(log=logger)
    def call_thoughts(self, _): # -> None:
        """Process thoughts command"""
        ...
    
    @log_start_end(log=logger)
    def call_reporthtml(self, _): # -> None:
        """Process reporthtml command"""
        ...
    
    @log_start_end(log=logger)
    def call_exithelp(self, _): # -> None:
        """Process exithelp command"""
        ...
    
    @log_start_end(log=logger)
    def call_rcontext(self, _): # -> None:
        """Process rcontext command"""
        ...
    
    @log_start_end(log=logger)
    def call_dt(self, _): # -> None:
        """Process dt command"""
        ...
    
    @log_start_end(log=logger)
    def call_richpanel(self, _): # -> None:
        """Process richpanel command"""
        ...
    
    @log_start_end(log=logger)
    def call_tbhint(self, _): # -> None:
        """Process tbhint command"""
        ...
    


