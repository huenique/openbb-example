"""
This type stub file was generated by pyright.
"""

import datetime as dt
import pandas as pd
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union
from bs4 import BeautifulSoup

"""CoinGecko helpers"""
__docformat__ = ...
logger = ...
GECKO_BASE_URL = ...
DENOMINATION = ...
def millify(n: Union[float, int]) -> str:
    ...

def calc_change(current: Union[float, int], previous: Union[float, int]): # -> float | Literal[0]:
    """Calculates change between two different values"""
    ...

def get_btc_price() -> float:
    """Get BTC/USD price from CoinGecko API

    Returns
    -------
    str
        latest bitcoin price in usd.
    """
    ...

def scrape_gecko_data(url: str) -> BeautifulSoup:
    """Helper method that scrape Coin Gecko site.

    Parameters
    ----------
    url : str
        coin gecko url to scrape e.g: "https://www.coingecko.com/en/discover"

    Returns
    -------
        BeautifulSoup object
    """
    ...

def replace_underscores_to_newlines(cols: list, line: int = ...) -> list:
    """Helper method that replace underscores to white space and breaks it to new line

    Parameters
    ----------
    cols
        - list of columns names
    line
        - line length
    Returns
    -------
        list of column names with replaced underscores
    """
    ...

def find_discord(item: Optional[List[Any]]) -> Union[str, Any]:
    ...

def join_list_elements(elem): # -> LiteralString | None:
    ...

def filter_list(lst: Optional[List[Any]]) -> Optional[List[Any]]:
    ...

def calculate_time_delta(date: dt.datetime) -> int:
    ...

def get_eth_addresses_for_cg_coins(file) -> pd.DataFrame:
    ...

def clean_question_marks(dct: dict) -> None:
    ...

def replace_qm(df: pd.DataFrame) -> pd.DataFrame:
    ...

def get_url(url: str, elem: BeautifulSoup):
    ...

def clean_row(row: BeautifulSoup) -> list:
    """Helper method that cleans whitespaces and newlines in text returned from BeautifulSoup
    Parameters
    ----------
    row
        text returned from BeautifulSoup find method
    Returns
    -------
        list of elements
    """
    ...

def convert(word: str) -> str:
    ...

def collateral_auditors_parse(args: Any) -> Tuple[Any, Any]:
    ...

def swap_columns(df: pd.DataFrame) -> pd.DataFrame:
    ...

def changes_parser(changes: list) -> list:
    ...

def remove_keys(entries: tuple, the_dict: Dict[Any, Any]) -> None:
    ...

def rename_columns_in_dct(dct: dict, mapper: dict) -> dict:
    ...

def create_dictionary_with_prefixes(columns: Sequence[Any], dct: Dict[Any, Any], constrains: Optional[Tuple] = ...): # -> dict[Unknown, Unknown]:
    ...

