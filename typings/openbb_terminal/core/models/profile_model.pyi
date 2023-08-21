"""
This type stub file was generated by pyright.
"""

from typing import Dict
from pydantic.dataclasses import dataclass
from openbb_terminal.core.models import BaseModel

@dataclass(config=dict(validate_assignment=True, frozen=True))
class ProfileModel(BaseModel):
    """Data model for profile."""
    token_type: str = ...
    token: str = ...
    uuid: str = ...
    email: str = ...
    username: str = ...
    primary_usage: str = ...
    remember: bool = ...
    def load_user_info(self, session: dict, email: str, remember: bool): # -> None:
        """Load user info from login info.

        Parameters
        ----------
        session : dict
            The login info.
        email : str
            The email.
        remember : bool
            Remember the session.
        """
        ...
    
    def get_uuid(self) -> str:
        """Get uuid.

        Returns
        -------
        str
            The uuid.
        """
        ...
    
    def get_token(self) -> str:
        """Get token.

        Returns
        -------
        str
            The token.
        """
        ...
    
    def get_session(self) -> Dict[str, str]:
        """Get session info.

        Returns
        -------
        Dict[str, str]
            The session info.
        """
        ...
    
    def get_auth_header(self) -> str:
        """Get auth header.

        Returns
        -------
        str
            The auth header, e.g. "Bearer <token>".
        """
        ...
    
    def __repr__(self) -> str:
        ...
    


