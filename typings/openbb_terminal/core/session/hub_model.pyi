"""
This type stub file was generated by pyright.
"""

import requests
from typing import Any, List, Literal, Optional
from uuid import UUID

def create_session(email: str, password: str, base_url: str = ..., timeout: int = ...) -> Optional[requests.Response]:
    """Create a session.

    Parameters
    ----------
    email : str
        The email.
    password : str
        The password.
    base_url : str
        The base url, by default BASE_URL
    timeout : int
        The timeout, by default TIMEOUT

    Returns
    -------
    Optional[requests.Response]
        The response from the login request.
    """
    ...

def check_token_expiration(token: str): # -> None:
    """Raises ExpiredSignatureError if the token is expired."""
    ...

def create_session_from_token(token: str, base_url: str = ..., timeout: int = ...): # -> Response | None:
    """Create a session from token.

    Parameters
    ----------
    token : str
        The token.
    base_url : str
        The base url, by default BASE_URL
    timeout : int
        The timeout, by default TIMEOUT
    """
    ...

def delete_session(auth_header: str, token: str, base_url: str = ..., timeout: int = ...) -> Optional[requests.Response]:
    """Delete the session.

    Parameters
    ----------
    auth_header : str
        The authorization header, e.g. "Bearer <token>".
    token : str
        The token to delete.
    base_url : str
        The base url, by default BASE_URL
    timeout : int
        The timeout, by default TIMEOUT

    Returns
    -------
    Optional[requests.Response]
        The response from the logout request.
    """
    ...

def process_session_response(response: requests.Response) -> dict:
    """Process the response from the login request.

    Parameters
    ----------
    response : requests.Response
        The response from the login request.

    Returns
    -------
    dict
        The login info.
    """
    ...

def get_session(email: str, password: str) -> dict:
    """Get the session info.

    Parameters
    ----------
    email : str
        The email.
    password : str
        The password.

    Returns
    -------
    dict
        The session info.
    """
    ...

def get_session_from_token(token: str) -> dict:
    """Get the session info from token.

    Parameters
    ----------
    token : str
        The token.

    Returns
    -------
    dict
        The session info.
    """
    ...

def fetch_user_configs(session: dict, base_url: str = ..., timeout: int = ...) -> Optional[requests.Response]:
    """Fetch user configurations.

    Parameters
    ----------
    session : dict
        The session info.
    base_url : str
        The base url, by default BASE_URL
    timeout : int
        The timeout, by default TIMEOUT

    Returns
    -------
    Optional[requests.Response]
        The response from the get request.
    """
    ...

def clear_user_configs(config: str, auth_header: str, base_url: str = ..., timeout: int = ...) -> Optional[requests.Response]:
    """Clear user configurations to the server.

    Parameters
    ----------
    config : str
        The config to clear.
    auth_header : str
        The authorization header, e.g. "Bearer <token>".
    base_url : str
        The base url, by default BASE_URL
    timeout : int
        The timeout, by default TIMEOUT

    Returns
    -------
    Optional[requests.Response]
        The response from the put request.
    """
    ...

def upload_user_field(key: str, value: Any, auth_header: str, base_url: str = ..., timeout: int = ..., silent: bool = ...) -> Optional[requests.Response]:
    """Send user field to the server.

    Parameters
    ----------
    key : str
        The key to put, e.g. 'features_settings', 'features_keys', 'features_sources'.
    value : Any
        The value to put.
    auth_header : str
        The authorization header, e.g. "Bearer <token>".
    base_url : str
        The base url, by default BASE_URL
    timeout : int
        The timeout, by default TIMEOUT
    silent : bool
        Whether to silence the console output, by default False

    Returns
    -------
    Optional[requests.Response]
        The response from the put request.
    """
    ...

def upload_config(key: str, value: str, type_: Literal["settings", "terminal_style"], auth_header: str, base_url: str = ..., timeout: int = ...) -> Optional[requests.Response]:
    """Patch user configurations to the server.

    Parameters
    ----------
    key : str
        The key to patch.
    value : str
        The value to patch.
    type_ : Literal["settings", "terminal_style"]
        The type of the patch.
    auth_header : str
        The authorization header, e.g. "Bearer <token>".
    base_url : str
        The base url, by default BASE_URL
    timeout : int
        The timeout, by default TIMEOUT

    Returns
    -------
    Optional[requests.Response]
        The response from the patch request.
    """
    ...

