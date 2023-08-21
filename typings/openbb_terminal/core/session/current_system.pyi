"""
This type stub file was generated by pyright.
"""

from typing import Any
from openbb_terminal.core.models import SystemModel

def get_current_system() -> SystemModel:
    """Get current system."""
    ...

def set_current_system(system: SystemModel): # -> None:
    """Set current system."""
    ...

def set_system_variable(name: str, value: Any): # -> None:
    """Set system variable

    Parameters
    ----------
    name : str
        Variable name
    value : Any
        Variable value
    """
    ...

__env_dict = ...
__system = ...