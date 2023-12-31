"""
This type stub file was generated by pyright.
"""

from typing import Dict
from openbb_terminal.decorators import log_start_end

"""FinancialModelingPrep model"""
__docformat__ = ...
logger = ...
@log_start_end(log=logger)
def get_etf_sector_weightings(name: str) -> Dict:
    """Return sector weightings allocation of ETF. [Source: FinancialModelingPrep]

    Parameters
    ----------
    name: str
        ETF name

    Returns
    -------
    Dict[str, Any]
        Dictionary with sector weightings allocation
    """
    ...

