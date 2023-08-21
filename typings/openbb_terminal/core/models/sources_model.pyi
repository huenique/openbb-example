"""
This type stub file was generated by pyright.
"""

from typing import Dict, List
from pydantic.dataclasses import dataclass
from openbb_terminal.core.models.base_model import BaseModel

def read_default_sources() -> Dict:
    """Read default sources from file.

    Returns
    -------
    Dict
        Dictionary with sources
    """
    ...

__allowed = ...
def get_allowed_sources() -> Dict:
    """Get allowed sources.

    Returns
    -------
    Dict
        Dictionary with sources
    """
    ...

@dataclass(config=dict(validate_assignment=True))
class SourcesModel(BaseModel):
    """Model for sources."""
    choices: Dict[str, List[str]] = ...
    def __repr__(self): # -> str:
        ...
    

