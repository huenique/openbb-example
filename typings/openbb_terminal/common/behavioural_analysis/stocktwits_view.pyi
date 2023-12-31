"""
This type stub file was generated by pyright.
"""

from openbb_terminal.decorators import log_start_end

"""Stocktwits View"""
__docformat__ = ...
logger = ...
@log_start_end(log=logger)
def display_bullbear(symbol: str): # -> None:
    """
    Print bullbear sentiment based on last 30 messages on the board.
    Also prints the watchlist_count. [Source: Stocktwits]

    Parameters
    ----------
    symbol: str
        Stock ticker symbol
    """
    ...

@log_start_end(log=logger)
def display_messages(symbol: str, limit: int = ...): # -> None:
    """Prints up to 30 of the last messages on the board. [Source: Stocktwits].

    Parameters
    ----------
    symbol: str
        Stock ticker symbol
    limit: int
        Number of messages to get
    """
    ...

@log_start_end(log=logger)
def display_trending(): # -> None:
    """Show trensing stocks on stocktwits."""
    ...

@log_start_end(log=logger)
def display_stalker(user: str, limit: int = ...): # -> None:
    """Show last posts for given user.

    Parameters
    ----------
    user : str
        Stocktwits username
    limit : int, optional
        Number of messages to show, by default 10
    """
    ...