def upload_routine(auth_header: str, name: str = ..., description: str = ..., routine: str = ..., override: bool = ..., tags: str = ..., public: bool = ..., base_url: str = ..., timeout: int = ...) -> Optional[requests.Response]:
    """Send a routine to the server.

    Parameters
    ----------
    auth_header : str
        The authorization header, e.g. "Bearer <token>".
    name : str
        The name of the routine.
    routine : str
        The routine.
    override : bool
        Whether to override the routine if it already exists.
    tags : str
        The tags of the routine.
    public : bool
        Whether to make the routine public or not.
    base_url : str
        The base url, by default BASE_URL
    timeout : int
        The timeout, by default TIMEOUT

    Returns
    -------
    Optional[requests.Response]
        The response from the post request.
    """
    ...

def download_routine(auth_header: str, uuid: UUID, base_url: str = ..., timeout: int = ...) -> Optional[requests.Response]:
    """Download a routine from the server.

    Parameters
    ----------
    auth_header : str
        The authorization header, e.g. "Bearer <token>".
    uuid : UUID
        The uuid of the routine.
    base_url : str
        The base url, by default BASE_URL
    timeout : int
        The timeout, by default TIMEOUT

    Returns
    -------
    Optional[requests.Response]
        The response from the get request.
    """
    ...

def delete_routine(auth_header: str, uuid: UUID, base_url: str = ..., timeout: int = ...) -> Optional[requests.Response]:
    """Delete a routine from the server.

    Parameters
    ----------
    auth_header : str
        The authorization header, e.g. "Bearer <token>".
    uuid : UUID
        The uuid of the routine.
    base_url : str
        The base url, by default BASE_URL
    timeout : int
        The timeout, by default TIMEOUT

    Returns
    -------
    Optional[requests.Response]
        The response from the delete request.
    """
    ...

def list_routines(auth_header: str, fields: Optional[List[str]] = ..., page: int = ..., size: int = ..., base_url: str = ..., timeout: int = ..., silent: bool = ...) -> Optional[requests.Response]:
    """List all routines from the server.

    Parameters
    ----------
    auth_header : str
        The authorization header, e.g. "Bearer <token>".
    fields : Optional[List[str]]
        The fields to return, by default None
    page : int
        The page number.
    size : int
        The number of routines per page.
    base_url : str
        The base url, by default BASE_URL
    timeout : int
        The timeout, by default TIMEOUT
    silent : bool
        Whether to silence the console output, by default False

    Returns
    -------
    Optional[requests.Response]
        The response from the get request.
    """
    ...

def get_default_routines(url: str = ..., timeout: int = ..., silent: bool = ...): # -> Response | None:
    """Get the default routines from CMS.

    Parameters
    ----------
    timeout : int
        The timeout, by default TIMEOUT
    silent : bool
        Whether to silence the console output, by default False

    Returns
    -------
    Optional[requests.Response]
        The response from the get request.
    """
    ...

def generate_personal_access_token(auth_header: str, base_url: str = ..., timeout: int = ..., days: int = ...) -> Optional[requests.Response]:
    """
    Generate an OpenBB Personal Access Token.

    Parameters
    ----------
    auth_header : str
        The authorization header, e.g. "Bearer <token>".
    base_url : str
        The base url, by default BASE_URL
    timeout : int
        The timeout, by default TIMEOUT
    days : int
        The number of days the token should be valid for.

    Returns
    -------
    Optional[requests.Response]
    """
    ...

def get_personal_access_token(auth_header: str, base_url: str = ..., timeout: int = ...) -> Optional[requests.Response]:
    """
    Show the user's OpenBB Personal Access Token.

    Parameters
    ----------
    auth_header : str
        The authorization header, e.g. "Bearer <token>".
    base_url : str
        The base url, by default BASE_URL
    timeout : int
        The timeout, by default TIMEOUT

    Returns
    -------
    Optional[requests.Response]
    """
    ...

def revoke_personal_access_token(auth_header: str, base_url: str = ..., timeout: int = ...) -> Optional[requests.Response]:
    """
    Delete the user's OpenBB Personal Access Token.

    Parameters
    ----------
    auth_header : str
        The authorization header, e.g. "Bearer <token>".
    base_url : str
        The base url, by default BASE_URL
    timeout : int
        The timeout, by default TIMEOUT

    Returns
    -------
    Optional[requests.Response]
    """
    ...

