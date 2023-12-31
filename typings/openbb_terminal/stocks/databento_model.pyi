"""
This type stub file was generated by pyright.
"""

import pandas as pd
from pydantic import BaseModel
from openbb_terminal.decorators import check_api_key, log_start_end

__docformat__ = ...
logger = ...
class DataBento(BaseModel):
    symbol: str
    exchange: str = ...
    stype: str = ...
    start: str = ...
    end: str = ...
    class Config:
        arbitrary_types_allowed = ...
    
    
    def get_historical_stock(self): # -> DataFrame:
        """Gets historical EOD stock data from DataBento.  Currently, just NASDAQ is supported.
        Note that only nonadjusted data is available."""
        ...
    
    def get_historical_futures(self): # -> DataFrame:
        """Gets historical EODfutures data from DataBento.  Currently, just CME is supported.
        Note this gets the highest volume contract each day"""
        ...
    
    @log_start_end(log=logger)
    @check_api_key(["API_DATABENTO_KEY"])
    def get_historical(self) -> pd.DataFrame:
        """Prepares the request to be made.  I am using their https interface instead of their python client.
        This updated to .C.0"""
        ...
    
    def process_request(self, base_url, params, auth) -> pd.DataFrame:
        """Takes the request and returns the adjusted dataframe"""
        ...
    


@log_start_end(log=logger)
@check_api_key(["API_DATABENTO_KEY"])
def get_historical_stock(symbol: str, start_date: str, end_date: str) -> pd.DataFrame:
    """Gets historical EOD data from DataBento.  Currently, just NASDAQ is supported.

    Parameters
    ----------
    symbol : str
        Symbol to get data for
    start_date : str
        Start date of data
    end_date : str
        End date to get data for

    """
    ...

@log_start_end(log=logger)
@check_api_key(["API_DATABENTO_KEY"])
def get_historical_futures(symbol: str, start_date: str, end_date: str) -> pd.DataFrame:
    """Gets historical EODfutures data from DataBento.  Currently, just CME is supported.

    Parameters
    ----------
    symbol : str
        Symbol to get data for
    start_date : str
        Start date of data
    end_date : str
        End date to get data for

    """
    ...

