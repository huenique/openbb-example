"""
This type stub file was generated by pyright.
"""

from typing import Any, Dict, Optional
from openbb_terminal.core.models import CredentialsModel, PreferencesModel, ProfileModel, SourcesModel, UserModel

__env_dict = ...
__credentials = ...
__preferences = ...
__sources = ...
__profile = ...
__local_user = ...
__current_user = ...
def get_current_user() -> UserModel:
    """Get current user."""
    ...

def set_current_user(user: UserModel): # -> None:
    """Set current user."""
    ...

def get_env_dict() -> dict:
    """Get env dict."""
    ...

def is_local() -> bool:
    """Check if user is guest.

    Returns
    -------
    bool
        True if user is guest, False otherwise.
    """
    ...

def set_default_user(): # -> None:
    """Set default user."""
    ...

def copy_user(sources: Optional[SourcesModel] = ..., credentials: Optional[CredentialsModel] = ..., preferences: Optional[PreferencesModel] = ..., profile: Optional[ProfileModel] = ..., user: Optional[UserModel] = ...): # -> UserModel:
    ...

def set_preference(name: str, value: Any): # -> None:
    """Set preference

    Parameters
    ----------
    name : str
        Preference name
    value : Any
        Preference value
    """
    ...

def set_credential(name: str, value: str): # -> None:
    """Set credential

    Parameters
    ----------
    name : str
        Credential name
    value : str
        Credential value
    """
    ...

def set_sources(choices: Dict): # -> None:
    """Set sources

    Parameters
    ----------
    choices : Dict
        Sources dict
    """
    ...
