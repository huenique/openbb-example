"""
This type stub file was generated by pyright.
"""

import sys
from typing import Optional
from prompt_toolkit import PromptSession

logger = ...
def is_jupyter() -> bool:
    ...

def is_papermill() -> bool:
    """Check if session is being launched with args '-m ipykernel_launcher',
    thus coming from papermill Popen. See 'ipykernel_launcher' in reports_model
    for more detail.
    """
    ...

def inputhook(inputhook_context): # -> Literal[False]:
    ...

if sys.stdin.isatty():
    session: Optional[PromptSession] = ...
else:
    session = ...