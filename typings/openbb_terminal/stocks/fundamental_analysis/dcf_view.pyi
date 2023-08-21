"""
This type stub file was generated by pyright.
"""

import pandas as pd
from typing import List, Optional, Union
from openpyxl import Workbook
from openbb_terminal.decorators import log_start_end

""" DCF View """
__docformat__ = ...
logger = ...
class CreateExcelFA:
    @log_start_end(log=logger)
    def __init__(self, symbol: str, beta: float, audit: bool = ..., ratios: bool = ..., len_pred: int = ..., max_similars: int = ..., no_filter: bool = ..., growth: bool = ...) -> None:
        """
        Creates a detailed DCF for a given company

        Parameters
        ----------
        symbol : str
            The ticker symbol to create a DCF for
        audit : bool
            Whether or not to show that the balance sheet and income statement tie-out
        ratios : bool
            Whether to show ratios for the company and for similar companies
        len_pred : int
            The number of years to make predictions for before assuming a terminal value
        max_similars : int
            The maximum number of similar companies to show, will be less if there are not enough
        no_filter : bool
            Disable filtering of similar companies to being in the same market cap category
        growth : bool
            When true this turns the revenue assumption from linear regression to percentage growth
        """
        ...
    
    @log_start_end(log=logger)
    def create_workbook(self): # -> None:
        ...
    
    @log_start_end(log=logger)
    def get_data(self, statement: str, row: int, header: bool) -> pd.DataFrame:
        ...
    
    @log_start_end(log=logger)
    def add_estimates(self): # -> None:
        ...
    
    @log_start_end(log=logger)
    def create_dcf(self): # -> None:
        ...
    
    @log_start_end(log=logger)
    def create_header(self, ws: Workbook): # -> None:
        ...
    
    @log_start_end(log=logger)
    def run_audit(self): # -> None:
        ...
    
    @log_start_end(log=logger)
    def get_growth(self, x_ind: str, y_ind: str, no_neg: bool = ..., pred_type: str = ...): # -> None:
        """Add growth to a column. Usually this is linear but other options are allowed

        x_ind: str
            The x variable to use. This is unused if growth is the pred_type
        y_ind: str
            The y variable to use
        no_neg: bool
            Whether or not the value can have negative numbers (profit can be revenue cannot)
        pred_type: str
            This is assumed to be linear but growth is allowed as well
        """
        ...
    
    @log_start_end(log=logger)
    def get_sum(self, row: Union[int, str], first: str, adds: List[str], subtracts: List[str], audit: bool = ..., text: Optional[str] = ...): # -> None:
        ...
    
    def title_to_row(self, title: str) -> int:
        ...
    
    @log_start_end(log=logger)
    def custom_exp(self, row: Union[int, str], text: str, ws: int = ..., column: Optional[str] = ...): # -> None:
        ...
    
    @log_start_end(log=logger)
    def add_ratios(self): # -> None:
        ...
    

