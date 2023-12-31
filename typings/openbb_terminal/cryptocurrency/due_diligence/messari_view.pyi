"""
This type stub file was generated by pyright.
"""

from typing import Optional, Union
from openbb_terminal import OpenBBFigure
from openbb_terminal.decorators import check_api_key, log_start_end

"""Messari view"""
__docformat__ = ...
logger = ...
@log_start_end(log=logger)
@check_api_key(["API_MESSARI_KEY"])
def display_messari_timeseries_list(limit: int = ..., query: str = ..., only_free: bool = ..., export: str = ..., sheet_name: Optional[str] = ...) -> None:
    """Prints table showing messari timeseries list
    [Source: https://messari.io/]

    Parameters
    ----------
    limit : int
        number to show
    query : str
        Query to search across all messari timeseries
    only_free : bool
        Display only timeseries available for free
    export : str
        Export dataframe data to csv,json,xlsx file
    """
    ...

@log_start_end(log=logger)
@check_api_key(["API_MESSARI_KEY"])
def display_messari_timeseries(symbol: str, timeseries_id: str, start_date: Optional[str] = ..., end_date: Optional[str] = ..., interval: str = ..., export: str = ..., sheet_name: Optional[str] = ..., external_axes: bool = ...) -> Union[None, OpenBBFigure]:
    """Plots messari timeseries
    [Source: https://messari.io/]

    Parameters
    ----------
    symbol : str
        Crypto symbol to check market cap dominance
    timeseries_id: str
        Obtained by api.crypto.dd.get_mt command
    start_date : Optional[str]
        Initial date like string (e.g., 2021-10-01)
    end_date : Optional[str]
        End date like string (e.g., 2021-10-01)
    interval : str
        Interval frequency (possible values are: 5m, 15m, 30m, 1h, 1d, 1w)
    export : str
        Export dataframe data to csv,json,xlsx file
    external_axes : bool, optional
        Whether to return the figure object or not, by default False
    """
    ...

@log_start_end(log=logger)
@check_api_key(["API_MESSARI_KEY"])
def display_marketcap_dominance(symbol: str, start_date: Optional[str] = ..., end_date: Optional[str] = ..., interval: str = ..., export: str = ..., sheet_name: Optional[str] = ..., external_axes: bool = ...) -> Union[None, OpenBBFigure]:
    """Plots market dominance of a coin over time
    [Source: https://messari.io/]

    Parameters
    ----------
    symbol : str
        Crypto symbol to check market cap dominance
    start_date : Optional[str]
        Initial date like string (e.g., 2021-10-01)
    end_date : Optional[str]
        End date like string (e.g., 2021-10-01)
    interval : str
        Interval frequency (possible values are: 5m, 15m, 30m, 1h, 1d, 1w)
    export : str
        Export dataframe data to csv,json,xlsx file
    external_axes : bool, optional
        Whether to return the figure object or not, by default False
    """
    ...

@log_start_end(log=logger)
@check_api_key(["API_MESSARI_KEY"])
def display_links(symbol: str, export: str = ..., sheet_name: Optional[str] = ...) -> None:
    """Prints table showing coin links
    [Source: https://messari.io/]

    Parameters
    ----------
    symbol : str
        Crypto symbol to check links
    export : str
        Export dataframe data to csv,json,xlsx file
    external_axes : bool, optional
        Whether to return the figure object or not, by default False
    """
    ...

@log_start_end(log=logger)
@check_api_key(["API_MESSARI_KEY"])
def display_roadmap(symbol: str, ascend: bool = ..., limit: int = ..., export: str = ..., sheet_name: Optional[str] = ..., external_axes: bool = ...) -> Union[None, OpenBBFigure]:
    """Plots coin roadmap
    [Source: https://messari.io/]

    Parameters
    ----------
    symbol : str
        Crypto symbol to check roadmap
    ascend: bool
        reverse order
    limit : int
        number to show
    export : str
        Export dataframe data to csv,json,xlsx file
    external_axes : bool, optional
        Whether to return the figure object or not, by default False
    """
    ...

@log_start_end(log=logger)
@check_api_key(["API_MESSARI_KEY"])
def display_tokenomics(symbol: str, export: str = ..., sheet_name: Optional[str] = ..., external_axes: bool = ...) -> Union[None, OpenBBFigure]:
    """Plots coin tokenomics
    [Source: https://messari.io/]

    Parameters
    ----------
    symbol : str
        Crypto symbol to check tokenomics
    export : str
        Export dataframe data to csv,json,xlsx file
    external_axes : bool, optional
        Whether to return the figure object or not, by default False
    """
    ...

@log_start_end(log=logger)
@check_api_key(["API_MESSARI_KEY"])
def display_project_info(symbol: str, export: str = ..., sheet_name: Optional[str] = ...) -> None:
    """Prints table showing project info
    [Source: https://messari.io/]

    Parameters
    ----------
    symbol : str
        Crypto symbol to check project info
    export : str
        Export dataframe data to csv,json,xlsx file
    """
    ...

@log_start_end(log=logger)
@check_api_key(["API_MESSARI_KEY"])
def display_investors(symbol: str, export: str = ..., sheet_name: Optional[str] = ...) -> None:
    """Prints table showing coin investors
    [Source: https://messari.io/]

    Parameters
    ----------
    symbol : str
        Crypto symbol to check coin investors
    export : str
        Export dataframe data to csv,json,xlsx file
    """
    ...

@log_start_end(log=logger)
@check_api_key(["API_MESSARI_KEY"])
def display_team(symbol: str, export: str = ..., sheet_name: Optional[str] = ...) -> None:
    """Prints table showing coin team
    [Source: https://messari.io/]

    Parameters
    ----------
    symbol : str
        Crypto symbol to check coin team
    export : str
        Export dataframe data to csv,json,xlsx file
    """
    ...

@log_start_end(log=logger)
@check_api_key(["API_MESSARI_KEY"])
def display_governance(symbol: str, export: str = ..., sheet_name: Optional[str] = ...) -> None:
    """Prints table showing coin governance
    [Source: https://messari.io/]

    Parameters
    ----------
    symbol : str
        Crypto symbol to check coin governance
    export : str
        Export dataframe data to csv,json,xlsx file
    """
    ...

@log_start_end(log=logger)
@check_api_key(["API_MESSARI_KEY"])
def display_fundraising(symbol: str, export: str = ..., sheet_name: Optional[str] = ..., external_axes: bool = ...) -> Union[OpenBBFigure, None]:
    """Display coin fundraising
    [Source: https://messari.io/]

    Parameters
    ----------
    symbol : str
        Crypto symbol to check coin fundraising
    export : str
        Export dataframe data to csv,json,xlsx file
    external_axes : bool, optional
        Whether to return the figure object or not, by default False
    """
    ...

