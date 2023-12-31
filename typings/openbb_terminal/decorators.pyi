"""
This type stub file was generated by pyright.
"""

"""Decorators"""
__docformat__ = ...
logger = ...
def log_start_end(func=..., log=...): # -> _Wrapped[(...), Unknown, (*args: Unknown, **kwargs: Unknown), Unknown | list[Unknown]] | ((func: Unknown) -> _Wrapped[(...), Unknown, (*args: Unknown, **kwargs: Unknown), Unknown | list[Unknown]]):
    """Wrap function to add a log entry at execution start and end.

    Parameters
    ----------
    func : optional
        Function, by default None
    log : optional
        Logger, by default None

    Returns
    -------
        Wrapped function
    """
    ...

def check_api_key(api_keys): # -> (func: Unknown) -> _Wrapped[(...), Unknown, (*args: Unknown, **kwargs: Unknown), Unknown | None]:
    """
    Wrapper around the view or controller function and
    print message statement to the console if API keys are not yet defined.
    """
    ...

def disable_check_api(): # -> None:
    ...

