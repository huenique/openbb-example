"""
This type stub file was generated by pyright.
"""

from logging import Logger
from typing import Any, Callable, Dict, Optional
from openbb_terminal.core.sdk.sdk_init import FORECASTING_TOOLKIT_ENABLED, OPTIMIZATION_TOOLKIT_ENABLED
from openbb_terminal.core.session.current_system import get_current_system

"""OpenBB Terminal SDK Helpers."""
if (notFORECASTING_TOOLKIT_ENABLED and notget_current_system().DISABLE_FORECASTING_WARNING):
    ...
if (notOPTIMIZATION_TOOLKIT_ENABLED and notget_current_system().DISABLE_OPTIMIZATION_WARNING):
    ...
def clean_attr_desc(attr: Optional[Any] = ...) -> Optional[str]:
    """Clean the attribute description."""
    ...

def class_repr(cls_dict: Dict[str, Any]) -> list:
    """Return the representation of the class."""
    ...

class Operation:
    def __init__(self, name: str, trail: str, func: Callable) -> None:
        ...
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        ...
    
    def about(self): # -> None:
        ...
    


class Category:
    """The base class that all categories must inherit from."""
    _location_path: str = ...
    def __init__(self, *args, **kwargs) -> None:
        """Initialize the class"""
        ...
    
    def __repr__(self): # -> str:
        """Return the representation of the class."""
        ...
    
    def __getattribute__(self, name: str): # -> Operation | Any:
        """We override the __getattribute__ method and wrap all callable



        attributes with a wrapper that logs the call and the result.



        """
        ...
    
    def about(self): # -> None:
        ...
    


class OperationLogger:
    last_method: Dict[Any, Any] = ...
    def __init__(self, trail: str, method_chosen: Callable, args: Any, kwargs: Any, logger: Optional[Logger] = ...) -> None:
        ...
    
    def log_before_call(self): # -> None:
        ...
    
    def log_after_call(self, method_result: Any): # -> None:
        ...
    


def get_sdk_imports_text() -> str:
    """Return the text for the SDK imports."""
    ...

