"""
This type stub file was generated by pyright.
"""

import datetime
import pandas as pd
from typing import List, Union
from degiro_connector.trading.models.trading_pb2 import LatestNews, NewsByCompany, Order, ProductSearch, TopNewsPreview, Update
from openbb_terminal.decorators import log_start_end

logger = ...
class DegiroModel:
    @log_start_end(log=logger)
    def __init__(self) -> None:
        ...
    
    def get_default_credentials(self): # -> Credentials:
        """
        Generate default credentials object from config file

        Returns:
            Credentials: credentials object with default settings
        """
        ...
    
    def get_default_trading_api(self): # -> API:
        """
        Generate default trading api object from config file

        Returns:
            TradingAPI: trading api object with default settings
        """
        ...
    
    @log_start_end(log=logger)
    def cancel(self, order_id: str) -> bool:
        ...
    
    @log_start_end(log=logger)
    def companynews(self, symbol: str, limit: int = ..., offset: int = ..., languages: str = ...) -> NewsByCompany:
        ...
    
    @log_start_end(log=logger)
    def create_calculate_product_id(self, product: int, symbol: str) -> Union[int, None]:
        ...
    
    @log_start_end(log=logger)
    def create_calculate_size(self, price: float, size: int, up_to: float): # -> int:
        ...
    
    @log_start_end(log=logger)
    def create_check(self, order: Order) -> Union[Order.CheckingResponse, bool]:
        ...
    
    @log_start_end(log=logger)
    def create_confirm(self, confirmation_id: str, order: Order) -> Union[Order.ConfirmationResponse, bool]:
        ...
    
    @log_start_end(log=logger)
    def hold_positions(self) -> pd.DataFrame:
        ...
    
    @log_start_end(log=logger)
    def lastnews(self, limit: int) -> LatestNews:
        ...
    
    @log_start_end(log=logger)
    def login(self): # -> None:
        ...
    
    @log_start_end(log=logger)
    def login_default_credentials(self): # -> Credentials:
        ...
    
    @log_start_end(log=logger)
    def logout(self) -> bool:
        ...
    
    @log_start_end(log=logger)
    def lookup(self, limit: int, offset: int, search_text: str) -> ProductSearch:
        ...
    
    @log_start_end(log=logger)
    def pending(self) -> Update.Orders:
        ...
    
    @log_start_end(log=logger)
    def topnews(self) -> TopNewsPreview:
        ...
    
    @log_start_end(log=logger)
    def update(self, order: Order) -> Update.Orders:
        ...
    
    @log_start_end(log=logger)
    def update_pending_order(self, order_id: str) -> Union[None, Order]:
        ...
    
    @log_start_end(log=logger)
    def get_transactions(self, start: datetime.date, end: datetime.date) -> pd.DataFrame:
        ...
    
    @log_start_end(log=logger)
    def get_products_details(self, product_id_list: List[int]) -> pd.DataFrame:
        ...
    
    @log_start_end(log=logger)
    def get_transactions_export(self, start: datetime.date, end: datetime.date, currency: str) -> pd.DataFrame:
        ...
    
    @staticmethod
    @log_start_end(log=logger)
    def export_data(portfolio_df: pd.DataFrame, export: str = ...): # -> None:
        ...
    
    @log_start_end(log=logger)
    def check_session_id(self) -> bool:
        ...
    
    @log_start_end(log=logger)
    def reset_sessionid_and_creds(self): # -> None:
        ...
    
    @log_start_end(log=logger)
    def check_credentials(self): # -> bool:
        ...
    


