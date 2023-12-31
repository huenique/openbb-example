"""
This type stub file was generated by pyright.
"""

from pathlib import Path
from typing import Any, Dict
from openbb_terminal.core.log.generation.settings import AWSSettings

def send_to_s3_directly(aws_access_key_id: str, aws_secret_access_key: str, bucket: str, file: Path, object_key: str): # -> None:
    ...

def fetch_presigned_url(api_url: str, object_key: str) -> Dict[str, Any]:
    ...

def send_to_s3_using_presigned_url(api_url: str, file: Path, object_key: str): # -> None:
    ...

def send_to_s3(archives_file: Path, aws_settings: AWSSettings, file: Path, object_key: str, tmp_file: Path, last: bool = ...): # -> None:
    """Send a file into a s3 bucket.

    Args:
        archives_file (Path):
            Destination Path after processing.
        aws_settings (AWSSettings):
            AWS settings.
        file (Path):
            Path of the file to process.
        object_key (str): _description_
            File location inside the s3 bucket.
        tmp_file (Path):
            Temporary Path in which to put the file during processing.
        last (bool, optional):
            Whether or not this is the last sending before program exit.
            Defaults to False.

    Raises:
        AttributeError:
            If `file` is empty.
    """
    ...

