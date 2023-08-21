"""
This type stub file was generated by pyright.
"""

from argparse import Namespace
from typing import Optional
from openbb_terminal.decorators import check_api_key, log_start_end

logger = ...
class DegiroView:
    ORDER_ACTION = ...
    ORDER_DURATION = ...
    ORDER_TYPE = ...
    @log_start_end(log=logger)
    def __init__(self) -> None:
        ...
    
    @staticmethod
    @log_start_end(log=logger)
    def help_display(): # -> None:
        ...
    
    @log_start_end(log=logger)
    def cancel(self, ns_parser: Namespace): # -> None:
        ...
    
    @log_start_end(log=logger)
    def companynews(self, symbol: str, limit: int = ..., offset: int = ..., languages: str = ...): # -> None:
        ...
    
    @log_start_end(log=logger)
    def create(self, ns_parser: Namespace): # -> None:
        ...
    
    @log_start_end(log=logger)
    def hold(self, ns_parser: Namespace): # -> None:
        ...
    
    @log_start_end(log=logger)
    def lastnews(self, ns_parser: Namespace): # -> None:
        ...
    
    @log_start_end(log=logger)
    @check_api_key(["DG_USERNAME", "DG_PASSWORD"])
    def login(self, otp: Optional[int] = ...): # -> None:
        ...
    
    @log_start_end(log=logger)
    def logout(self): # -> None:
        ...
    
    @log_start_end(log=logger)
    def lookup(self, ns_parser: Namespace): # -> None:
        ...
    
    @log_start_end(log=logger)
    def pending(self, ns_parser: Namespace): # -> None:
        ...
    
    @log_start_end(log=logger)
    def topnews(self, ns_parser: Namespace): # -> None:
        ...
    
    @log_start_end(log=logger)
    def update(self, ns_parser: Namespace): # -> None:
        ...
    
    @log_start_end(log=logger)
    def transactions_export(self, ns_parser: Namespace): # -> None:
        ...
    


